from django.contrib import admin
from .models import Cargo, DetalleVale, Perfil, Servicio, Sucursal, Turno, Vale, Venta

# Register your models here.
admin.site.register(Cargo)
admin.site.register(DetalleVale)
admin.site.register(Perfil)
admin.site.register(Servicio)
admin.site.register(Sucursal)
admin.site.register(Turno)
admin.site.register(Vale)
admin.site.register(Venta)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]
    list_per_page = 10
