from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
#"""Temat poznawany przez użytkownika."""
    appName = models.CharField(max_length=20)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
#"""Zwraca reprezentację modelu w postaci ciągu tekstowego."""
    return self.text


class Report(models.Model):
#"""Konkretne informacje o postępie w nauce."""
    reportId = models.ForeignKey(App, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'reports'

    def __str__(self):
#"""Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"

