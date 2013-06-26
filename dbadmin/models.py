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
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
import time
dateformat='%d/%m/%Y '

class SuperModel(models.Model):
    def save(self,*args,**kwargs):
        self.field_inst_id='webadmin'
        self.field_permissions=0
        #Mini hack for saving inlines that define their own timestamp
        if hasattr(self, 'field_timestamp_c') and not self.field_timestamp_c:
            self.field_timestamp_c=datetime.now()
        self.field_timestamp_m=datetime.now()
        self.field_group_id= Grupo.objects.get(pk='admin')             
        if hasattr(self, 'id_surrogate') and not self.id_surrogate:
            #Mini hack for saving inlines that define their own counter
            if hasattr(self, 'counter') and not self.counter:    
                self.counter=int(time.time())
            self.id_surrogate=str(self.field_owner_id)+":"+str(self.field_inst_id)+":"+str(self.counter)
        super(SuperModel,self).save(*args,**kwargs) 
    class Meta:
        abstract = True
        
class Bitacora(models.Model):
    usuario = models.ForeignKey('Usuario',db_column='usuario')
    operacion = models.CharField(max_length=64L,null=False, blank=False)
    timestamp = model_util.UnixTimestampField(null=False, blank=False) # Field renamed because it started with '_'.
    extra = models.CharField(max_length=256L,null=True, blank=True)
    class Meta:
        db_table = 'bitacora'
        
