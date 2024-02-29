from django import forms
from .models import *

class MentorForm(forms.ModelForm):
    kelompok = forms.ModelChoiceField(queryset=Kelompok.objects.filter(mentor__isnull=True))
    
    class Meta:
        model = Mentor
        fields = '__all__'

class AcaraForm(forms.ModelForm):
    class Meta:
        model = Acara
        fields = '__all__'
        widgets = {
            'waktu_mulai': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'waktu_selesai': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class PengurusIntiForm(forms.ModelForm):
    class Meta:
        model = PengurusInti
        fields = '__all__'

class BPHForm(forms.ModelForm):
    class Meta:
        model = BPH
        fields = '__all__'

class MenteeForm(forms.ModelForm):
    kelompok = forms.ModelChoiceField(queryset=Kelompok.objects.all())
    class Meta:
        model = Mentee
        fields = '__all__'

class MentoringForm(forms.ModelForm):
    kelompok = forms.ModelChoiceField(queryset=Kelompok.objects.all())
    class Meta:
        model = Mentoring
        fields = ['kelompok', 'waktu', 'tempat', 'materi']

