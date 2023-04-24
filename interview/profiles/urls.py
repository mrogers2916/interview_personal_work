
from django.urls import path
from interview.inventory.views import InventoryLanguageListCreateView, InventoryLanguageRetrieveUpdateDestroyView, InventoryListCreateView, InventoryRetrieveUpdateDestroyView, InventoryTagListCreateView, InventoryTagRetrieveUpdateDestroyView, InventoryTypeListCreateView, InventoryTypeRetrieveUpdateDestroyView, InventoryItemsCreatedCertainDay, InventoryItemsDeactivateOrderView, InventoryItemsDateRange
from interview.order.views import OrderListCreateView, OrderTagListCreateView


urlpatterns = [
    path('', InventoryListCreateView.as_view(), name='inventory-list'),
    
]
