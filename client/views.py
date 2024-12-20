from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages, auth
from .forms import *
from .models import *
from django.db.models import Q
from datetime import datetime

# Create your views here.
def trang_chu(request):
  bai_viets = BaiViet.objects.filter(
    Q(khung_gio_hien=None, khung_gio_an=None) | Q(khung_gio_hien__lte=datetime.now().time(), khung_gio_an__gte=datetime.now().time()), 
    trang_thai='Đã đăng'
    ).order_by('-thoi_gian_dang')
  return render(request, 'trang-chu.html', {'bai_viets': bai_viets})

def danh_muc_bai_viet(request, slug_danh_muc):
  danh_muc = get_object_or_404(DanhMuc, slug=slug_danh_muc)
  bai_viets = BaiViet.objects.filter(
    Q(khung_gio_hien=None, khung_gio_an=None) | Q(khung_gio_hien__lte=datetime.now().time(), khung_gio_an__gte=datetime.now().time()), 
    trang_thai='Đã đăng', danh_muc=danh_muc
    ).order_by('-thoi_gian_dang')
  return render(request, 'danh-muc-bai-viet.html', {'bai_viets': bai_viets, 'danh_muc': danh_muc})

def tim_kiem(request):
  p = request.GET.get('p', '')
  if p:
    bai_viets = BaiViet.objects.filter(
      Q(khung_gio_hien=None, khung_gio_an=None) | Q(khung_gio_hien__lte=datetime.now().time(), khung_gio_an__gte=datetime.now().time()), 
      trang_thai='Đã đăng', tieu_de__icontains=p
      ).order_by('-thoi_gian_dang')
  else:
    bai_viets = None
  return render(request, 'tim-kiem.html', {'p': p, 'bai_viets': bai_viets})

def bai_viet_chi_tiet(request, slug_bai_viet):
  bai_viet = get_object_or_404(BaiViet, 
                               Q(khung_gio_hien=None, khung_gio_an=None) | Q(khung_gio_hien__lte=datetime.now().time(), khung_gio_an__gte=datetime.now().time()),
                               slug=slug_bai_viet, trang_thai='Đã đăng')
  binh_luans = bai_viet.duoc_binh_luan.filter(da_duyet=True)
  if request.user.is_authenticated:
    if bai_viet.id in request.user.hoso.yeu_thich:
      bai_viet.da_thich = True
    else:
      bai_viet.da_thich = False
  if request.POST:
    if request.user.is_authenticated:
      action = request.POST.get('action', '')
      if action:
        if action == 'like':
          request.user.hoso.them_yeu_thich(bai_viet.id)
        if action == 'cancel_like':
          request.user.hoso.huy_yeu_thich(bai_viet.id)
      else:
        form = BieuMauDanhGia(request.POST)
        if form.is_valid():
          danh_gia = form.save(False)
          danh_gia.nguoi_dung = request.user
          danh_gia.bai_viet = bai_viet
          danh_gia.save()
          messages.success(request, 'Đã gửi bình luận, vui lòng chờ duyệt')
      return redirect('bai-viet-chi-tiet', bai_viet.slug)
    else:
      return redirect('dang-nhap')
  return render(request, 'bai-viet-chi-tiet.html', {'bai_viet': bai_viet, 'binh_luans': binh_luans})

def dang_ky(request):
  if request.POST:
    form = UserCreationForm(request.POST)
    if form.is_valid():
      auth.login(request, form.save())
      return redirect('trang-chu')
    else:
      messages.error(request, 'Người dùng đã tồn tại hoặc mật khẩu không khớp')
  return render(request, 'dang-ky.html')

def dang_nhap(request):
  if request.POST:
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      auth.login(request, form.get_user())
      return redirect('trang-chu')
    else:
      messages.error(request, 'Tài khoản hoặc mật khẩu không đúng')
  return render(request, 'dang-nhap.html')

def dang_xuat(request):
  if request.user.is_authenticated:
    auth.logout(request)
    return redirect('trang-chu')
  else:
    return redirect('dang-nhap')
  
def tai_khoan(request):
  if request.user.is_authenticated:
    return render(request, 'tai-khoan.html')
  else:
    return redirect('dang-nhap')
  
def sua_thong_tin(request):
  if request.user.is_authenticated:
    user_form = BieuMauNguoiDung(request.POST or None, instance=request.user)
    hoso_form = BieuMauHoSo(request.POST or None, instance=request.user.hoso)
    if request.POST:
      if user_form.is_valid() and hoso_form.is_valid():
        user_form.save()
        hoso_form.save()
        messages.success(request, 'Cập nhật thông tin thành công')
        return redirect('tai-khoan')
    return render(request, 'sua-thong-tin.html', {'hoso_form': hoso_form, 'user_form': user_form})
  else:
    return redirect('dang-nhap')
  
def yeu_thich(request):
  if request.user.is_authenticated:
    list_yeu_thich = request.user.hoso.yeu_thich
    bai_viets = BaiViet.objects.filter(Q(khung_gio_hien=None, khung_gio_an=None) | Q(khung_gio_hien__lte=datetime.now().time(), khung_gio_an__gte=datetime.now().time()), 
                                       id__in=list_yeu_thich, trang_thai='Đã đăng')
    return render(request, 'yeu-thich.html', {'bai_viets': bai_viets})
  else:
    return redirect('dang-nhap')