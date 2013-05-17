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
from django.forms.models import ModelChoiceField, BaseInlineFormSet,\
    modelformset_factory, inlineformset_factory
from django.core.urlresolvers import reverse
import datetime
from django.contrib.admin.templatetags.admin_list import date_hierarchy
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
import time
from dbadmin.models import Grupo, Motivo, VisitaReschedule, VisitaClose,\
    DetalleProducto, Categoria, Pago, Banco, MetodoPago, CobranzaCuentaPorCobrar
from dbadmin.filters import ProductTreeListFilter, DateRangeFilter
from django.db import models, router
from django.db.models.signals import post_save
from django.contrib.comments.signals import comment_was_posted
import re
import locale
from django.forms.widgets import Widget
from django.contrib.localflavor import no
from dbadmin.options import VentasPlusModelAdmin, VisitaVentasPlusModelAdmin
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

# class BancoAdmin(VentasPlusModelAdmin):
#     add_continue_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
#     add_another_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
#     add_message=u'El %(name)s "%(obj)s" fue a\xF1adido satisfactoriamente'
#     change_continue_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
#     change_saveasnew_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
#     change_another_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
#     change_message='El %(name)s "%(obj)s" fue modificado satisfactoriamente.'
# 
# admin.site.register(Banco,BancoAdmin)
# 
# admin.site.register(MetodoPago)
# class UnidadAdmin(VentasPlusModelAdmin):
#     pass
# admin.site.register(Unidad,UnidadAdmin)

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
                
                cleaned_data['field_timestamp_c']=datetime.datetime.now()+datetime.timedelta(seconds=completed)
                cleaned_data['counter']=int(time.time()+completed)   
                               
                if cleaned_data and not cleaned_data.get('DELETE', False):
                    completed += 1
    
            if completed < 1:
                raise forms.ValidationError("Al menos un Producto es requerido.")

    def save_new(self, form, commit=True):
        form.instance.counter=form.cleaned_data['counter']
        form.instance.field_timestamp_c=form.cleaned_data['field_timestamp_c']
        return super(RequireOneFormSet, self).save_new(form, commit=commit)
    
class PagoRequireOneFormSet(BaseInlineFormSet):
    """Require at least one form in the formset to be completed."""
    def clean(self):
        """Check that at least one form has been completed."""
        super(PagoRequireOneFormSet, self).clean()
        for error in self.errors:
            if error:
                return
        completed = 0
        if self.form.base_fields:
            for cleaned_data in self.cleaned_data:
                cleaned_data['field_timestamp_c']=datetime.datetime.now()+datetime.timedelta(seconds=completed)
                cleaned_data['counter']=int(time.time()+completed)  
                if cleaned_data and not cleaned_data.get('DELETE', False):
                    completed += 1
    
            if completed < 1:
                raise forms.ValidationError("Al menos un Pago es requerido.")
            

    def save_new(self, form, commit=True):
        form.instance.counter=form.cleaned_data['counter']
        form.instance.field_timestamp_c=form.cleaned_data['field_timestamp_c']
        return super(PagoRequireOneFormSet, self).save_new(form, commit=commit)
    
class PagoInline(admin.StackedInline):
    model = Pago
    extra= 1
    formset = PagoRequireOneFormSet
    classes = ('collapse open',)
    inline_classes = ('collapse open',)
    verbose_name='Pago Asociado'
    verbose_name_plural='Pagos Asociados'
    fieldsets = (
        (None, {
            'fields': ( 'monto','saldo','id_banco','fecha_documento','numero_documento','titular','id_cobranza', 'id_deposito','id_metodo_pago')
        }),
            
    )

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.save()    

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
            'fields': ( 'id_producto','cantidad','id_unidad','precio_unidad','descuento','descuento_negativo','flete', 'porcentaje_impuesto', 'monto_impuesto','monto_total')
        }),
            
    )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:        
            return self.readonly_fields

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class PedidoAdmin(VentasPlusModelAdmin):
    list_display = ('format_fecha','format_fecha_entrega','format_cliente','total','format_vendedor','tiene_comentario')
    date_hierarchy = 'fecha'
    dateformat='%d/%m/%Y '
    
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

