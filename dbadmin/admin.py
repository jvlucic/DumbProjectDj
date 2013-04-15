'''
Created on 01/03/2011

@author: Jorge
'''
from django.contrib import admin, messages
from models import Pedido, Cliente, Usuario, ItemPedido, Producto, Unidad, Visita,Cobranza,CuentaPorCobrar, Deposito

from django.http import HttpRequest
from django.contrib.admin.models import LogEntry
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import forms, helpers
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.models import ModelChoiceField, BaseInlineFormSet
from django.core.urlresolvers import reverse
import datetime
from django.contrib.admin.templatetags.admin_list import date_hierarchy
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
import time
from dbadmin.models import Grupo, Motivo, VisitaReschedule, VisitaClose,\
    DetalleProducto, Categoria
from dbadmin.filters import ProductTreeListFilter, DateRangeFilter
from django.db import models, router
from django.db.models.signals import post_save
from django.contrib.comments.signals import comment_was_posted
import re
import locale
from django.forms.widgets import Widget
from django.contrib.localflavor import no
from dbadmin.options import VentasPlusModelAdmin
from django.utils.encoding import force_text
from django.template.response import TemplateResponse
from django.contrib.admin.util import model_ngettext, get_deleted_objects
from django.core.exceptions import PermissionDenied
from django.contrib.admin.filters import RelatedFieldListFilter,\
    AllValuesFieldListFilter
from django.contrib.admin.views.main import ChangeList


admin.site.unregister(Group)
admin.site.unregister(Site)
#admin.site.unregister(User)
    

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('format_action_time','user', 'content_type', 'object_id','object_repr','tipo_accion')
    dateformat='%d/%m/%Y '
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

class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form

class RequireOneFormSet(BaseInlineFormSet):
    """Require at least one form in the formset to be completed."""
    def clean(self):
        """Check that at least one form has been completed."""
        super(RequireOneFormSet, self).clean()
        for error in self.errors:
            if error:
                return
        completed = 0
        if self.form.base_fields:
            for cleaned_data in self.cleaned_data:
                # form has data and we aren't deleting it.
                if (not('cantidad' in cleaned_data) or ((cleaned_data['cantidad'] is None) or (not isinstance( cleaned_data['cantidad'], ( int, long ) )))):
                    raise forms.ValidationError("Debe agregar al menos un producto")
                
                if cleaned_data and not cleaned_data.get('DELETE', False):
                    completed += 1
    
            if completed < 1:
                raise forms.ValidationError("Al menos un Producto es requerido.")

class ItemPedidoInlinenForm(forms.ModelForm):
    cantidad= forms.IntegerField(required=True ,min_value=1,initial=22)
    class Meta:
        model = Deposito

class ItemPedidoInline(admin.StackedInline):
    model = ItemPedido
    extra= 1
    formset = RequireOneFormSet
    classes = ('collapse open',)
    inline_classes = ('collapse open',)
    readonly_fields =['id_producto','cantidad',
             'monto_total','monto_impuesto','flete','descuento','precio_unidad',
             'porcentaje_impuesto','descuento_negativo'
             ]
    verbose_name='Producto Asociado'
    verbose_name_plural='Productos Asociados'
    fieldsets = (
        (None, {
            'fields': ( 'id_producto','cantidad','precio_unidad','descuento','descuento_negativo','flete', 'porcentaje_impuesto', 'monto_impuesto','monto_total')
        }),
            
    )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['monto_total']
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
            
