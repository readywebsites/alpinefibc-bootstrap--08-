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

    # Static Pages
    path('about.html', views.about_view, name='about_html'),
    path('about/', views.about_view, name='about_clean'),

    path('products.html', views.products, name='products_html'),
    path('products/', views.products, name='products_clean'),

    path('quality.html', views.quality, name='quality_html'),
    path('quality/', views.quality, name='quality_clean'),

    path('infrastructure.html', views.infrastructure, name='infrastructure_html'),
    path('infrastructure/', views.infrastructure, name='infrastructure_clean'),

    path('certification.html', views.certification, name='certification_html'),
    path('certification/', views.certification, name='certification_clean'),

    path('blog.html', views.blog, name='blog_html'),
    path('blog/', views.blog, name='blog_clean'),

    path('contact.html', views.contact, name='contact_html'),
    path('contact/', views.contact, name='contact_clean'),

    path('career.html', views.career, name='career_html'),
    path('career/', views.career, name='career_clean'),

    # Product Pages (Both .html and clean URLs)
    path('u-panel-fibc.html', views.u_panel_fibc, name='u_panel_fibc_html'),
    path('u-panel-fibc/', views.u_panel_fibc, name='u_panel_fibc_clean'),

    path('un-fibc-bags.html', views.un_fibc_bags, name='un_fibc_bags_html'),
    path('un-fibc-bags/', views.un_fibc_bags, name='un_fibc_bags_clean'),

    path('circular-fibc.html', views.circular_fibc, name='circular_fibc_html'),
    path('circular-fibc/', views.circular_fibc, name='circular_fibc_clean'),

    path('baffle-fibc-bags.html', views.baffle_fibc_bags, name='baffle_fibc_bags_html'),
    path('baffle-fibc-bags/', views.baffle_fibc_bags, name='baffle_fibc_bags_clean'),

    path('food-grade-fibc-bags.html', views.food_grade_fibc_bags, name='food_grade_fibc_bags_html'),
    path('food-grade-fibc-bags/', views.food_grade_fibc_bags, name='food_grade_fibc_bags_clean'),

    path('ventilated-fibc-bags.html', views.ventilated_fibc_bags, name='ventilated_fibc_bags_html'),
    path('ventilated-fibc-bags/', views.ventilated_fibc_bags, name='ventilated_fibc_bags_clean'),

    path('conductive-fibc-bags.html', views.conductive_fibc_bags, name='conductive_fibc_bags_html'),
    path('conductive-fibc-bags/', views.conductive_fibc_bags, name='conductive_fibc_bags_clean'),

    path('fibc-liners.html', views.fibc_liners, name='fibc_liners_html'),
    path('fibc-liners/', views.fibc_liners, name='fibc_liners_clean'),

    path('pp-woven-ground-cover.html', views.pp_woven_ground_cover, name='pp_woven_ground_cover_html'),
    path('pp-woven-ground-cover/', views.pp_woven_ground_cover, name='pp_woven_ground_cover_clean'),

    path('fibc-bags.html', views.fibc_bags, name='fibc_bags_html'),
    path('fibc-bags/', views.fibc_bags, name='fibc_bags_clean'),

    path('dissipative-fibc-bags.html', views.dissipative_fibc_bags, name='dissipative_fibc_bags_html'),
    path('dissipative-fibc-bags/', views.dissipative_fibc_bags, name='dissipative_fibc_bags_clean'),

    path('4-panel-fibc-bags.html', views.four_panel_fibc_bags, name='four_panel_fibc_bags_html'),
    path('4-panel-fibc-bags/', views.four_panel_fibc_bags, name='four_panel_fibc_bags_clean'),

    path('conical-fibc-bags.html', views.conical_fibc_bags, name='conical_fibc_bags_html'),
    path('conical-fibc-bags/', views.conical_fibc_bags, name='conical_fibc_bags_clean'),

    path('pharma-grade-fibc-bags.html', views.pharma_grade_fibc_bags, name='pharma_grade_fibc_bags_html'),
    path('pharma-grade-fibc-bags/', views.pharma_grade_fibc_bags, name='pharma_grade_fibc_bags_clean'),

    path('why-use-fibcs.html', views.why_use_fibcs, name='why_use_fibcs_html'),
    path('why-use-fibcs/', views.why_use_fibcs, name='why_use_fibcs_clean'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)