#    readonly_fields =['fecha', 'fecha_entrega','id_cliente','field_owner_id','total','numero','comentario','id_metodo_pago']

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
            'fields': ( 'codigo','razon_social','identificacion','telefono1','telefono2','fax', 'correo', 'comentario','tipo','flete','descuento_maestro','descuento_otro1','descuento_otro2')
        }),
        ('Datos de la Persona de Contacto', {
            'classes': ('collapse',),
            'fields': ( 'pc_nombre','pc_telefono','pc_celular','pc_cargo', 'pc_correo_electronico', 'pc_fecha_nacimiento',)
        }),
            
    )
        
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
    list_display = ('itemno','nombre','categoria','tipo','linea','calidad','tamano','color','precio','cantidad')
    search_fields = ['nombre']
    
    list_filter=[ProductTreeListFilter ,ProductTreeListFilter,ProductTreeListFilter,ProductTreeListFilter,ProductTreeListFilter,ProductTreeListFilter]
    fields=['itemno','nombre','precio','cantidad','categoria','tipo','linea','calidad','tamano','color']
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

    def get_readonly_fields(self, request, obj=None):
        readonly_fields=super(ProductoAdmin, self).get_readonly_fields(request)
        if request.user.is_superuser:
            return readonly_fields
        else:
            return list(readonly_fields)+['categoria','tipo','linea','calidad','tamano','color']
        
    def get_form(self, request, obj=None, **kwargs):
        return super(ProductoAdmin, self).get_form(request, obj=None, **kwargs)
    
    def categoria(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=1).descripcion_level 
    categoria.short_description = u'Categor\xEDa'
    
    def tipo(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=2).descripcion_level 
    tipo.short_description = 'Tipo'
    
    def linea(self, obj):
        return DetalleProducto.objects.filter(id_producto=obj).get(level=3).descripcion_level 
    linea.short_description = u'L\xEDnea'
    
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
                detalleProducto.field_timestamp_c=datetime.datetime.now()+datetime.timedelta(seconds=i)
                detalleProducto.counter=int(time.time()+i)
                detalleProducto.field_owner_id = Usuario.objects.get(pk=producto.field_owner_id) 
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
        obj.save()

admin.site.register(Usuario,UsuarioAdmin)



class ClienteListFilter(AllValuesFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super(ClienteListFilter, self).__init__( field, request, params, model, model_admin, field_path)
        self.title="Cliente"


class CobranzaCuentaPorCobrarAdminForm(forms.ModelForm):
    numero_recibo = forms.CharField(max_length=64L, label=u"N\xFAmero de recibo")
    impreso = forms.NullBooleanField(required=False)
    fecha_impreso = forms.DateField(required=False)
    fecha = forms.DateField(required=False)
    id_cobrador = forms.CharField(max_length=192L, label="Cobrador")
    id_cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(),required=True,label=u'Cliente')   
    monto = forms.FloatField()
    concepto = forms.CharField(max_length=64L)
    latitud = forms.FloatField(required=False)
    longitud = forms.FloatField(required=False)
    def __init__(self, *args, **kwargs):
        super(CobranzaCuentaPorCobrarAdminForm, self).__init__(*args, **kwargs)
        #cob=Cobranza.objects.get(pk=cinstance.id_cobranza)
        if self.instance.id_cobranza_id:
            cinstance=self.instance.id_cobranza
            self.fields['numero_recibo']=forms.CharField(max_length=64L, label=u"N\xFAmero de recibo",initial=cinstance.numero_recibo )
            self.fields['impreso'] = forms.NullBooleanField(required=False,initial=cinstance.impreso)
            self.fields['fecha_impreso'] = forms.DateField(required=False,initial=cinstance.fecha_impreso)
            self.fields['fecha'] = forms.DateField(required=False,initial=cinstance.fecha)
            self.fields['id_cobrador'] = forms.CharField(max_length=192L, label="Cobrador",initial=cinstance.id_cobrador)
            self.fields['id_cliente'] = forms.ModelChoiceField(queryset=Cliente.objects.all(),required=True,label=u'Cliente',initial=cinstance.numero_recibo)   
            self.fields['monto'] = forms.FloatField(initial=cinstance.monto)
            self.fields['concepto'] = forms.CharField(max_length=64L,initial=cinstance.concepto)
            self.fields['latitud'] = forms.FloatField(required=False,initial=cinstance.latitud)
            self.fields['longitud'] = forms.FloatField(required=False,initial=cinstance.longitud)

