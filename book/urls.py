from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("store-book", StoreBook.as_view(), name="store-book"),
    path("view-book", ViewBook.as_view(), name="view-book"),
    path("filter", Filter.as_view(), name="filter"),
    path("detailed-view/<id>", DetailedView.as_view(), name="detailed-view"),
]