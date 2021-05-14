from django.urls import path, re_path, register_converter

from . import views, converters

# register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    # path('2003/', views.special_case_2003),
    # re_path(r'^(?P<year>[0-9]{4}/$)', views.year_archive),
    # re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),

    # with register_converter()
    # path('<yyyy:year>/', views.year_archive),
    # path('<yyyy:year>/<int:month>/', views.month_archive),
    # path('<yyyy:year>/<int:month>/<slug:slug>/', views.article_detail),

    # basic patterns
    path('2003/', views.special_case_2003),
    path('<int:year>/', views.year_archive),
    path('<int:year>/<int:month>/', views.month_archive),
    path('<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
