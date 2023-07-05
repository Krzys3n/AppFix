from django.shortcuts import render, redirect, get_object_or_404

from AppFixA.forms import AppForm, ReportForm
from AppFixA.models import App, Report


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

def new_report(request, app_id):
    app = get_object_or_404(App, id=app_id)

    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = ReportForm()
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = ReportForm(data=request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.app = app
            report.reportId_id = app.id  # Przypisz poprawny identyfikator reportId_id
            report.save()
            return redirect('apps')

    context = {'form': form, 'app_id': app_id}
    return render(request, 'new_report.html', context)


def edit_report(request, report_id):
    #"""Edycja istniejącego wpisu."""
    report = Report.objects.get(id=report_id)
    app = report.reportId
    if request.method != 'POST':
        # Żądanie początkowe, wypełnienie formularza aktualną treścią wpisu.
        form = ReportForm(instance=report)
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = ReportForm(instance=report, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app', app.id)

    context = {'report': report, 'app': app, 'form': form}
    return render(request, 'edit_report.html', context)