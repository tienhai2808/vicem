from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.
class HoSo(models.Model):
  nguoi_dung = models.OneToOneField(User, on_delete=models.CASCADE)
  vai_tro = models.CharField(max_length=30, choices=[('Biên tập viên', 'Biên tập viên'), ('Tổng biên tập', 'Tổng biên tập')], blank=True, null=True)
  gioi_tinh = models.CharField(max_length=10, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Ẩn', 'Ẩn')], default='Ẩn')
  ngay_sinh = models.DateField(blank=True, null=True)
  dien_thoai = models.CharField(max_length=11, blank=True, null=True)
  yeu_thich = models.JSONField(default=list, blank=True, null=True) 
  
  def __str__(self):
    return f'Hồ sơ {self.nguoi_dung.username}'
  
  def them_yeu_thich(self, bai_viet_id):
    if bai_viet_id not in self.yeu_thich:
      self.yeu_thich.append(bai_viet_id)
      self.save()
  
  def huy_yeu_thich(self, bai_viet_id):
    if bai_viet_id in self.yeu_thich:
      self.yeu_thich.remove(bai_viet_id)
      self.save()
      
def create_profile(sender, instance, created, **kwargs):
  if created:
    user_profile = HoSo(nguoi_dung=instance)
    user_profile.save()
post_save.connect(create_profile, sender=User)
  
  
class DanhMuc(models.Model):
  ten = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200)
  
  def __str__(self):
    return self.ten
  

class BaiViet(models.Model):
  nguoi_tao = models.ForeignKey(User, on_delete=models.PROTECT, related_name='bai_viet')
  tieu_de = models.CharField(max_length=500)
  slug = models.SlugField(max_length=500, blank=True, null=True)
  danh_muc = models.ForeignKey(DanhMuc, on_delete=models.PROTECT)
  hinh_anh = models.ImageField(upload_to='')
  noi_dung = models.TextField()
  trang_thai = models.CharField(max_length=30, choices=[('Chờ đăng', 'Chờ đăng'), ('Đã đăng', 'Đã đăng')], default='Chờ đăng')
  ngay_tao = models.DateField(auto_now_add=True)
  thoi_gian_dang = models.DateTimeField(blank=True, null=True)
  khung_gio_hien = models.TimeField(blank=True, null=True)
  khung_gio_an = models.TimeField(blank=True, null=True)
  
  def __str__(self):
    return self.tieu_de
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.tieu_de)
    super(BaiViet, self).save(*args, **kwargs)
  

class DanhGia(models.Model):
  nguoi_dung = models.ForeignKey(User, on_delete=models.CASCADE, related_name='da_binh_luan')
  bai_viet = models.ForeignKey(BaiViet, on_delete=models.CASCADE, related_name='duoc_binh_luan')
  so_sao = models.IntegerField()
  noi_dung = models.TextField()
  thoi_gian = models.DateTimeField(auto_now_add=True)
  da_duyet = models.BooleanField(default=False)
  
  def __str__(self):
    return f'{self.nguoi_dung.username} đánh giá bài viết {self.bai_viet.pk}'