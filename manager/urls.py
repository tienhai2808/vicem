from django.urls import path
from .views import *

urlpatterns = [
    path('', quan_ly, name='quan-ly'),
    path('tao-bai-viet/', tao_bai_viet, name='tao-bai-viet'),
    path('bai-viet-cua-toi/', bai_viet_cua_toi, name='bai-viet-cua-toi'),
    path('tat-ca-danh-muc/', tat_ca_danh_muc, name='tat-ca-danh-muc'),
    path('danh-muc/<int:id_danh_muc>/', danh_muc, name='danh-muc'),
    path('bai-viet-cho-dang/', bai_viet_cho_dang, name='bai-viet-cho-dang'),
    path('bai-viet-da-dang/', bai_viet_da_dang, name='bai-viet-da-dang'),
    path('duyet-binh-luan/', duyet_binh_luan, name='duyet-binh-luan'),
    path('<slug:slug_bai_viet>/', bai_viet, name='bai-viet'),
]