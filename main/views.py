from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def quality(request):
    return render(request, 'quality.html')

def infrastructure(request):
    return render(request, 'infrastructure.html')

def certification(request):
    return render(request, 'certification.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def career(request):
    return render(request, 'career.html')

# Product-specific views
def u_panel_fibc(request):
    return render(request, 'u-panel-fibc.html')

def un_fibc_bags(request):
    return render(request, 'un-fibc-bags.html')

def circular_fibc(request):
    return render(request, 'circular-fibc.html')

def baffle_fibc_bags(request):
    return render(request, 'baffle-fibc-bags.html')

def food_grade_fibc_bags(request):
    return render(request, 'food-grade-fibc-bags.html')

def ventilated_fibc_bags(request):
    return render(request, 'ventilated-fibc-bags.html')

def conductive_fibc_bags(request):
    return render(request, 'conductive-fibc-bags.html')

def fibc_liners(request):
    return render(request, 'fibc-liners.html')

def pp_woven_ground_cover(request):
    return render(request, 'pp-woven-ground-cover.html')

def fibc_bags(request):
    return render(request, 'fibc-bags.html')

def dissipative_fibc_bags(request):
    return render(request, 'dissipative-fibc-bags.html')

def four_panel_fibc_bags(request):
    return render(request, '4-panel-fibc-bags.html')

def conical_fibc_bags(request):
    return render(request, 'conical-fibc-bags.html')

def pharma_grade_fibc_bags(request):
    return render(request, 'pharma-grade-fibc-bags.html')


def why_use_fibcs(request):
    return render(request, 'why-use-fibcs.html')

    