class PedidoAdmin(VentasPlusModelAdmin):
    list_display = ('format_fecha','format_fecha_entrega','format_cliente','total','format_vendedor','tiene_comentario')
    #TODO: FIX DATE HIERARCHY
    date_hierarchy = 'fecha'
    dateformat='%d/%m/%Y '
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')
    list_filter=[('fecha', DateRangeFilter)]
    fields=['fecha','id_cliente','fecha_entrega','id_metodo_pago','numero','comentario','total']
    
    add_continue_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
    add_another_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
    add_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
    
    change_continue_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_saveasnew_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_another_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    
    class Media:
        js = ("js/grappelli_custom_datepicker_template_dom_init.js",)
        
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
        if (obj.fecha_entrega):
            return obj.fecha_entrega.strftime(self.dateformat)
        else:
            return ''        
    format_fecha_entrega.short_description = 'Fecha Entrega'
    format_fecha_entrega.admin_order_field = 'fecha_entrega'
    
    search_fields = ['id_cliente__pc_nombre']

    inlines = [
        ItemPedidoInline,
    ]

    readonly_fields =['fecha', 'fecha_entrega','id_cliente','field_owner_id','total','numero','comentario','id_metodo_pago']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['total']
        return self.readonly_fields

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return False
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

class ClienteAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteAdminForm, self).__init__(*args, **kwargs)
        self.fields['pc_fecha_nacimiento'] = forms.DateField(label="Fecha de nacimiento",widget=forms.DateInput(attrs={'size': 64L, 'class':'vDateField'}))
        self.fields['pc_fecha_nacimiento'].required = True
    class Meta:
        model = Cliente

class ClienteAdmin(VentasPlusModelAdmin):
    list_display = ('razon_social','pc_nombre','pc_telefono','identificacion')
    search_fields = ['pc_nombre']
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')

    add_continue_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
    add_another_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
    add_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
    
    change_continue_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_saveasnew_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_another_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    classes = ('collapse ',)
    form=ClienteAdminForm
    fieldsets = (
        (None, {
            'fields': ( 'codigo','razon_social','identificacion','telefono1','telefono2','fax', 'correo', 'comentario','tipo','flete','descuento_maestro','descuento_otro1','descuento_otro2','id_zona')
        }),
        ('Datos de la Persona de Contacto', {
            'classes': ('collapse',),
            'fields': ( 'pc_nombre','pc_telefono','pc_celular','pc_cargo', 'pc_correo_electronico', 'pc_fecha_nacimiento',)
        }),
            
    )
    
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

class DetalleProductoInlineForm(forms.ModelForm):
    id_level=forms.ModelChoiceField(queryset=Categoria.objects.filter(id_level=1),required=True,label='Categoria')
    level=forms.HiddenInput()
    class Meta:
        model = DetalleProducto


class DetalleProductoInline(admin.TabularInline):
    model = DetalleProducto
    extra= 6
    fields=['id_level','level']
#   readonly_fields =['id_level','level','descripcion_level','id_letter']
    verbose_name='Detalle Producto'
    verbose_name_plural='Detalle Producto'

#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == "id_level":
#            kwargs["queryset"] = Categoria.objects.filter(id_level=1)
#        return super(DetalleProductoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
 
    
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class ProductoCustomForm (forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.filter(level=1),required=True,label=u'Categor\xEDa')
    tipo = forms.ModelChoiceField(queryset=Categoria.objects.filter(level=2),required=True,label='Tipo')
    linea = forms.ModelChoiceField(queryset=Categoria.objects.filter(level=3),required=True,label=u'L\xEDnea')
    calidad = forms.ModelChoiceField(queryset=Categoria.objects.filter(level=4),required=True,label='Calidad')
    tamano = forms.ModelChoiceField(queryset=Categoria.objects.filter(level=5),required=True,label=u'Tama\xF1o')
    color = forms.ModelChoiceField(queryset=Categoria.objects.filter(level=6),required=True,label='Color')

    def __init__(self, *args, **kwargs):
        super(ProductoCustomForm, self).__init__(*args, **kwargs)
        if self.instance:
            for detalleProducto in  self.instance.detalleproducto_set.all():
                level={1: 'categoria',2: 'tipo',3: 'linea',4: 'calidad',5: 'tamano',6: 'color',}.get(detalleProducto.level, None)
                self.fields[level]=forms.ModelChoiceField(queryset=Categoria.objects.filter(level=detalleProducto.level),required=True,label=level.capitalize(),initial=Categoria.objects.filter(level=detalleProducto.level,id_level=detalleProducto.id_level))
    class Meta:
        model = Producto

                        
            
