from template import views
from django.urls import path, re_path

urlpatterns = [

    # index pages
    path("index", views.index, name="template-index"),
    path("index-2", views.index_2, name="template-index-2"),
    path("index-3", views.index_3, name="template-index-3"),
    path("index-4", views.index_4, name="template-index-4"),
    path("index-5", views.index_5, name="template-index-5"),
    path("index-6", views.index_6, name="template-index-6"),
    path("index-7", views.index_7, name="template-index-7"),
    # {% url 'template-index' %}

    # index single pages
    path("index-1-single", views.index_1_single, name="template-index-1-single"),
    path("index-2-single", views.index_2_single, name="template-index-2-single"),
    path("index-3-single", views.index_3_single, name="template-index-3-single"),
    path("index-4-single", views.index_4_single, name="template-index-4-single"),
    path("index-5-single", views.index_5_single, name="template-index-5-single"),
    path("index-6-single", views.index_6_single, name="template-index-6-single"),
    path("index-7-single", views.index_7_single, name="template-index-7-single"),
    

    # index dark pages
    path("index-1-dark", views.index_1_dark, name="template-index-1-dark"),
    path("index-2-dark", views.index_2_dark, name="template-index-2-dark"),
    path("index-3-dark", views.index_3_dark, name="template-index-3-dark"),
    path("index-4-dark", views.index_4_dark, name="template-index-4-dark"),
    path("index-5-dark", views.index_5_dark, name="template-index-5-dark"),
    path("index-6-dark", views.index_6_dark, name="template-index-6-dark"),
    path("index-7-dark", views.index_7_dark, name="template-index-7-dark"),


    

    # index rtl pages
    path("index-rtl", views.index_rtl, name="template-index-rtl"),


    path("about", views.about, name="template-about"),

    # projects
    path("projects", views.projects, name="template-projects"),
    path("project-details", views.project_details, name="template-project-details"),

    # team
    path("team", views.team, name="template-team"),
    path("team-details", views.team_details, name="template-team-details"),


    path("testimonial", views.testimonial, name="template-testimonial"),
    path("pricing", views.pricing, name="template-pricing"),
    path("faq", views.faq, name="template-faq"),
    path("404", views.page_not_found, name="template-404"),

    # services
    path("services", views.services, name="template-services"),
    path("service-details", views.service_details, name="template-service-details"),

    # shop
    path("shop-products", views.shop_products, name="template-shop-products"),
    path("shop-products-sidebar", views.shop_products_sidebar, name="template-shop-products-sidebar"),
    path("shop-product-details", views.shop_product_details, name="template-shop-product-details"),
    path("shop-cart", views.shop_cart, name="template-shop-cart"),
    path("shop-checkout", views.shop_checkout, name="template-shop-checkout"),

    # news
    path("news-grid", views.news_grid, name="template-news-grid"),
    path("news-details", views.news_details, name="template-news-details"),

    path("contact", views.contact, name="template-contact"),









]