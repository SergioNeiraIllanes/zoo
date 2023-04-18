from django import forms
from django.contrib.contenttypes.models import ContentType


CHOICES_TYPES = [
    (ct.id, f'{ct.app_label}-{ct.model}')
    for ct in ContentType.objects.all().order_by('id')
]

class PermissionCreateForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    codename = forms.CharField(label='Código', max_length=100)
    content_type = forms.ChoiceField(
        widget=forms.Select,
        choices=CHOICES_TYPES,
    )
