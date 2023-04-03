from django.urls import path, include

from product import views

urlpattern = [
    path('latest-products/', views.LatestProductList.as_view()),
    

]