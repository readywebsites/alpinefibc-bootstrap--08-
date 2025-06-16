from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),
    path('index.html', views.home, name='home_html'),

    # About
    path('about/', views.about_view, name='about_view'),
    path('about.html', views.about_view, name='about_html'),

    # Products Page
    path('products/', views.products, name='products'),
    path('products.html', views.products, name='products_html'),

    # Other Pages
    path('quality/', views.quality, name='quality'),
    path('quality.html', views.quality, name='quality_html'),

    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('infrastructure.html', views.infrastructure, name='infrastructure_html'),

    path('certification/', views.certification, name='certification'),
    path('certification.html', views.certification, name='certification_html'),

    path('blog/', views.blog, name='blog'),
    path('blog.html', views.blog, name='blog_html'),

    path('contact/', views.contact, name='contact'),
    path('contact.html', views.contact, name='contact_html'),

    path('career/', views.career, name='career'),
    path('career.html', views.career, name='career_html'),

    # Why Use FIBCs page
    path('why-use-fibcs/', views.why_use_fibcs, name='why_use_fibcs'),
    path('why-use-fibcs.html', views.why_use_fibcs),  # Optional if you want `.html` access
  

    # Product Detail Pages (both clean and .html)
    path('u-panel-fibc/', views.u_panel_fibc, name='u_panel_fibc'),
    path('circular-fibc/', views.circular_fibc, name='circular_fibc'),
    path('baffle-fibc-bags/', views.baffle_fibc_bags, name='baffle_fibc_bags'),
    path('un-fibc-bags/', views.un_fibc_bags, name='un_fibc_bags'),
    path('food-grade-fibc-bags/', views.food_grade_fibc_bags, name='food_grade_fibc_bags'),
    path('ventilated-fibc-bags/', views.ventilated_fibc_bags, name='ventilated_fibc_bags'),
    path('conductive-fibc-bags/', views.conductive_fibc_bags, name='conductive_fibc_bags'),
    path('fibc-liners/', views.fibc_liners, name='fibc_liners'),
    path('pp-woven-ground-cover/', views.pp_woven_ground_cover, name='pp_woven_ground_cover'),
    path('fibc-bags/', views.fibc_bags, name='fibc_bags'),
    path('dissipative-fibc-bags/', views.dissipative_fibc_bags, name='dissipative_fibc_bags'),
    path('4-panel-fibc-bags/', views.four_panel_fibc_bags, name='four_panel_fibc_bags'),
    path('conical-fibc-bags/', views.conical_fibc_bags, name='conical_fibc_bags'),
    path('pharma-grade-fibc-bags/', views.pharma_grade_fibc_bags, name='pharma_grade_fibc_bags'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)