from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('product-page/', product_page, name="product_page"),
    path('product-category-page/<int:id>', product_category_page, name="product_category_page"),
    path('product-details/<int:id>', product_details, name="product_details"),
    path('blog-full-width/', blog_full_width, name="blog_full_width"),
    path('blog-details/<int:id>', blog_details, name='blog_details'),
    path('contac-us/', contact, name="contact_us"),
    path('about-us/', about, name="about_us"),
    path('faqs/', faqs, name="faqs"),
    path('terms-condition/', terms_condition, name="terms_condition"),
    path('privacy-policy/', privacy_policy, name="privacy_policy"),



    path('carts/', carts, name="carts"),
    path('checkout/', checkout, name="checkout"),
    path('compare/', compare, name="compare"),
    path('track_order/', track_order, name="track_order"),
    path('wishlist/', wishlist, name="wishlist"),
    path('blog_left_sidebar/', blog_left_sidebar, name="blog_left_sidebar"),
    path('blog_right_sidebar/', blog_right_sidebar, name="blog_right_sidebar"),
    path('blog_detail_left_sidebar/', blog_detail_left_sidebar, name="blog_detail_left_sidebar"),
    path('blog_detail_right_sidebar/', blog_detail_right_sidebar, name="blog_detail_right_sidebar"),
    path('shop_banner_left_sidebar_col_3/', shop_banner_left_sidebar_col_3, name="shop_banner_left_sidebar_col_3"),
    path('product_left_sidebar/', product_left_sidebar, name="product_left_sidebar"),
    path('product_right_sidebar/', product_right_sidebar, name="product_right_sidebar"),
    path('product_accordion_left_sidebar/', product_accordion_left_sidebar, name="product_accordion_left_sidebar"),
    path('product_accordion_right_sidebar/', product_accordion_right_sidebar, name="product_accordion_right_sidebar"),
    path('product_full_width/', product_full_width, name="product_full_width"),
    path('product_accordion_full_width/', product_accordion_full_width, name="product_accordion_full_width"),
    path('shop_full_width/', shop_full_width, name="shop_full_width"),
    path('shop_banner_left_sidebar_col_4/', shop_banner_left_sidebar_col_4, name="shop_banner_left_sidebar_col_4"),
    path('shop_full_width_col_6/', shop_full_width_col_6, name="shop_full_width_col_6"),
    path('shop_list_right_sidebar/', shop_list_right_sidebar, name="shop_list_right_sidebar"),
]