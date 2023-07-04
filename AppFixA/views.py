from django.shortcuts import render, redirect

from AppFixA.forms import AppForm, ReportForm
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


def new_app(request):
    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = AppForm()
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = AppForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('apps')
        # Wyświetlenie pustego formularza.
    context = {'form': form}
    return render(request, 'new_app.html', context)


def new_report(request):
    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = ReportForm()
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = ReportForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('reports')
        # Wyświetlenie pustego formularza.
    context = {'form': form}
    return render(request, 'new_report.html', context)