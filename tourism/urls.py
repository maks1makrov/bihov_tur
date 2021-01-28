from django.urls import path, include

from tourism import views

urlpatterns = [
    path('categories', views.ListFieldAPI.as_view(), name='categories'),
    path('categories/<int:id>', views.ListFieldAPI.as_view(), name='one_categories'),
    path('toursites/', views.ListToursitesAPI.as_view(), name="toursites"),
    path('toursites_of_category/<int:id>', views.ListToursitesAPI.as_view(), name="toursites_categories"),
    path('toursite_number/<int:number>', views.ListToursitesAPI.as_view(), name="toursite_full"),
    path('articles', views.ListArticlesAPI.as_view(), name="articles"),
    path('articles/<int:id>', views.ListArticlesAPI.as_view(), name="articles_id"),
    path('test/', views.TestIndex.as_view(), name="test"),

]
