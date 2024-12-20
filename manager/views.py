from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from django.utils import timezone
from client.models import *

# Create your views here.
def quan_ly(request):
  if request.user.is_authenticated and request.user.hoso.vai_tro:
    return render(request, 'quan-ly.html')
  else:
    return redirect('trang-chu')

def tao_bai_viet(request):
  if request.user.is_authenticated and request.user.hoso.vai_tro:
    form = BieuMauBaiViet(request.POST or None, request.FILES or None)
    if request.POST:
      if form.is_valid():
        bai_viet = form.save(False)
        bai_viet.nguoi_tao = request.user
        bai_viet.save()
        messages.success(request, 'Tạo bài viết thành công')
        return redirect('quan-ly')
    return render(request, 'tao-bai-viet.html', {'form': form})
  else:
    return redirect('trang-chu')
  
def bai_viet_cua_toi(request):
  if request.user.is_authenticated and request.user.hoso.vai_tro:
    bai_viets = BaiViet.objects.filter(nguoi_tao=request.user)
    return render(request, 'bai-viet-cua-toi.html', {'bai_viets': bai_viets})
  else:
    return redirect('trang-chu')
  
def bai_viet(request, slug_bai_viet):
  bai_viet = get_object_or_404(BaiViet, slug=slug_bai_viet, trang_thai='Chờ đăng')
  if request.user.is_authenticated and (request.user == bai_viet.nguoi_tao or request.user.hoso.vai_tro == 'Tổng biên tập'):
    form = BieuMauBaiViet(request.POST or None, request.FILES or None, instance=bai_viet)
    if request.POST:
      if form.is_valid():
        bai_viet_update = form.save()
        messages.success(request, 'Đã cập nhật những thay đổi')
        return redirect('bai-viet', bai_viet_update.slug)
    return render(request, 'bai-viet.html', {'bai_viet': bai_viet, 'form': form})
  
def tat_ca_danh_muc(request):
  if request.user.is_authenticated and request.user.hoso.vai_tro == 'Tổng biên tập':
    danh_mucs = DanhMuc.objects.all()
    form = BieuMauDanhMuc(request.POST or None)
    if request.POST:
      id_delete = request.POST.get('id_delete', '')
      if id_delete:
        DanhMuc.objects.get(id=id_delete).delete()
        messages.success(request, 'Xóa danh mục thành công')
        return redirect('tat-ca-danh-muc')
      if form.is_valid():
        form.save()
        messages.success(request, 'Thêm danh mục thành công')
        return redirect('tat-ca-danh-muc')
    return render(request, 'tat-ca-danh-muc.html', {'danh_mucs': danh_mucs, 'form': form})
  else:
    return redirect('trang-chu')
  
def danh_muc(request, id_danh_muc):
  if request.user.is_authenticated and request.user.hoso.vai_tro == 'Tổng biên tập':
    danh_muc = get_object_or_404(DanhMuc, id=id_danh_muc)
    form = BieuMauDanhMuc(request.POST or None, instance=danh_muc)
    if request.POST:
      if form.is_valid():
        form.save()
        messages.success(request, 'Đã cập nhật những thay đổi')
        return redirect('tat-ca-danh-muc')
    return render(request, 'danh-muc.html', {'form': form, 'danh_muc': danh_muc})
  else:
    return redirect('trang-chu')
  
def bai_viet_cho_dang(request):
  if request.user.is_authenticated and request.user.hoso.vai_tro == 'Tổng biên tập':
    bai_viets = BaiViet.objects.filter(trang_thai='Chờ đăng')
    if request.POST:
      action = request.POST.get('action')
      id_post = request.POST.get('id_post')
      start_time = request.POST.get('start_time', '')
      end_time = request.POST.get('end_time', '')
      if action == 'delete':
        BaiViet.objects.get(id=id_post).delete()
        messages.success(request, 'Xóa bài viết thành công')
      if action == 'post':
        bai_viet = BaiViet.objects.get(id=id_post)
        if start_time and end_time:
          bai_viet.khung_gio_hien = start_time
          bai_viet.khung_gio_an = end_time
        bai_viet.trang_thai = 'Đã đăng'
        bai_viet.thoi_gian_dang = timezone.now()
        bai_viet.save()
        messages.success(request, 'Đăng bài viết thành công')
      return redirect('bai-viet-cho-dang')
    return render(request, 'bai-viet-cho-dang.html', {'bai_viets': bai_viets})
  else:
    return redirect('trang-chu')
  
def bai_viet_da_dang(request):
  if request.user.is_authenticated and request.user.hoso.vai_tro == 'Tổng biên tập':
    bai_viets = BaiViet.objects.filter(trang_thai='Đã đăng')
    if request.POST:
      action = request.POST.get('action')
      id_post = request.POST.get('id_post')
      if action == 'delete':
        BaiViet.objects.get(id=id_post).delete()
        messages.success(request, 'Xóa bài viết thành công')
      if action == 'remove':
        bai_viet = BaiViet.objects.get(id=id_post)
        bai_viet.khung_gio_hien = None
        bai_viet.khung_gio_an = None
        bai_viet.trang_thai = 'Chờ đăng'
        bai_viet.thoi_gian_dang = None
        bai_viet.save()
        messages.success(request, 'Gỡ bài viết thành công')
      return redirect('bai-viet-da-dang')
    return render(request, 'bai-viet-da-dang.html', {'bai_viets': bai_viets})
  else:
    return redirect('trang-chu')
  
def duyet_binh_luan(request):
  if request.user.is_authenticated and request.user.hoso.vai_tro == 'Tổng biên tập':
    binh_luans = DanhGia.objects.filter(da_duyet=False)
    if request.POST:
      action = request.POST.get('action')
      id_cmt = request.POST.get('id_cmt')
      if action == 'delete':
        DanhGia.objects.get(id=id_cmt).delete()
        messages.success(request, 'Xóa bình luận thành công')
      if action == 'confirm':
        cmt = DanhGia.objects.get(id=id_cmt)
        cmt.da_duyet = True
        cmt.save()
        messages.success(request, 'Duyệt bình luận thành công')
      return redirect('duyet-binh-luan')
    return render(request, 'duyet-binh-luan.html', {'binh_luans': binh_luans})
  else:
    return redirect('trang-chu')