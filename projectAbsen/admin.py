from django.contrib import admin
from projectAbsen.models import Siswa,Kelas,Jurusan,Transaksi

# Register your models here.
class AbsenAdmin(admin.ModelAdmin):
    list_display = ['NISN','Nama']

admin.site.register(Siswa, AbsenAdmin)
admin.site.register(Kelas)
admin.site.register(Jurusan)
admin.site.register(Transaksi)