from django.shortcuts import render

from AppFixA.models import App


def index(request):
    return render(request, 'index.html')

def apps(request):
# """Wyświetlenie wszystkich tematów."""
    apps = App.objects.order_by('date_added')
    context = {'apps': apps}
    return render(request, 'apps.html', context)


def app(request, app_id):
    app = App.objects.get(id=app_id)
    reports = app.report_set.order_by('-date_added')
    context = {'app': app, 'reports': reports}
    return render(request, 'app.html', context)