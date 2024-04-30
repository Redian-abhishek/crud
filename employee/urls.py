from django.contrib import admin  
from django.urls import path  
from employee import views  
urlpatterns = [  
    path('', views.landing_page, name='landing_page'),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('/search', views.search, name='search'),

]  