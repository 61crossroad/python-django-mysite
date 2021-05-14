from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.page),
    path('<int:num>/', views.page),

    # TODO resolve <> parameters
    # path('<page_slug>-<page_id>', include([
    #     path('history/', views.history),
    #     path('edit/', views.edit),
    #     path('discuss/', views.discuss),
    #     path('permissions/', views.permissions),
    # ]))
]
