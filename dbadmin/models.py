# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe
from synergy_ventasplus_web_admin import model_util
from django.template.defaultfilters import default
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import messages
from django.db.models import signals


class Grupo(models.Model):
    nombre = models.CharField(max_length=64L, primary_key=True)
    descripcion = models.CharField(max_length=512L, blank=True)
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'grupo'
        
class Banco(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField( db_column='_permissions', null=False, default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')        
        db_table = 'ps_banco'
    def __unicode__(self):
        return self.nombre        

class Categoria(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=True)
    id_level = models.IntegerField(null=True, blank=True,db_column='id_level')
    level = models.IntegerField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_categoria'
    def __unicode__(self):
        return self.nombre        

class Cliente(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    codigo = models.CharField(max_length=64L, blank=True , verbose_name=u'C\xF3digo')
    razon_social = models.CharField(max_length=64L, blank=True, verbose_name=u'Raz\xF3n Social')
    identificacion = models.CharField(max_length=16L, blank=True, verbose_name=u'Identificaci\xF3n')
    telefono1 = models.CharField(max_length=16L, blank=True, verbose_name=u'Tel\xE9fono')
    telefono2 = models.CharField(max_length=16L, blank=True, verbose_name=u'Tel\xE9fono Secundario')
    fax = models.CharField(max_length=16L, blank=True)
    correo = models.CharField(max_length=128L, blank=True)
    comentario = models.CharField(max_length=255L, blank=True)
    tipo = models.IntegerField(null=True, blank=True)
    flete = models.FloatField(null=True, blank=True)
    descuento_maestro = models.FloatField(null=True, blank=True)
    descuento_otro1 = models.FloatField(null=True, blank=True)
    descuento_otro2 = models.FloatField(null=True, blank=True)
    pc_nombre = models.CharField(max_length=64L, blank=True , verbose_name=u'Persona de Contacto')
    pc_telefono = models.CharField(max_length=16L, blank=True, verbose_name=u'Tel\xE9fono Persona de Contacto')
    pc_celular = models.CharField(max_length=16L, blank=True, verbose_name=u'Celular Persona de Contacto')
    pc_cargo = models.CharField(max_length=64L, blank=True, verbose_name=u'Cargo Persona de Contacto')
    pc_correo_electronico = models.CharField(max_length=128L, blank=True, verbose_name=u'Email Persona de Contacto')
    pc_fecha_nacimiento = models.CharField(max_length=10L, blank=True, verbose_name=u'Fecha Nac. Persona de Contacto')
    id_lista_precio = models.CharField(max_length=16L, blank=True, verbose_name=u'Lista de precio')
    #FIXME: CHANGED TO FK
    #id_zona = models.IntegerField(null=True, blank=True)
    id_zona = models.ForeignKey('Zona', db_column='id_zona', verbose_name=u'Zona')
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_cliente'
    def __unicode__(self):
        return self.razon_social
    
class Cobranza(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    numero_recibo = models.CharField(max_length=64L, blank=True,verbose_name="N\xFAmero de recibo")
    impreso = models.NullBooleanField(null=True, blank=True)
    fecha_impreso = models.DateField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    id_cobrador = models.IntegerField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente')    
    monto = models.FloatField(null=True, blank=True)
    concepto = models.CharField(max_length=64L, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_cobranza'
    def __unicode__(self):
        return self.numero_recibo+" ("+self.concepto+")"
    
class CuentaPorCobrar(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    numero_documento = models.CharField(max_length=64L, blank=True,verbose_name="N\xFAmero")
    monto_original = models.FloatField(null=True, blank=True)
    saldo_actual = models.FloatField(null=True, blank=True)
    fecha_documento = models.DateField(null=True, blank=True)
    fecha_despacho = models.DateField(null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    procesada = models.NullBooleanField(null=True, blank=True)
    cancelada = models.NullBooleanField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente',verbose_name="Cliente")   
    #FIXME: CHANGED TO FK
    #id_cobranza = models.IntegerField(null=True, blank=True)
    id_cobranza = models.ForeignKey('Cobranza', db_column='id_cobranza',verbose_name="Cobranza")   
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_cuenta_por_cobrar'
        verbose_name_plural='Cuentas por cobrar'
    def __unicode__(self):
        return self.numero_documento
    def esta_vencida(self):
        if ( self.fecha_vencimiento and (self.cancelada or self.fecha_vencimiento>datetime.date(datetime.now()))):        
            return mark_safe('<img src="/static/admin/img/icon-yes.gif" alt="Si">')
        elif (self.fecha_vencimiento and self.fecha_vencimiento<=datetime.date(datetime.now())):
            return mark_safe('<img src="/static/admin/img/icon-no.gif" alt="No">')
    esta_vencida.allow_tags = True
    esta_vencida.short_description = 'Vigente'
    
        
class Deposito(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    numero = models.CharField(max_length=64L, blank=True,verbose_name="N\xFAmero")
    monto = models.FloatField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_banco = models.IntegerField(null=True, blank=True)
    id_banco = models.ForeignKey('Banco', db_column='id_banco', verbose_name=u'Banco')       
    fecha = models.DateField(null=True, blank=True)
    cuenta = models.CharField(max_length=64L, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_deposito'
        verbose_name=u'dep\xF3sito'
        verbose_name_plural=u'dep\xF3sitos'
        
    def __unicode__(self):
        return self.numero
    
class DetalleProducto(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    #FIXME: CHANGED TO FK
    id_level = models.IntegerField(null=True, blank=True)
#    id_level = models.ForeignKey('Categoria',null=False, blank=False,to_field='id_level')
    level = models.IntegerField(null=True, blank=True)
    descripcion_level = models.CharField(max_length=255L, blank=True)
    id_letter = models.CharField(max_length=16L, blank=True)
    #FIXME: CHANGED TO FK
    #id_producto = models.IntegerField(max_length=64L,null=True, blank=True)
    id_producto = models.ForeignKey('Producto', max_length=64L, db_column='id_producto',null=True, blank=True, verbose_name='Producto')      
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_detalle_producto'
    def __unicode__(self):
        return {1: u'categor\xEDa',2: u'tipo',3: u'l\xEDnea',4: u'calidad',5: u'tama\xF1o',6: u'color',}.get(self.level, None)+" "+self.descripcion_level

    
class Direccion(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=True)
    direccion = models.CharField(max_length=255L, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente', verbose_name='Cliente')       
    flete = models.FloatField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_direccion'

class Item(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    id_lista_precio = models.CharField(max_length=16L, blank=True)
    precio = models.FloatField(null=True, blank=True)
    codigo_barra = models.CharField(max_length=64L, blank=True)   
    #FIXME: CHANGED TO FK
    #id_producto = models.IntegerField(max_length=64L,null=True, blank=True)
    id_producto = models.ForeignKey('Producto', max_length=64L, db_column='id_producto',null=True, blank=True, verbose_name='Producto')      
    #FIXME: CHANGED TO FK
    #id_unidad = models.IntegerField(max_length=64L,null=True, blank=True)
    id_unidad = models.ForeignKey('Unidad', max_length=64L, db_column='id_unidad',null=True, blank=True)      
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_item'

class ItemPedido(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    cantidad = models.IntegerField(null=True, blank=True)
    direccion_entrega = models.CharField(max_length=255L, blank=True)
    comentario = models.CharField(max_length=255L, blank=True)
    monto_impuesto = models.FloatField(null=True, blank=True)
    monto_total = models.FloatField(null=True, blank=True)
    flete = models.FloatField(null=True, blank=True)
    descuento = models.FloatField(null=True, blank=True)
    precio_unidad = models.FloatField(null=True, blank=True)
    porcentaje_impuesto = models.FloatField(null=True, blank=True)
    descuento_negativo = models.FloatField(null=True, blank=True)
    tipo_descuento = models.FloatField(null=True, blank=True)
    id_impuesto = models.IntegerField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_unidad = models.IntegerField(max_length=64L,null=True, blank=True)
    id_unidad = models.ForeignKey('Unidad', max_length=64L, db_column='id_unidad',null=True, blank=True)          
    #FIXME: CHANGED TO FK
    #id_producto = models.IntegerField(max_length=64L,null=True, blank=True)
    id_producto = models.ForeignKey('Producto', max_length=64L, db_column='id_producto',null=True, blank=True, verbose_name='Producto')      
    #FIXME: CHANGED TO FK
    #id_pedido = models.IntegerField(max_length=64L,null=True, blank=True)
    id_pedido = models.ForeignKey('Pedido', db_column='id_pedido',null=True, blank=True)      
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_item_pedido'
    def __unicode__(self):
        return self.id_surrogate
    #TODO: Find a better way to save owner 
    def save(self,*args,**kwargs):
        self.field_owner_id = self.id_pedido.field_owner_id
        self.field_group_id = self.id_pedido.field_group_id
        self.field_inst_id = self.id_pedido.field_inst_id
        self.field_permissions = self.id_pedido.field_permissions
        self.field_timestamp_c = self.id_pedido.field_timestamp_c
        self.field_timestamp_m = self.id_pedido.field_timestamp_m
        self.field_deleted = self.id_pedido.field_deleted
        super(ItemPedido,self).save(*args,**kwargs)     

class MetodoPago(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=True)
    banco = models.NullBooleanField(null=True, blank=True)
    monto = models.NullBooleanField(null=True, blank=True)
    numero = models.NullBooleanField(null=True, blank=True,verbose_name="N\xFAmero")
    fecha = models.NullBooleanField(null=True, blank=True)
    titular = models.NullBooleanField(null=True, blank=True)
    deposito = models.NullBooleanField(null=True, blank=True,verbose_name=u'Dep\xF3sito')    
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_metodo_pago'
    def __unicode__(self):
        return self.nombre
            
class Motivo(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=True)
    tipo = models.IntegerField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_motivo'
    def __unicode__(self):
        return str(self.nombre)

class Pago(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    monto = models.FloatField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_banco = models.IntegerField(null=True, blank=True)
    id_banco = models.ForeignKey('Banco', db_column='id_banco')     
    fecha_documento = models.DateField(null=True, blank=True)
    numero_documento = models.CharField(max_length=64L, blank=True,verbose_name="N\xFAmero de documento")
    titular = models.CharField(max_length=64L, blank=True)
    saldo = models.FloatField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_cobranza = models.IntegerField(null=True, blank=True)
    id_cobranza = models.ForeignKey('Cobranza', db_column='id_cobranza')   
    #FIXME: CHANGED TO FK
    #id_deposito = models.CharField(max_length=64L, blank=True)
    id_deposito = models.ForeignKey('Deposito', db_column='id_deposito',verbose_name=u'Dep\xF3sito')       
    id_metodo_pago = models.IntegerField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_pago'

class Pedido(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    numero = models.CharField(max_length=64L, blank=True,verbose_name=u'N\xFAmero')
    fecha = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    orden_de_compra = models.CharField(max_length=64L, blank=True)
    total_bruto = models.FloatField(null=True, blank=True)
    descuento_maestro = models.FloatField(null=True, blank=True)
    descuento_otro1 = models.FloatField(null=True, blank=True)
    descuento_otro2 = models.FloatField(null=True, blank=True)
    sub_total = models.FloatField(null=True, blank=True)
    impuesto = models.FloatField(null=True, blank=True)
    otro_impuesto = models.FloatField(null=True, blank=True)
    flete = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    comentario = models.CharField(max_length=255L, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente', verbose_name='Cliente')    
    #FIXME: CHANGED TO FK
    #id_metodo_pago = models.IntegerField(null=True, blank=True)
    id_metodo_pago = models.ForeignKey('MetodoPago', db_column='id_metodo_pago',verbose_name=u'M\xE9todo de Pago')
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_pedido'
    def tiene_comentario(self):
        if (self.comentario!=u''):        
            return mark_safe('<img src="/static/admin/img/icon_success.gif" alt="Si">')
        else:
            return mark_safe('<img src="/static/admin/img/icon_error.gif" alt="No">')

    tiene_comentario.allow_tags = True
    tiene_comentario.short_description = '\xBFTiene Comentario?'
    def __unicode__(self):
        return '#'+self.numero; 

class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super(DahlBookManager, self).get_queryset().filter(itemno='1000').annotate(testprop='BASURA')
        
class Producto(models.Model):
    objects = DahlBookManager()
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id',verbose_name=u'N\xFAmero')
    itemno = models.CharField(max_length=64L, db_column='itemNo', blank=True,verbose_name=u'N\xFAmero de item') # Field name made lowercase.
    nombre = models.CharField(max_length=64L, blank=True)
    precio = models.FloatField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    comentario = models.CharField(max_length=255L, blank=True)
    imagen = models.CharField(max_length=255L, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255L, db_column='_inst_id',default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_producto'
    def __unicode__(self):
        return self.nombre    
        
class Unidad(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=True)
    unidad = models.IntegerField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_unidad'

class Visita(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    hora_inicio = models.CharField(max_length=16L, blank=True)
    hora_fin = models.CharField(max_length=16L, blank=True)
    fecha_reagenda = models.DateField(null=True, blank=True,verbose_name='Nueva Fecha')
    id_motivo_visita = models.ForeignKey('Motivo',null=True, blank=True, verbose_name='Motivo Visita',db_column='id_motivo_visita')
    id_motivo_no_visita = models.ForeignKey('Motivo',null=True, blank=True, verbose_name='Motivo No Visita',related_name='novisita',db_column='id_motivo_no_visita')
    id_motivo_no_cobranza = models.ForeignKey('Motivo',null=True, blank=True, verbose_name='Motivo No Cobranza',related_name='nocobranza',db_column='id_motivo_no_cobranza')
    id_motivo_no_pedido = models.ForeignKey('Motivo',null=True, blank=True, verbose_name='Motivo No Pedido',related_name='nopedido',db_column='id_motivo_no_pedido')
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente',verbose_name='Cliente', db_column='id_cliente')  
    fecha = models.DateField(null=True, blank=True)
    comentario = models.CharField(max_length=255L, blank=True)
    visitado = models.NullBooleanField(null=True, blank=True)
    fecha_modificacion = models.DateField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_visita'
    def __unicode__(self):
        return str(self.id_cliente)+' Fecha: '+str(self.fecha)
        
class VisitaClose(Visita):
    class Meta:
        proxy=True
        verbose_name='Modificar Visitas'
        verbose_name_plural='Modificar Visitas'
    def __unicode__(self):
        return str(self.id_cliente)+' Fecha: '+str(self.fecha)+" CERRADA"        
        
class VisitaReschedule(Visita):
    class Meta:
        proxy=True
        verbose_name='Modificar Visitas'
        verbose_name_plural='Modificar Visitas'        
    def __unicode__(self):
        return str(self.id_cliente)+' Fecha: '+str(self.fecha)+" REAGENDADA"        


class Zona(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_zona'
    def __unicode__(self):
        return self.nombre
    
class ZonaUsuario(models.Model):
    id_surrogate = models.AutoField(primary_key=True,db_column='_surrogate_id')
    id_usuario_app = models.IntegerField(null=True, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=255, db_column='_inst_id', default=0)
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=True) # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        unique_together = ('field_owner_id', 'field_timestamp_c')
        db_table = 'ps_zona_usuario'

class RsGrupoUsuario(models.Model):
    nombre = models.ForeignKey(Grupo, db_column='nombre')
    username = models.ForeignKey('Usuario', db_column='username')
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'rs_grupo_usuario'

class Usuario(models.Model):
    nombre = models.CharField(max_length=64L, blank=True)
    apellido = models.CharField(max_length=64L, blank=True)
    codigo = models.CharField(max_length=64L, blank=True, verbose_name=u'C\xF3digo')
    username = models.CharField(max_length=32L, primary_key=True, verbose_name=u'Nombre de Usuario')
    password = models.CharField(max_length=32L, blank=True)
    correo = models.CharField(max_length=128L, blank=True)
    field_timestamp_c = models.PositiveIntegerField(max_length=22, db_column='_timestamp_c',null=False, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    adminuser = models.OneToOneField(User, null=True, blank=True, verbose_name=u'Usuario Administrador')
    class Meta:
        db_table = 'usuario'
    def __unicode__(self):
        return self.username
