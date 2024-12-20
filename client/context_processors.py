from .models import DanhMuc

def danh_muc(request):
  danh_mucs = DanhMuc.objects.all()
  for dm in danh_mucs:
    dm.ten = dm.ten.upper()
  return {'danh_mucs': danh_mucs}