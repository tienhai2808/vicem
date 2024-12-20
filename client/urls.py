from django.urls import path
from .views import *

urlpatterns = [
    path('', trang_chu, name='trang-chu'),
    path('tai-khoan/', tai_khoan, name='tai-khoan'),
    path('tai-khoan/dang-ky/', dang_ky, name='dang-ky'),
    path('tai-khoan/dang-nhap/', dang_nhap, name='dang-nhap'),
    path('tai-khoan/dang-xuat/', dang_xuat, name='dang-xuat'),
    path('tai-khoan/sua-thong-tin/', sua_thong_tin , name='sua-thong-tin'),
    path('tai-khoan/yeu-thich/', yeu_thich , name='yeu-thich'),
    path('tim-kiem/', tim_kiem, name='tim-kiem'),
    path('bai-viet/<slug:slug_bai_viet>/', bai_viet_chi_tiet, name='bai-viet-chi-tiet'),
    path('<slug:slug_danh_muc>/', danh_muc_bai_viet, name='danh-muc-bai-viet')
]