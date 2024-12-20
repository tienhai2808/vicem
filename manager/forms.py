from django import forms
from client.models import BaiViet, DanhMuc


class BieuMauBaiViet(forms.ModelForm):
  class Meta:
    model = BaiViet
    fields = ['tieu_de', 'danh_muc', 'noi_dung', 'hinh_anh']
    labels = {'tieu_de': 'Tiêu đề', 'danh_muc': 'Danh mục', 'noi_dung': 'Nội dung', 'hinh_anh': 'Hình ảnh'}
    

class BieuMauDanhMuc(forms.ModelForm):
  class Meta:
    model = DanhMuc
    fields = '__all__'
    labels = {'ten': 'Tên danh mục', 'slug': 'Slug danh mục'}
    widgets = {'ten': forms.TextInput(attrs={'class': 'form-control'}),
               'slug': forms.TextInput(attrs={'class': 'form-control'})}