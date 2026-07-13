def seo_context(request):
    return {
        'site_name': 'Electrorazbor.ru',
        'site_url': request.build_absolute_uri('/'),
        'default_description': 'Запчасти и комплектующие для электросамокатов Ninebot и Xiaomi',
        'default_keywords': 'запчасти электросамокат ninebot xiaomi segway ремонт',
    }