from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string
from django.utils.datetime_safe import datetime

from home.models import UserProfile
from order.models import ShopCartForm, Shopcart, OrderForm, Order, OrderProduct
from books.models import Category, Product


def index(request):
    return HttpResponse("Order App")

@login_required(login_url='/login')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    #***** ürün sepette var mı kontrolü****
    checkproduct = Shopcart.objects.filter(product_id=id)
    if checkproduct:
        control = 1
    else:
        control = 0

    if request.method == 'POST': #ürün detaydan geldiyse
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1: #ürün varsa güncelle
                data = Shopcart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
                messages.success(request, "Ürün başarı ile güncellenmiştir.")
                return HttpResponseRedirect(url)
            else: #ürün yoksa
                data = Shopcart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
                messages.success(request, "Ürün başarı ile sepete eklenmiştir.")
                return HttpResponseRedirect(url)
        request.session['cart_items'] = Shopcart.objects.filter(user_id=current_user.id).count()

    else: # direkt sepete eklendiyse
        if control == 1:  # ürün varsa güncelle
            data = Shopcart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
            messages.success(request, "Ürün başarı ile güncellenmiştir.")
            return HttpResponseRedirect(url)
        else:  # ürün yoksa
            data = Shopcart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
            messages.success(request, "Ürün başarı ile sepete eklenmiştir.")
            return HttpResponseRedirect(url)
        request.session['cart_items'] = Shopcart.objects.filter(user_id=current_user.id).count()
    messages.warning(request,"Ürün sepete eklenemedi hata oluştu")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = Shopcart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = Shopcart.objects.filter(user_id=current_user.id).count()
    total = 0
    for rs in schopcart:
        total += rs.quantity

    context = {'schopcart': schopcart,
               'category': category,
               'total': total,
               }
    return render(request,'Shopcart_products.html', context)

@login_required(login_url='/login')
def deletefromcart(request,id):
    Shopcart.objects.filter(id=id).delete()
    request.session['cart_items'] = Shopcart.objects.filter(user_id=current_user.id).count()
    messages.success(request, "Ürün Sepetten Silinmiştir")
    return HttpResponseRedirect("/shopcart")


@login_required(login_url='/login')
def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user

    schopcart = Shopcart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in schopcart:
        total += rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            tarih = datetime.now()+timedelta(days=15)
            data.teslim_tarih = tarih
            data.code =ordercode
            data.save()

            # Move Shopcart items to order Product items
            schopcart = Shopcart.objects.filter(user_id=current_user.id)
            for rs in schopcart:
                detail = OrderProduct()
                detail.order_id = data.id #order id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity

                #reduce quantity of sold product
                product = Product.objects.get(id=rs.product_id)
                product.amount -=rs.quantity
                product.save()
                #************* <> *********
                detail.save()

            Shopcart.objects.filter(user_id=current_user.id).delete() #clear and delete shop cart
            request.session['cart_items'] = 0
            messages.success(request,"Siparişiniz oluşturuldu, Teşekkür Ederiz")
            return render(request,'Order_Completed.html',{'ordercode':ordercode, 'category': category, 'tarih': tarih })
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect("/order/orderproduct")
    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'schopcart': schopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile
               }
    return render(request,'Order_Form.html', context)






