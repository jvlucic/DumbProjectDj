'''
Created on 01/03/2011

@author: Jorge
'''
from django.contrib import admin
from models import Pedido, Cliente, Usuario, ItemPedido, Producto, Unidad, Visita,Cobranza,CuentaPorCobrar, Deposito

from django.http import HttpRequest
from django.contrib.admin.models import LogEntry
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import forms
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.models import ModelChoiceField
from django.core.urlresolvers import reverse
import datetime
from django.contrib.admin.templatetags.admin_list import date_hierarchy
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
import time
from dbadmin.models import Grupo, Motivo, VisitaReschedule, VisitaClose


admin.site.unregister(Group)
admin.site.unregister(Site)
#admin.site.unregister(User)

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('format_action_time','user', 'content_type', 'object_id','object_repr','tipo_accion')
    dateformat='%d %b %Y %H:%M'
    def format_action_time(self, obj):
        return obj.action_time.strftime(self.dateformat)
    format_action_time.short_description = _('Fecha Accion')
    format_action_time.admin_order_field = 'action_time'
    def tipo_accion(self, obj):
        if (obj.action_flag==1):
            return _('Creacion')
        elif (obj.action_flag==2):
            return _('Modificacion')
        elif (obj.action_flag==3):
            return _('Eliminacion')
        
    tipo_accion.short_description = _('Tipo de Accion')
    tipo_accion.admin_order_field = 'action_flag'
    list_filter = ['user','action_flag']

admin.site.register(LogEntry,LogEntryAdmin)

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra= 0
    fields=['id_producto','cantidad',
             'monto_total','monto_impuesto','flete','descuento','precio_unidad',
             'porcentaje_impuesto','descuento_negativo'
             ]
    readonly_fields =['id_producto','cantidad',
             'monto_total','monto_impuesto','flete','descuento','precio_unidad',
             'porcentaje_impuesto','descuento_negativo'
             ]
    verbose_name='Productos Asociados'

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('format_fecha','format_fecha_entrega','format_cliente','total','format_vendedor','tiene_comentario')
    #TODO: FIX DATE HIERARCHY
    date_hierarchy = 'fecha'
    dateformat='%d %b %Y '
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')
    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()
        
    def format_vendedor(self, obj):
        return obj.field_owner_id.nombre+" "+obj.field_owner_id.apellido
    format_vendedor.short_description = 'Vendedor'
    format_vendedor.admin_order_field = 'vendedor'

    def format_cliente(self, obj):
        return obj.id_cliente.pc_nombre
    format_cliente.short_description = 'Cliente'
    format_cliente.admin_order_field = 'cliente'

    def format_fecha(self, obj):
        if (obj.fecha):
            return obj.fecha.strftime(self.dateformat)
        else:
            return ''
    format_fecha.short_description = 'Fecha'
    format_fecha.admin_order_field = 'fecha'

    def format_fecha_entrega(self, obj):
        if (obj.fecha):
            return obj.fecha_entrega.strftime(self.dateformat)
        else:
            return ''        
    format_fecha_entrega.short_description = 'Fecha Entrega'
    format_fecha_entrega.admin_order_field = 'fecha_entrega'
    
    search_fields = ['id_cliente__pc_nombre']
    fieldsets = [
        ('Encabezado',{'fields': ['fecha','id_cliente','fecha_entrega']}),
        ('Datos Adicionales', {'fields': ['total'],
                               'classes': ['collapse']
                               }),
    ]
    inlines = [
        ItemPedidoInline,
    ]

    readonly_fields =['fecha', 'fecha_entrega','id_cliente','field_owner_id','total']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def changelist_view(self, request,  extra_context=None):
        newrequest3=request
        newrequest3.GET._mutable=True
        print 'Original'
        print newrequest3.GET

        tobedel=[]
        for k in newrequest3.GET.iterkeys():
            if (newrequest3.GET.getlist(k)[0]==u''):
                tobedel.append(k)
            else:
                if (k.find('__id__')!=-1):
                    newrequest3.GET.__setitem__(k,newrequest3.GET.get(k))                    
                elif (k.find('total')!=-1):
                    newrequest3.GET.__setitem__(k,newrequest3.GET.get(k))                                      
                else:
                    newrequest3.GET.__setitem__(k,newrequest3.GET.getlist(k)[0])      
        for k in tobedel:
            del newrequest3.GET[k]
        
        print 'FINAL'
        print newrequest3.GET
        newrequest3.GET._mutable=False
        return super(PedidoAdmin, self).changelist_view(request)


