from landing import views
from django.urls import path, re_path

urlpatterns = [

    # authentication
    path("", views.index, name="index"),
    path("faqs", views.faqs, name="faqs"),
    path("about/us", views.about_us, name="about-us"),
    path("legal", views.legal, name="legal"),
    path("refer/and/earn", views.refer_and_earn, name="refer_and_earn"),
    
]