from django.urls import path
from . views import StoreView, HomeView, MenuView, NewMenu, StoreUpdateView, StoreDeleteView, MenuUpdateView, MenuDeleteView, OrderView
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('add',StoreView.as_view(), name='add-store' ),
    path('update-store/<str:id>',StoreUpdateView.as_view(), name='store-update'),
    path('<pk>/delete-store/', StoreDeleteView.as_view(), name='delete-store'),
    path('menu/<str:id>', MenuView.as_view(), name='menu'),
    path('add-menu/<str:id>',NewMenu.as_view(), name='add-store' ),
    path('update-menu/<str:id>',MenuUpdateView.as_view(), name='menu-update'),
    path('<pk>/delete-menu/', MenuDeleteView.as_view(), name='delete-menu'),
    path('order/<str:id>',OrderView.as_view(), name='order'),
    
    
]