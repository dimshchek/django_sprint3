from django.shortcuts import render


def about(request):
    """Страница about."""
    return render(request, 'pages/about.html')


def rules(request):
    """Страница Правила."""
    return render(request, 'pages/rules.html')