class ProductoAdmin(VentasPlusModelAdmin):
    list_display = ('id_surrogate','itemno','categoria','tipo','linea','calidad','tamano','color','nombre','precio','cantidad')
    search_fields = ['nombre']
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')
    list_filter=[ProductTreeListFilter ,ProductTreeListFilter,ProductTreeListFilter,ProductTreeListFilter,ProductTreeListFilter,ProductTreeListFilter]

    form=ProductoCustomForm
    
    filterConfigData =  [
                          {'title':_(u'Categor\xEDa'), 'parameter_name':'categoria', 'level':1},
                          {'title':_(u'Tipo'), 'parameter_name':'tipo', 'level':2},
                          {'title':_(u'L\xEDnea'), 'parameter_name':'linea', 'level':3},
                          {'title':_(u'Calidad'), 'parameter_name':'calidad', 'level':4},
                          {'title':_(u'Tama\xF1o'), 'parameter_name':'tamano', 'level':5},
                          {'title':_(u'Color'), 'parameter_name':'color', 'level':6},                          
                        ]    
    add_continue_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    add_another_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    add_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    
    change_continue_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_saveasnew_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_another_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
    change_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
        
    def get_form(self, request, obj=None, **kwargs):
        
        return super(ProductoAdmin, self).get_form(request, obj=None, **kwargs)
    
    def categoria(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=1).descripcion_level 
    categoria.short_description = 'Categor\xEDa'
    
    def tipo(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=2).descripcion_level 
    tipo.short_description = 'Tipo'
    
    def linea(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=3).descripcion_level 
    linea.short_description = 'LxEDnea'
    
    def calidad(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=4).descripcion_level 
    calidad.short_description = 'Calidad'
    
    def tamano(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=5).descripcion_level 
    tamano.short_description = u'Tama\xF1o'

    def color(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=6).descripcion_level 
    color.short_description = 'Color'

        
    def save_model(self, request, obj, form, change):

        
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()
        self.change_msg_dict={'name': force_text(obj._meta.verbose_name),'obj':force_text(obj.id_surrogate)}
        self.msg_dict={'name': force_text(obj._meta.verbose_name),'obj':force_text(obj.id_surrogate)}        
        producto=obj
        categoria_list=[form.cleaned_data['categoria'],
                        form.cleaned_data['tipo'],
                        form.cleaned_data['linea'],
                        form.cleaned_data['calidad'],
                        form.cleaned_data['tamano'],
                        form.cleaned_data['color']
                        ]
        i=0
        relatedDp=obj.detalleproducto_set.all()
        if (relatedDp):
            for detalleProducto in  relatedDp:
                level={1: 'categoria',2: 'tipo',3: 'linea',4: 'calidad',5: 'tamano',6: 'color',}.get(detalleProducto.level, None)
                detalleProducto.id_level=form.cleaned_data[level].id_level
                detalleProducto.level=form.cleaned_data[level].level
                detalleProducto.descripcion_level=form.cleaned_data[level].nombre
                detalleProducto.save()
        else:
            for categoria in categoria_list:
                detalleProducto=DetalleProducto(id_level=categoria.id_level,
                                                level=categoria.level, 
                                                descripcion_level=categoria.nombre,
                                                id_producto=producto
                                                )
                detalleProducto.field_owner_id = Usuario.objects.get(pk=producto.field_owner_id) 
                detalleProducto.field_inst_id=0
                detalleProducto.field_permissions=0
                detalleProducto.field_timestamp_c=int(time.time()+i)
                detalleProducto.field_timestamp_m=datetime.datetime.now()
                #TODO: DONT HARDCODE GROUP
                detalleProducto.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
                detalleProducto.save()        
                i+=1

admin.site.register(Producto,ProductoAdmin)




