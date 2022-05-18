from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    customer_num = forms.IntegerField()
    reservation_date = forms.CharField(max_length=10)
    reservation_time = forms.CharField(max_length=10)