class CobranzaRequireOneFormSet(BaseInlineFormSet):
    """Require at least one form in the formset to be completed."""
    def clean(self):
        """Check that at least one form has been completed."""
        super(CobranzaRequireOneFormSet, self).clean()
        for error in self.errors:
            if error:
                return
        completed = 0
        if self.form.base_fields:
            for cleaned_data in self.cleaned_data:
                cleaned_data['field_timestamp_c']=datetime.datetime.now()+datetime.timedelta(seconds=completed)
                cleaned_data['counter']=int(time.time()+completed)  
                if cleaned_data and not cleaned_data.get('DELETE', False):
                    completed += 1
    
            if completed < 1:
                raise forms.ValidationError("Al menos un Pago es requerido.")
            

    def save_new(self, form, commit=True):
        form.instance.counter=form.cleaned_data['counter']
        form.instance.field_timestamp_c=form.cleaned_data['field_timestamp_c']
        return super(CobranzaRequireOneFormSet, self).save_new(form, commit=commit)

class CobranzaInline(admin.StackedInline):
    model = CobranzaCuentaPorCobrar
    extra= 1
    form=CobranzaCuentaPorCobrarAdminForm
    classes = ('collapse open',)
    inline_classes = ('collapse open',)
    verbose_name='Cobranza Asociada'
    verbose_name_plural='Cobranzas Asociadas'
    fieldsets = (
        (None, {
            'fields': ( 'numero_recibo','impreso','fecha_impreso','id_cliente','fecha','id_cobrador','monto', 'concepto')
        }),
                
    )
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return True    

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return True

    def save_model(self, request, obj, form, change):
        obj.save()    
    
class CuentaPorCobrarAdmin(VentasPlusModelAdmin):
    dateformat='%d/%m/%Y '
    list_display = ('numero_documento','id_cliente','procesada','esta_vencida','format_fecha_vencimiento','cancelada')
    search_fields = ['id_cliente__pc_nombre']
    list_filter = [("id_cliente__razon_social",ClienteListFilter),'procesada','fecha_vencimiento','cancelada']
    
    add_continue_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    add_another_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    add_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    
    change_continue_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_saveasnew_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_another_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    inlines=[CobranzaInline]
    
    def format_fecha_vencimiento(self, obj):
        if (obj.fecha_vencimiento):
            return obj.fecha_vencimiento.strftime(self.dateformat)
    format_fecha_vencimiento.short_description = _('Fecha Vencimiento')
    format_fecha_vencimiento.admin_order_field = 'fecha_vencimiento'    
    
    def save_model(self, request, obj, form, change):
        self.msg_dict={'name': force_text(obj._meta.verbose_name),'idC':force_text(obj.numero_documento),'obj':force_text(obj.id_cliente)}
        self.change_msg_dict={'name': force_text(obj._meta.verbose_name),'idC':force_text(obj.numero_documento),'obj':force_text(obj.id_cliente)}
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.save()
    
admin.site.register(CuentaPorCobrar,CuentaPorCobrarAdmin)
    
