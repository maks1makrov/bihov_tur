from django.urls import path, include

from tourism import views

urlpatterns = [
    path('categories', views.ListFieldAPI.as_view(), name='categories'),
    path('categories/<int:id>', views.ListFieldAPI.as_view(), name='one_categories'),
    path('toursites/', views.ListToursitesAPI.as_view(), name="toursites"),
    path('test/', views.TestIndex.as_view(), name="test"),

]