class Grupo(models.Model):
    nombre = models.CharField(max_length=64L, primary_key=True)
    descripcion = models.CharField(max_length=512L, blank=False)
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'grupo'
                
        
class Banco(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=False)
    counter=models.IntegerField( max_length=16L, db_column='_counter', null=False, blank=False)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField( db_column='_permissions', null=False, default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        
        db_table = 'ps_banco'
    def __unicode__(self):
        return self.nombre        

class BancoCuenta(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    id_banco = models.ForeignKey('Banco', db_column='id_banco', verbose_name=u'Banco')      
    cuenta = models.CharField(max_length=64L, blank=False) 
    counter=models.IntegerField( max_length=16L, db_column='_counter', null=False, blank=False)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField( db_column='_permissions', null=False, default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'ps_banco_cuenta'
    def __unicode__(self):
        return self.cuenta  

class Categoria(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=False)
    id_level = models.IntegerField(null=True, blank=True,db_column='id_level')
    level = models.IntegerField(null=True, blank=True)
    parent_id_level = models.IntegerField(null=True, blank=True,db_column='parent_id_level')
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_categoria'
    def __unicode__(self):
        return self.nombre        

class Cliente(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    codigo = models.CharField(max_length=64L, null=True, blank=False , verbose_name=u'C\xF3digo')
    razon_social = models.CharField(max_length=64L, blank=False, verbose_name=u'Raz\xF3n Social')
    identificacion = models.CharField(max_length=16L, blank=False, verbose_name=u'Identificaci\xF3n')
    telefono1 = models.CharField(max_length=16L, null=True, blank=True, verbose_name=u'Tel\xE9fono')
    telefono2 = models.CharField(max_length=16L, null=True,  blank=True, verbose_name=u'Tel\xE9fono Secundario')
    fax = models.CharField(max_length=16L, null=True, blank=True)
    correo = models.CharField(max_length=128L, blank=False)
    comentario = models.CharField(max_length=255L, blank=False)
    tipo = models.IntegerField(null=True, blank=True)
    flete = models.FloatField(null=True, blank=True)
    limite_credito = models.FloatField(null=True, blank=True)
    saldo_disponible = models.FloatField(null=True, blank=True)
    descuento_maestro = models.FloatField(null=True, blank=True)
    descuento_otro1 = models.FloatField(null=True, blank=True)
    descuento_otro2 = models.FloatField(null=True, blank=True)
    pc_nombre = models.CharField(max_length=64L, blank=False , verbose_name=u'Nombre')
    pc_telefono = models.CharField(max_length=16L, blank=False, verbose_name=u'Tel\xE9fono')
    pc_celular = models.CharField(max_length=16L, blank=False, verbose_name=u'Celular')
    pc_cargo = models.CharField(max_length=64L, blank=False, verbose_name=u'Cargo')
    pc_correo_electronico = models.CharField(max_length=128L, blank=False, verbose_name=u'Email')
    pc_fecha_nacimiento = models.CharField(max_length=10L, blank=False, verbose_name=u'Fecha de Nacimiento')
    id_lista_precio = models.CharField(max_length=16L, blank=False, verbose_name=u'Lista de precio')
    #FIXME: CHANGED TO FK
    #id_zona = models.IntegerField(null=True, blank=True)
    #id_zona = models.ForeignKey('Zona', db_column='id_zona', verbose_name=u'Zona')
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_cliente'
    def __unicode__(self):
        return self.razon_social
    
class Cobranza(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    numero_recibo = models.CharField(max_length=64L, blank=False,verbose_name="N\xFAmero de recibo")
    impreso = models.NullBooleanField(null=True, blank=True)
    fecha_impreso = models.DateField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    id_cobrador = models.CharField(max_length=192L,null=False, blank=False,verbose_name="Cobrador")
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente',verbose_name="Cliente")    
    monto = models.FloatField(null=False, blank=False)
    concepto = models.CharField(max_length=64L, blank=False)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    correlativo=models.IntegerField( db_column='correlativo', null=True, blank=True)
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'ps_cobranza'
    def __unicode__(self):
        return '#'+self.numero_recibo+" ("+self.concepto+")"


class CobranzaCuentaPorCobrar(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    id_cobranza = models.ForeignKey('Cobranza', db_column='id_cobranza',null=False, blank=False,verbose_name="Cobranza") 
    id_cuenta_por_cobrar = models.ForeignKey('CuentaPorCobrar', db_column='id_cuenta_por_cobrar',null=False, blank=False,verbose_name="Cuenta por cobrar") 
    fecha = models.DateField(null=True, blank=True)
    tipo=models.CharField(max_length=64L ,null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente',verbose_name="Cliente")    
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'ps_cobranza_cuenta_por_cobrar'
    def __unicode__(self):
        return str(self.id_cobranza)+" ("+str(self.id_cuenta_por_cobrar)+")"

class Configuracion(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    clave= models.CharField(max_length=192L,null=False, blank=False)
    valor= models.CharField(max_length=192L,null=True, blank=True)
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'ps_configuracion'
    def __unicode__(self):
        return self.clave

class CuentaPorCobrar(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    numero_documento = models.CharField(max_length=64L, blank=False,verbose_name="N\xFAmero")
    monto_original = models.FloatField(null=False, blank=False)
    saldo_actual = models.FloatField(null=False, blank=False)
    saldo_erp = models.FloatField(null=False, blank=False)

    fecha_documento = models.DateField(null=False, blank=False)
    fecha_despacho = models.DateField(null=True, blank=True)
    fecha_vencimiento = models.DateField(null=False, blank=False)
    fecha_entrega = models.DateField(null=True, blank=True)
    tipo=models.CharField(max_length=64L ,null=True, blank=True)

    procesada = models.NullBooleanField(null=True, blank=True)
    cancelada = models.NullBooleanField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente',verbose_name="Cliente")   
    #FIXME: CHANGED TO FK
    #id_cobranza = models.IntegerField(null=True, blank=True)
#    id_cobranza = models.ForeignKey('Cobranza', db_column='id_cobranza',null=True, blank=True,verbose_name="Cobranza",default=None)   
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    cobranzas = models.ManyToManyField('Cobranza', through=CobranzaCuentaPorCobrar)

    class Meta:
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
    
        
class Deposito(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    numero = models.CharField(max_length=64L, blank=False,verbose_name="N\xFAmero")
    monto = models.FloatField(null=False, blank=False)
    #FIXME: CHANGED TO FK
    #id_banco = models.IntegerField(null=True, blank=True)
    id_banco = models.ForeignKey('Banco', db_column='id_banco', verbose_name=u'Banco')       
    fecha = models.DateField(null=True, blank=True)
    cuenta = models.CharField(max_length=64L, blank=False)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    correlativo=models.IntegerField( db_column='correlativo', null=True, blank=True)    
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_deposito'
        verbose_name=u'dep\xF3sito'
        verbose_name_plural=u'dep\xF3sitos'
        
    def __unicode__(self):
        return self.numero
    
class DetalleProducto(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    #FIXME: CHANGED TO FK
    id_level = models.IntegerField(null=True, blank=True)
#    id_level = models.ForeignKey('Categoria',null=False, blank=False,to_field='id_level')
    level = models.IntegerField(null=True, blank=True)
    descripcion_level = models.CharField(max_length=255L, blank=False)
    id_letter = models.CharField(max_length=16L, blank=False)
    #FIXME: CHANGED TO FK
    #id_producto = models.IntegerField(max_length=64L,null=True, blank=True)
    id_producto = models.ForeignKey('Producto', max_length=64L, db_column='id_producto',null=False, blank=False, verbose_name='Producto')      
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_detalle_producto'
    def __unicode__(self):
        return {1: u'Categor\xEDa',2: u'Tipo',3: u'L\xEDnea',4: u'Calidad',5: u'Tama\xF1o',6: u'Color',}.get(self.level, None)+" "+self.descripcion_level

    
class Direccion(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=False)
    direccion = models.CharField(max_length=255L, blank=False)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente', verbose_name='Cliente')       
    flete = models.FloatField(null=True, blank=True)
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_direccion'

class Item(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    id_lista_precio = models.CharField(max_length=16L, blank=False)
    precio = models.FloatField(null=False, blank=False)
    codigo_barra = models.CharField(max_length=64L, blank=False)   
    #FIXME: CHANGED TO FK
    #id_producto = models.IntegerField(max_length=64L,null=True, blank=True)
    id_producto = models.ForeignKey('Producto', max_length=64L, db_column='id_producto',null=False, blank=False, verbose_name='Producto')      
    #FIXME: CHANGED TO FK
    #id_unidad = models.IntegerField(max_length=64L,null=True, blank=True)
    id_unidad = models.ForeignKey('Unidad', max_length=64L, db_column='id_unidad',null=False, blank=False)      
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_item'
    def __unicode__(self):
        return str(self.id_producto)
    
class ItemPedido(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    cantidad = models.IntegerField(null=True, blank=True)
    direccion_entrega = models.CharField(max_length=255L, blank=False)
    comentario = models.CharField(max_length=255L, blank=False)
    monto_impuesto = models.FloatField(null=True, blank=True)
    monto_total = models.FloatField(null=True, blank=True)
    flete = models.FloatField(null=True, blank=True)
    descuento = models.FloatField(null=True, blank=True)
    precio_unidad = models.FloatField(null=False, blank=False)
    porcentaje_impuesto = models.FloatField(null=True, blank=True)
    descuento_negativo = models.FloatField(null=True, blank=True)
    tipo_descuento = models.FloatField(null=True, blank=True)
    id_impuesto = models.CharField(null=True, max_length=64L, blank=True)
    #FIXME: CHANGED TO FK
    #id_unidad = models.IntegerField(max_length=64L,null=True, blank=True)
    id_unidad = models.ForeignKey('Unidad', max_length=64L, db_column='id_unidad',null=False, blank=False)          
    #FIXME: CHANGED TO FK
    #id_producto = models.IntegerField(max_length=64L,null=True, blank=True)
    id_producto = models.ForeignKey('Producto', max_length=64L, db_column='id_producto',null=False, blank=False, verbose_name='Producto')      
    #FIXME: CHANGED TO FK
    #id_pedido = models.IntegerField(max_length=64L,null=True, blank=True)
    id_pedido = models.ForeignKey('Pedido', db_column='id_pedido',null=False, blank=False)      
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_item_pedido'
    def __unicode__(self):
        return self.id_surrogate
    #TODO: Find a better way to save owner 
    def save(self,*args,**kwargs):
        self.field_owner_id = self.id_pedido.field_owner_id
        super(ItemPedido,self).save(*args,**kwargs)     

class MetodoPago(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=False)
    banco = models.NullBooleanField(null=True, blank=True)
    monto = models.NullBooleanField(null=True, blank=True)
    numero = models.NullBooleanField(null=True, blank=True,verbose_name="N\xFAmero")
    fecha = models.NullBooleanField(null=True, blank=True)
    titular = models.NullBooleanField(null=True, blank=True)
    deposito = models.NullBooleanField(null=True, blank=True,verbose_name=u'Dep\xF3sito')    
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_metodo_pago'
    def __unicode__(self):
        return self.nombre
            
class Motivo(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=False)
    tipo = models.IntegerField(null=True, blank=True)
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_motivo'
    def __unicode__(self):
        return smart_unicode(self.nombre)

class Pago(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    monto = models.FloatField(null=False, blank=False)
    #FIXME: CHANGED TO FK
    #id_banco = models.IntegerField(null=True, blank=True)
    id_banco = models.ForeignKey('Banco', db_column='id_banco',verbose_name=u'Banco',null=True, blank=True)     
    fecha_documento = models.DateField(null=True, blank=True)
    numero_documento = models.CharField(max_length=64L, blank=False,verbose_name="N\xFAmero de documento")
    titular = models.CharField(max_length=64L, blank=False)
    saldo = models.FloatField(null=False, blank=False)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente', verbose_name='Cliente')    
    #FIXME: CHANGED TO FK
    #id_cobranza = models.IntegerField(null=True, blank=True)
    id_cobranza = models.ForeignKey('Cobranza', db_column='id_cobranza',verbose_name=u'Cobranza')   
    #FIXME: CHANGED TO FK
    #id_deposito = models.CharField(max_length=64L, blank=False)
    id_deposito = models.ForeignKey('Deposito', db_column='id_deposito',verbose_name=u'Dep\xF3sito',blank=True, null=True,default=None)       
    id_metodo_pago = models.ForeignKey('MetodoPago', db_column='id_metodo_pago',verbose_name=u'M\xE9todo de Pago')
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_pago'
    def __unicode__(self):
        return '#'+smart_unicode(self.id_surrogate)        
    def save(self,*args,**kwargs):
        self.field_owner_id = self.id_deposito.field_owner_id
        super(Pago,self).save(*args,**kwargs)     

class PedidoStatus():
    SIN_APROBAR = 0
    PRE_APROBADO = 5
    APROBADO = 10
    
STATUS_CHOICES = (
    (PedidoStatus.SIN_APROBAR, 'Sin Aprobar'),
    (PedidoStatus.PRE_APROBADO, 'Pre-Aprobado'),
    (PedidoStatus.APROBADO, 'Aprobado'),
)
        
class Pedido(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    numero = models.CharField(max_length=64L, blank=False,verbose_name=u'N\xFAmero')
    fecha = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    orden_de_compra = models.CharField(max_length=64L, blank=False)
    total_bruto = models.FloatField(null=True, blank=True)
    descuento_maestro = models.FloatField(null=True, blank=True)
    descuento_otro1 = models.FloatField(null=True, blank=True)
    descuento_otro2 = models.FloatField(null=True, blank=True)
    sub_total = models.FloatField(null=True, blank=True)
    impuesto = models.FloatField(null=True, blank=True)
    otro_impuesto = models.FloatField(null=True, blank=True)
    flete = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    comentario = models.CharField(max_length=255L, blank=False)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', db_column='id_cliente', verbose_name='Cliente')    
    #FIXME: CHANGED TO FK
    #id_metodo_pago = models.IntegerField(null=True, blank=True)
    id_metodo_pago = models.ForeignKey('MetodoPago', db_column='id_metodo_pago',verbose_name=u'M\xE9todo de Pago', null=True, blank=True)
    correlativo=models.IntegerField( db_column='correlativo', null=True, blank=True)    
    estatus=models.IntegerField( db_column='estatus', null=True, blank=True,choices=STATUS_CHOICES)    
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'ps_pedido'
        permissions = (
            ("preapprove_pedido", "Can pre-approve pedidos"),
            ("approve_pedido", "Can approve pedidos"),
        )        
        
    def tiene_comentario(self):
        if (self.comentario!=u''):        
            return mark_safe('<img src="/static/admin/img/icon_success.gif" alt="Si">')
        else:
            return mark_safe('<img src="/static/admin/img/icon_error.gif" alt="No">')

    tiene_comentario.allow_tags = True
    tiene_comentario.short_description = '\xBFTiene Comentario?'
    def __unicode__(self):
        return '#'+self.numero; 
        
class Producto(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    itemno = models.CharField(max_length=64L, db_column='itemNo', blank=False,verbose_name=u'N\xFAmero de item') # Field name made lowercase.
    nombre = models.CharField(max_length=64L, blank=False)
    precio = models.FloatField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    comentario = models.CharField(max_length=255L, blank=False)
    imagen = models.CharField(max_length=255L, blank=False)
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_producto'
    def __unicode__(self):
        return self.nombre    
        
class Unidad(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    nombre = models.CharField(max_length=64L, blank=False)
    unidad = models.IntegerField(null=True, blank=True)
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_unidad'
    def __unicode__(self):
        return self.nombre
    
class Visita(SuperModel):
    id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
    hora_inicio = models.CharField(max_length=16L, blank=False)
    hora_fin = models.CharField(max_length=16L, blank=False)
    fecha_reagenda = models.DateField(null=True, blank=True,verbose_name='Nueva Fecha')
    id_motivo_visita = models.ForeignKey('Motivo',null=True, blank=True, verbose_name='Motivo Visita',db_column='id_motivo_visita')
    id_motivo_no_visita = models.ForeignKey('Motivo',null=True, blank=True, verbose_name='Motivo No Visita',related_name='novisita',db_column='id_motivo_no_visita')
    id_motivo_no_cobranza = models.ForeignKey('Motivo',null=True, blank=True, verbose_name='Motivo No Cobranza',related_name='nocobranza',db_column='id_motivo_no_cobranza')
    id_motivo_no_pedido = models.ForeignKey('Motivo',null=True, blank=True, verbose_name='Motivo No Pedido',related_name='nopedido',db_column='id_motivo_no_pedido')
    #FIXME: CHANGED TO FK
    #id_cliente = models.IntegerField(null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente',verbose_name='Cliente', db_column='id_cliente')  
    fecha = models.DateField(null=True, blank=True)
    comentario = models.CharField(max_length=255L, blank=False)
    visitado = models.NullBooleanField(null=True, blank=True)
    fecha_modificacion = models.DateField(null=True, blank=True)
    counter=models.IntegerField( db_column='_counter', null=False, blank=True)
    field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
    field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
    field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
    field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:

        db_table = 'ps_visita'
    def __unicode__(self):
        return str(self.id_cliente)+' Fecha: '+str(self.fecha.strftime(dateformat))
class VisitaClose(Visita):
    class Meta:
        proxy=True
        verbose_name='Cerrar Visitas'
        verbose_name_plural='Cerrar Visitas'
    def __unicode__(self):
        return str(self.id_cliente)+' Fecha: '+str(self.fecha.strftime(dateformat))+" CERRADA"        
        
class VisitaReschedule(Visita):
    class Meta:
        proxy=True
        verbose_name='Reagendar Visitas'
        verbose_name_plural='Reagendar Visitas'        
    def __unicode__(self):
        return str(self.id_cliente)+' Fecha: '+str(self.fecha.strftime(dateformat))+" REAGENDADA"        


# class Zona(SuperModel):
#     id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
#     nombre = models.CharField(max_length=64L, blank=False)
#     counter=models.IntegerField( db_column='_counter', null=False, blank=True)
#     field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
#     field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
#     field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
#     field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
#     field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
#     field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
#     field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
#     class Meta:
# 
#         db_table = 'ps_zona'
#     def __unicode__(self):
#         return self.nombre
#     
# class ZonaUsuario(SuperModel):
#     id_surrogate= models.CharField(max_length=192L,primary_key=True,db_column='_surrogate_id')
#     id_usuario_app = models.IntegerField(null=True, blank=True)
#     counter=models.IntegerField( db_column='_counter', null=False, blank=True)
#     field_owner_id = models.ForeignKey('Usuario', db_column='_owner_id', default='admin') # Field renamed because it started with '_'.
#     field_inst_id  = models.CharField(max_length=128, db_column='_inst_id', default='backend')
#     field_group_id = models.ForeignKey('Grupo', db_column='_group_id', blank=False, default='admin') # Field renamed because it started with '_'.
#     field_permissions = models.IntegerField(null=False, db_column='_permissions', blank=False,default=0) # Field renamed because it started with '_'.
#     field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
#     field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
#     field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
#     class Meta:
# 
#         db_table = 'ps_zona_usuario'

class RsGrupoUsuario(models.Model):
    nombre = models.ForeignKey(Grupo, db_column='nombre')
    username = models.ForeignKey('Usuario', db_column='username')
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    class Meta:
        db_table = 'rs_grupo_usuario'

class Usuario(models.Model):
    nombre = models.CharField(max_length=64L, blank=False)
    apellido = models.CharField(max_length=64L, blank=False)
    codigo = models.CharField(max_length=64L, blank=False, verbose_name=u'C\xF3digo')
    username = models.CharField(max_length=32L, primary_key=True, verbose_name=u'Nombre de Usuario')
    password = models.CharField(max_length=32L, blank=False)
    correo = models.CharField(max_length=128L, blank=False)
    field_timestamp_c = model_util.UnixTimestampField(max_length=22, db_column='_timestamp_c',null=True, blank=False) # Field renamed because it started with '_'.    
    field_timestamp_m = model_util.UnixTimestampField(db_column='_timestamp_m',null=False, blank=False) # Field renamed because it started with '_'.
    field_deleted = models.BooleanField(db_column='_deleted',default=0) # Field renamed because it started with '_'.
    adminuser = models.OneToOneField(User, null=True, blank=True, verbose_name=u'Usuario Administrador')
    class Meta:
        db_table = 'usuario'
    def __unicode__(self):
        return self.username
    
class Secuencia(models.Model):
    contador = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'secuencia'
    def __unicode__(self):
        return self.contador    
