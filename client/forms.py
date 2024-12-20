from django import forms
from django.contrib.auth.models import User
from .models import HoSo, DanhGia

class BieuMauDanhGia(forms.ModelForm):
  class Meta:
    model = DanhGia
    fields = ['so_sao', 'noi_dung']


class BieuMauNguoiDung(forms.ModelForm):
  first_name = forms.CharField(label='Họ', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
  last_name = forms.CharField(label='Tên', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
  email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}), required=False)
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']


class BieuMauHoSo(forms.ModelForm):
  GENDER_CHOICES = [('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Ẩn', 'Ẩn')]
  dien_thoai = forms.CharField(label='Số điện thoại', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
  ngay_sinh = forms.DateField(label='Ngày sinh', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
  gioi_tinh = forms.ChoiceField(choices=GENDER_CHOICES, label='Giới tính', widget=forms.Select(attrs={'class': 'form-select'}), required=False)
  class Meta:
    model = HoSo
    fields = ['dien_thoai', 'ngay_sinh', 'gioi_tinh']
    
