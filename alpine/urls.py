from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),

    path('about.html', views.about_view, name='about_view'),
    path('products.html', views.products, name='products'),
    path('quality.html', views.quality, name='quality'),
    path('infrastructure.html', views.infrastructure, name='infrastructure'),
    path('certification.html', views.certification, name='certification'),
    path('blog.html', views.blog, name='blog'),
    path('contact.html', views.contact, name='contact'),
    path('career.html', views.career, name='career'),

    # Product URLs
    path('u-panel-fibc.html', views.u_panel_fibc, name='u-panel-fibc'),
    path('un-fibc-bags.html', views.un_fibc_bags, name='un-fibc-bags'),
    path('circular-fibc.html', views.circular_fibc, name='circular-fibc'),
    path('baffle-fibc-bags.html', views.baffle_fibc_bags, name='baffle-fibc-bags'),
    path('food-grade-fibc-bags.html', views.food_grade_fibc_bags, name='food-grade-fibc-bags'),
    path('ventilated-fibc-bags.html', views.ventilated_fibc_bags, name='ventilated-fibc-bags'),
    path('conductive-fibc-bags.html', views.conductive_fibc_bags, name='conductive-fibc-bags'),
    path('fibc-liners.html', views.fibc_liners, name='fibc-liners'),
    path('pp-woven-ground-cover.html', views.pp_woven_ground_cover, name='pp-woven-ground-cover'),
    path('fibc-bags.html', views.fibc_bags, name='fibc-bags'),
    path('dissipative-fibc-bags.html', views.dissipative_fibc_bags, name='dissipative-fibc-bags'),
    path('4-panel-fibc-bags.html', views.four_panel_fibc_bags, name='4-panel-fibc-bags'),
    path('conical-fibc-bags.html', views.conical_fibc_bags, name='conical-fibc-bags'),
    path('pharma-grade-fibc-bags.html', views.pharma_grade_fibc_bags, name='pharma-grade-fibc-bags'),
    path('why-use-fibcs.html', views.why_use_fibcs, name='why_use_fibcs'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)