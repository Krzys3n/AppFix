from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    # """Rejestracja nowego użytkownika."""
    if request.method != 'POST':
        # Wyświetlenie pustego formularza rejestracji użytkownika.
        form = UserCreationForm()
    else:
    # Przetworzenie wypełnionego formularza.
        form = UserCreationForm(data=request.POST)
    if form.is_valid():
        new_user = form.save()
    # Zalogowanie użytkownika, a następnie przekierowanie go na stronę główną.
        login(request, new_user)
        return redirect('index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)