class UsuarioAdmin(VentasPlusModelAdmin):
    list_display = ('username','nombre','apellido','correo')
    search_fields = ['nombre','username','correo','apellido']
    exclude = ('field_timestamp_c','field_timestamp_m','field_deleted')
    add_continue_message=u'El %(name)s %(code)s-%(obj)s fue agregado satisfactoriamente'
    add_another_message=u'El %(name)s %(code)s-%(obj)s fue agregado satisfactoriamente'
    add_message=u'El %(name)s %(code)s-%(obj)s fue agregado satisfactoriamente'
    
    change_continue_message=u'El %(name)s %(code)s-%(obj)s fue modificado satisfactoriamente'
    change_saveasnew_message=u'El %(name)s %(code)s-%(obj)s fue modificado satisfactoriamente'
    change_another_message=u'El %(name)s %(code)s-%(obj)s fue modificado satisfactoriamente'
    change_message=u'El %(name)s %(code)s-%(obj)s fue modificado satisfactoriamente'    
    
    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ('field_timestamp_c','field_timestamp_m','field_deleted','adminuser')
        form = super(UsuarioAdmin, self).get_form(request, obj, **kwargs)
        return form
    
    def save_model(self, request, obj, form, change):
        self.change_msg_dict={'name': force_text(obj._meta.verbose_name),'code':force_text(obj.codigo),'obj':force_text(obj)}
        self.msg_dict={'name': force_text(obj._meta.verbose_name),'code':force_text(obj.codigo),'obj':force_text(obj)}
        
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()

admin.site.register(Usuario,UsuarioAdmin)

class CuentaPorCobrarAdminForm(VentasPlusModelAdmin):
    numero = forms.CharField(required=True,label=u'N\xFAmero')        