admin.site.register(Pedido,PedidoAdmin)    

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('pc_nombre','pc_telefono','identificacion')
    search_fields = ['pc_nombre']
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')
    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()
    
admin.site.register(Cliente,ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('itemno','nombre','precio','cantidad')
    search_fields = ['nombre']
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')
    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()
            
admin.site.register(Producto,ProductoAdmin)

class VisitaAdminForm(forms.ModelForm):
    id_motivo_visita=forms.ModelChoiceField(queryset=Motivo.objects.filter(tipo=1),required=False,label='Motivo Visita')
    id_motivo_no_visita=forms.ModelChoiceField(queryset=Motivo.objects.filter(tipo=2),required=False, label='Motivo No Visita')
    id_motivo_no_cobranza=forms.ModelChoiceField(queryset=Motivo.objects.filter(tipo=3),required=False, label='Motivo No Cobranza')
    id_motivo_no_pedido=forms.ModelChoiceField(queryset=Motivo.objects.filter(tipo=4),required=False, label='Motivo No Pedido')
    class Meta:
        model = Visita


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','username','correo')
    search_fields = ['nombre','username','correo','apellido']
    exclude = ('field_timestamp_c','field_timestamp_m','field_deleted')
    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()

admin.site.register(Usuario,UsuarioAdmin)

class CuentaPorCobrarAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','procesada','esta_vencida','fecha_vencimiento')
    search_fields = ['id_cliente__pc_nombre']
    list_filter = ['id_cliente__pc_nombre','fecha_vencimiento','cancelada','procesada']
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')
    readonly_fields =['numero_documento', 'monto_original','saldo_actual','fecha_documento','fecha_despacho','fecha_vencimiento','fecha_entrega','procesada','cancelada','id_cliente','id_cobranza']
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    
    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()
    
admin.site.register(CuentaPorCobrar,CuentaPorCobrarAdmin)

class DepositoAdmin(admin.ModelAdmin):
    list_display = ('numero','id_banco','monto','fecha')
    search_fields = ['numero']
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id','latitud','longitud')
    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()
    
admin.site.register(Deposito,DepositoAdmin)



class VisitaCreateAdmin(admin.ModelAdmin):
    list_display = ['id_cliente','format_fecha','visitado','comentario']    
    dateformat='%d %b %Y %H:%M'
    date_hierarchy='fecha'
    list_filter = ['fecha','visitado']
    search_fields = ['id_cliente']    
    fields=('fecha','id_cliente','comentario')
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id','hora_inicio','hora_fin')
    form=VisitaAdminForm
    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()

    def format_fecha(self, obj):
        return obj.fecha.strftime(self.dateformat)
    format_fecha.short_description = _('Fecha')
    
admin.site.register(Visita,VisitaCreateAdmin)


        
        
class VisitaRescheduleAdmin(admin.ModelAdmin):
    list_display = ['id_cliente','visitado','comentario']    
    dateformat='%d %b %Y %H:%M'
    date_hierarchy='fecha'
    list_filter = ['fecha','visitado']
    search_fields = ['id_cliente']    
    fields=('fecha_reagenda',)
    form=VisitaAdminForm

    def has_add_permission(self, request):
        return False    
    
    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()

    
admin.site.register(VisitaReschedule,VisitaRescheduleAdmin)


        
        
class VisitaCloseAdmin(admin.ModelAdmin):
    list_display = ['id_cliente','visitado','comentario']    
    dateformat='%d %b %Y %H:%M'
    date_hierarchy='fecha'
    list_filter = ['fecha','visitado']
    search_fields = ['id_cliente']    
    fields=('id_motivo_no_visita','id_motivo_no_cobranza','id_motivo_no_pedido','comentario','visitado')
    form=VisitaAdminForm
    
    def has_add_permission(self, request):
        return False    

    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()

    
admin.site.register(VisitaClose,VisitaCloseAdmin)