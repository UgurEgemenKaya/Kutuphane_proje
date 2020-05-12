from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('update/', views.user_update , name='user_update'),
    path('password/',views.change_password, name='change_password'),
    path('orders/',views.orders, name='orders'),
    path('orderdetail/<int:id>',views.orderdetail, name='orderdetail'),

    #path('addcomment/<int:id>',views.addcomment, name='addcomment'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]