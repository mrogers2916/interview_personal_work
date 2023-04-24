
from django.urls import path
from interview.inventory.views import InventoryLanguageListCreateView, InventoryLanguageRetrieveUpdateDestroyView, InventoryListCreateView, InventoryRetrieveUpdateDestroyView, InventoryTagListCreateView, InventoryTagRetrieveUpdateDestroyView, InventoryTypeListCreateView, InventoryTypeRetrieveUpdateDestroyView, InventoryItemsCreatedCertainDay, InventoryItemsDeactivateOrderView, InventoryItemsDateRange
from interview.order.views import OrderListCreateView, OrderTagListCreateView


urlpatterns = [
    path('<int:id>/', InventoryRetrieveUpdateDestroyView.as_view(), name='inventory-detail'),
    path('languages/<int:id>/', InventoryLanguageRetrieveUpdateDestroyView.as_view(), name='inventory-languages-detail'),
    path('tags/<int:id>/', InventoryTagRetrieveUpdateDestroyView.as_view(), name='inventory-tags-detail'),
    path('types/<int:id>/', InventoryTypeRetrieveUpdateDestroyView.as_view(), name='inventory-types-detail'),
    path('languages/', InventoryLanguageListCreateView.as_view(), name='inventory-languages-list'),
    path('tags/', InventoryTagListCreateView.as_view(), name='inventory-tags-list'),
    path('types/', InventoryTypeListCreateView.as_view(), name='inventory-types-list'),
    path('', InventoryListCreateView.as_view(), name='inventory-list'),
    path('createdAfter/<str:date>/', InventoryItemsCreatedCertainDay.as_view(), name='inventory-date-created-list'),
    path('deactivate/<int:id>/', InventoryItemsDeactivateOrderView.as_view(), name='inventory-items-deactivate-order-view'),
    path('createdBetween/<str:date1>/<str:date2>/', InventoryItemsDateRange.as_view(), name='inventory-items-date-range'),
    
]