class ClienteListFilter(AllValuesFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super(ClienteListFilter, self).__init__( field, request, params, model, model_admin, field_path)
        self.title="Cliente"
    
class CuentaPorCobrarAdmin(VentasPlusModelAdmin):
    dateformat='%d/%m/%Y '
    list_display = ('numero_documento','id_cliente','procesada','esta_vencida','format_fecha_vencimiento','cancelada')
    search_fields = ['id_cliente__pc_nombre']
    list_filter = [("id_cliente__razon_social",ClienteListFilter),'procesada','fecha_vencimiento','cancelada']
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')
    readonly_fields =['numero_documento', 'monto_original','saldo_actual','fecha_documento','fecha_despacho','fecha_vencimiento','fecha_entrega','procesada','cancelada','id_cliente','id_cobranza']
    
    
    add_continue_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    add_another_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    add_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    
    change_continue_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_saveasnew_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_another_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'

    
    def format_fecha_vencimiento(self, obj):
        if (obj.fecha_vencimiento):
            return obj.fecha_vencimiento.strftime(self.dateformat)
    format_fecha_vencimiento.short_description = _('Fecha Vencimiento')
    format_fecha_vencimiento.admin_order_field = 'fecha_vencimiento'    
    
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
        self.msg_dict={'name': force_text(obj._meta.verbose_name),'idC':force_text(obj.numero_documento),'obj':force_text(obj.id_cliente)}
        self.change_msg_dict={'name': force_text(obj._meta.verbose_name),'idC':force_text(obj.numero_documento),'obj':force_text(obj.id_cliente)}
        
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.field_inst_id=0
        obj.field_permissions=0
        obj.field_timestamp_c=int(time.time())
        obj.field_timestamp_m=datetime.datetime.now()
        #TODO: DONT HARDCODE GROUP
        obj.field_group_id= Grupo.objects.get(pk='TESTGROUP') 
        obj.save()
    
admin.site.register(CuentaPorCobrar,CuentaPorCobrarAdmin)

class DepositoAdminForm(forms.ModelForm):
    numero= forms.CharField(max_length=64L, label=u'N\xFAmero')
    monto = forms.FloatField(required=True)
    cuenta = forms.CharField(max_length=64L, required=True, widget=forms.TextInput(attrs={'size': 64L, 'class':'vTextField'}))
    def __init__(self, *args, **kwargs):
        super(DepositoAdminForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].required = True
    class Meta:
        model = Deposito

class DepositoAdmin(VentasPlusModelAdmin):
    list_display = ('numero','id_banco','format_monto','fecha')
    search_fields = ['numero']
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id','latitud','longitud')
    form=DepositoAdminForm
    
    add_continue_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    add_another_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    add_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    
    change_continue_message=u'El %(name)s "%(obj)s" fue modificado satisfactoriamente'
    change_saveasnew_message=u'El %(name)s "%(obj)s" fue modificado satisfactoriamente'
    change_another_message=u'El %(name)s "%(obj)s" fue modificado satisfactoriamente'
    change_message=u'El %(name)s "%(obj)s" fue modificado satisfactoriamente'
    
    def format_monto(self, obj):
        return '{:,.2f}'.format(obj.monto).replace(".","%").replace(",",".").replace("%",",")+" Bs." 
    format_monto.short_description = 'Monto'
    format_monto.admin_order_field = 'monto'
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


class VisitaAdminForm(forms.ModelForm):
    id_motivo_visita=forms.ModelChoiceField(queryset=Motivo.objects.filter(tipo=1),required=False,label='Motivo Visita')
    id_motivo_no_visita=forms.ModelChoiceField(queryset=Motivo.objects.filter(tipo=2),required=False, label='Motivo No Visita')
    id_motivo_no_cobranza=forms.ModelChoiceField(queryset=Motivo.objects.filter(tipo=3),required=False, label='Motivo No Cobranza')
    id_motivo_no_pedido=forms.ModelChoiceField(queryset=Motivo.objects.filter(tipo=4),required=False, label='Motivo No Pedido')
    def __init__(self, *args, **kwargs):
        super(VisitaAdminForm, self).__init__(*args, **kwargs)
     
    class Meta:
        model = Visita
        
class VisitaCreateAdmin(VentasPlusModelAdmin):
    form=VisitaAdminForm
    list_display = ['id_cliente','format_fecha','visitado','comentario']    
    dateformat='%d/%m/%Y '
    list_filter=[('fecha', DateRangeFilter),'id_cliente']
    search_fields = ['id_cliente']    
    fields=('fecha','id_cliente','comentario','id_motivo_visita')
    exclude = ('field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id','hora_inicio','hora_fin')
    add_continue_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    add_another_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    add_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    
    change_continue_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_saveasnew_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_another_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    class Media:
        js = ("js/grappelli_custom_datepicker_template.js","js/grappelli_custom_datepicker_template_dom_init.js")
            
    def save_model(self, request, obj, form, change):
        self.msg_dict={'name': force_text(obj._meta.verbose_name),'idC':force_text(obj.fecha.strftime(self.dateformat)),'obj':force_text(obj.id_cliente)}
        self.change_msg_dict={'name': force_text(obj._meta.verbose_name),'idC':force_text(obj.fecha.strftime(self.dateformat)),'obj':force_text(obj.id_cliente)}
        
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
    format_fecha.admin_order_field = 'fecha'

admin.site.register(Visita,VisitaCreateAdmin)


        
        
class VisitaRescheduleAdmin(VentasPlusModelAdmin):
    list_display = ['id_cliente','visitado','comentario','fecha']    
    dateformat='%d/%m/%Y '
    list_filter = ['fecha','visitado','id_cliente']
    search_fields = ['id_cliente']    
    fields=('fecha','fecha_reagenda')
    form=VisitaAdminForm
    readonly_fields=['fecha']
    class Media:
        js = ("js/grappelli_custom_datepicker_template.js",)
            
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


        
        
class VisitaCloseAdmin(VentasPlusModelAdmin):
    list_display = ['id_cliente','visitado','comentario']    
    dateformat='%d/%m/%Y '
    list_filter = ['fecha','visitado']
    search_fields = ['id_cliente']    
    fields=('id_motivo_no_visita','id_motivo_no_cobranza','id_motivo_no_pedido','visitado')
    form=VisitaAdminForm
    class Media:
        js = ("js/grappelli_custom_datepicker_template.js","js/closeVisita.js")    
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

