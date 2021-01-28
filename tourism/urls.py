from django.urls import path, include

from tourism import views

urlpatterns = [
    path('categories/', views.ListFieldAPI.as_view(), name='categories'), #все категории
    path('categories/<int:id>', views.ListFieldAPI.as_view(), name='one_categories'),
    path('toursites/', views.ListToursitesAPI.as_view(), name="toursites"), #все туристические объекты
    path('toursites_of_category/<int:id>/', views.ListToursitesAPI.as_view(), name="toursites_categories"),#тур объекты определенной категории
    path('toursites/<int:number>/', views.ListToursitesAPI.as_view(), name="toursite_full"), #тур объект с конкретным id
    path('articles/', views.ListArticlesAPI.as_view(), name="articles"),#все статьи
    path('articles/<int:id>/', views.ListArticlesAPI.as_view(), name="articles_id"),#статья с конкретным id
    path('test/', views.TestIndex.as_view(), name="test"),

]
