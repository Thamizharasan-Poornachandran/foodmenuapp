from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='food'
urlpatterns = [
    #/food/
    #path('', views.index,name='index'),
    path('', views.IndexClassView.as_view(),name='index'),
    #detail view
    # path('<int:item_id>/',views.detail,name='detail'),
    path('<int:pk>/', login_required(views.FoodDetail.as_view()), name='detail'),
    #update view index
    path('update_view/', views.update_index,name='update_index'),
    #/food/1
    path('item/', views.item,name='item'),
    #Function and Class urls
    #path('add/',views.create_item,name='create_item'),
    path('add/',login_required(views.CreateItem.as_view()),name='create_item'),

    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]


