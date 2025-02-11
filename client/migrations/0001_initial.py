# Generated by Django 5.1 on 2024-11-23 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DanhMuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BaiViet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('noi_dung', models.TextField()),
                ('hinh_anh', models.ImageField(upload_to='')),
                ('trang_thai', models.CharField(choices=[('Chờ đăng', 'Chờ đăng'), ('Đã đăng', 'Đã đăng')], default='Chờ đăng', max_length=30)),
                ('ngay_tao', models.DateField(auto_now_add=True)),
                ('thoi_gian_dang', models.DateTimeField(blank=True, null=True)),
                ('khung_gio_hien', models.TimeField(blank=True, null=True)),
                ('khung_gio_an', models.TimeField(blank=True, null=True)),
                ('nguoi_tao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bai_viet', to=settings.AUTH_USER_MODEL)),
                ('danh_muc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.danhmuc')),
            ],
        ),
        migrations.CreateModel(
            name='DanhGia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_sao', models.IntegerField()),
                ('noi_dung', models.TextField()),
                ('thoi_gian', models.DateTimeField(auto_now_add=True)),
                ('da_duyet', models.BooleanField(default=False)),
                ('bai_viet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='duoc_binh_luan', to='client.baiviet')),
                ('nguoi_dung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='da_binh_luan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HoSo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vai_tro', models.CharField(blank=True, choices=[('Biên tập viên', 'Biên tập viên'), ('Tổng biên tập', 'Tổng biên tập')], max_length=30, null=True)),
                ('gioi_tinh', models.CharField(choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Ẩn', 'Ẩn')], default='Ẩn', max_length=10)),
                ('ngay_sinh', models.DateField(blank=True, null=True)),
                ('dien_thoai', models.CharField(blank=True, max_length=11, null=True)),
                ('yeu_thich', models.JSONField(default=list)),
                ('nguoi_dung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