class CobranzaAdmin(VentasPlusModelAdmin):
    dateformat='%d/%m/%Y '
    list_display = ('numero_recibo','id_cliente','impreso','format_fecha_impreso','fecha','monto','concepto')
    search_fields = ['id_cliente__pc_nombre']
    list_filter = [("id_cliente__razon_social",ClienteListFilter),'impreso','fecha','concepto']
    
    add_continue_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    add_another_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    add_message=u'La %(name)s %(idC)s asociada al cliente "%(obj)s" fue agregada satisfactoriamente'
    
    change_continue_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_saveasnew_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_another_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    change_message='La %(name)s %(idC)s asociada al cliente "%(obj)s" fue modificada satisfactoriamente.'
    
    def format_fecha_impreso(self, obj):
        if (obj.fecha_impreso):
            return obj.fecha_impreso.strftime(self.dateformat)
    format_fecha_impreso.short_description = _('Fecha Impreso')
    format_fecha_impreso.admin_order_field = 'fecha_impreso'    


    def save_model(self, request, obj, form, change):
        self.msg_dict={'name': force_text(obj._meta.verbose_name),'idC':force_text(obj.numero_recibo),'obj':force_text(obj.id_cliente)}
        self.change_msg_dict={'name': force_text(obj._meta.verbose_name),'idC':force_text(obj.numero_recibo),'obj':force_text(obj.id_cliente)}
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.save()
    
admin.site.register(Cobranza,CobranzaAdmin)


class DepositoAdminForm(forms.ModelForm):
    numero= forms.CharField(max_length=64L, label=u'N\xFAmero')
    monto = forms.FloatField(required=True)
    cuenta = forms.CharField(max_length=64L, required=True, widget=forms.TextInput(attrs={'size': 64L, 'class':'vTextField'}))
    def __init__(self, *args, **kwargs):
        super(DepositoAdminForm, self).__init__(*args, **kwargs)
        if ('fecha' in self.fields):
            self.fields['fecha'].required = True
    class Meta:
        model = Deposito

class DepositoAdmin(VentasPlusModelAdmin):
    list_display = ('numero','id_banco','format_monto','format_fecha')
    search_fields = ['numero']
    exclude = ('id_surrogate','counter','field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id','latitud','longitud')
    form=DepositoAdminForm
    dateformat='%d/%m/%Y '    
    add_continue_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    add_another_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    add_message=u'El %(name)s "%(obj)s" fue agregado satisfactoriamente'
    
    change_continue_message=u'El %(name)s "%(obj)s" fue modificado satisfactoriamente'
    change_saveasnew_message=u'El %(name)s "%(obj)s" fue modificado satisfactoriamente'
    change_another_message=u'El %(name)s "%(obj)s" fue modificado satisfactoriamente'
    change_message=u'El %(name)s "%(obj)s" fue modificado satisfactoriamente'
    inlines=[PagoInline]
    
    def format_fecha(self, obj):
        if (obj.fecha):
            return obj.fecha.strftime(self.dateformat)
    format_fecha.short_description = _('Fecha')
    format_fecha.admin_order_field = 'fecha'    
        
    def format_monto(self, obj):
        return '{:,.2f}'.format(obj.monto).replace(".","%").replace(",",".").replace("%",",")+" Bs." 
    format_monto.short_description = 'Monto'
    format_monto.admin_order_field = 'monto'

    
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
        
class VisitaCreateAdmin(VisitaVentasPlusModelAdmin):
    form=VisitaAdminForm
    list_display = ['id_cliente','format_fecha','visitado','comentario']    
    dateformat='%d/%m/%Y '
    list_filter=[('fecha', DateRangeFilter),'id_cliente']
    search_fields = ['id_cliente']    
    fields=('fecha','id_cliente','comentario','id_motivo_visita')
    exclude = ('id_surrogate','counter','field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id','hora_inicio','hora_fin')
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
        obj.save()

    def format_fecha(self, obj):
        return obj.fecha.strftime(self.dateformat)
    format_fecha.short_description = _('Fecha')
    format_fecha.admin_order_field = 'fecha'

admin.site.register(Visita,VisitaCreateAdmin)


        
        
class VisitaRescheduleAdmin(VisitaVentasPlusModelAdmin):
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
    
admin.site.register(VisitaReschedule,VisitaRescheduleAdmin)

        
class VisitaCloseAdmin(VisitaVentasPlusModelAdmin):
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
    
admin.site.register(VisitaClose,VisitaCloseAdmin)

