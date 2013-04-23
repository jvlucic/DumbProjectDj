# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Grupo'
        db.create_table(u'grupo', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L, primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=512L)),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Grupo'])

        # Adding model 'Banco'
        db.create_table(u'ps_banco', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(max_length=16L, db_column=u'_counter')),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Banco'])

        # Adding unique constraint on 'Banco', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_banco', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Categoria'
        db.create_table(u'ps_categoria', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('id_level', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'id_level', blank=True)),
            ('level', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('parent_id_level', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'parent_id_level', blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Categoria'])

        # Adding unique constraint on 'Categoria', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_categoria', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Cliente'
        db.create_table(u'ps_cliente', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=64L, null=True)),
            ('razon_social', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('identificacion', self.gf('django.db.models.fields.CharField')(max_length=16L)),
            ('telefono1', self.gf('django.db.models.fields.CharField')(max_length=16L, null=True, blank=True)),
            ('telefono2', self.gf('django.db.models.fields.CharField')(max_length=16L, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=16L, null=True, blank=True)),
            ('correo', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('tipo', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('flete', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descuento_maestro', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descuento_otro1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descuento_otro2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pc_nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('pc_telefono', self.gf('django.db.models.fields.CharField')(max_length=16L)),
            ('pc_celular', self.gf('django.db.models.fields.CharField')(max_length=16L)),
            ('pc_cargo', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('pc_correo_electronico', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('pc_fecha_nacimiento', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('id_lista_precio', self.gf('django.db.models.fields.CharField')(max_length=16L)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Cliente'])

        # Adding unique constraint on 'Cliente', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_cliente', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Cobranza'
        db.create_table(u'ps_cobranza', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('numero_recibo', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('impreso', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('fecha_impreso', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('id_cobrador', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('id_cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Cliente'], db_column=u'id_cliente')),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('concepto', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Cobranza'])

        # Adding unique constraint on 'Cobranza', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_cobranza', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'CuentaPorCobrar'
        db.create_table(u'ps_cuenta_por_cobrar', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('numero_documento', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('monto_original', self.gf('django.db.models.fields.FloatField')()),
            ('saldo_actual', self.gf('django.db.models.fields.FloatField')()),
            ('fecha_documento', self.gf('django.db.models.fields.DateField')()),
            ('fecha_despacho', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_vencimiento', self.gf('django.db.models.fields.DateField')()),
            ('fecha_entrega', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('procesada', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('cancelada', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('id_cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Cliente'], db_column=u'id_cliente')),
            ('id_cobranza', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['dbadmin.Cobranza'], null=True, db_column=u'id_cobranza', blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['CuentaPorCobrar'])

        # Adding unique constraint on 'CuentaPorCobrar', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_cuenta_por_cobrar', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Deposito'
        db.create_table(u'ps_deposito', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('id_banco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Banco'], db_column=u'id_banco')),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cuenta', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Deposito'])

        # Adding unique constraint on 'Deposito', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_deposito', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'DetalleProducto'
        db.create_table(u'ps_detalle_producto', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('id_level', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('descripcion_level', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('id_letter', self.gf('django.db.models.fields.CharField')(max_length=16L)),
            ('id_producto', self.gf('django.db.models.fields.related.ForeignKey')(max_length=64L, to=orm['dbadmin.Producto'], null=True, db_column=u'id_producto', blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['DetalleProducto'])

        # Adding unique constraint on 'DetalleProducto', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_detalle_producto', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Direccion'
        db.create_table(u'ps_direccion', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('id_cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Cliente'], db_column=u'id_cliente')),
            ('flete', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Direccion'])

        # Adding unique constraint on 'Direccion', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_direccion', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Item'
        db.create_table(u'ps_item', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('id_lista_precio', self.gf('django.db.models.fields.CharField')(max_length=16L)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('codigo_barra', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('id_producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Producto'], max_length=64L, db_column=u'id_producto')),
            ('id_unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Unidad'], max_length=64L, db_column=u'id_unidad')),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Item'])

        # Adding unique constraint on 'Item', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_item', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'ItemPedido'
        db.create_table(u'ps_item_pedido', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('cantidad', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('direccion_entrega', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('monto_impuesto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('monto_total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('flete', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descuento', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('precio_unidad', self.gf('django.db.models.fields.FloatField')()),
            ('porcentaje_impuesto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descuento_negativo', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tipo_descuento', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('id_impuesto', self.gf('django.db.models.fields.CharField')(max_length=64L, null=True, blank=True)),
            ('id_unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Unidad'], max_length=64L, db_column=u'id_unidad')),
            ('id_producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Producto'], max_length=64L, db_column=u'id_producto')),
            ('id_pedido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Pedido'], db_column=u'id_pedido')),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['ItemPedido'])

        # Adding unique constraint on 'ItemPedido', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_item_pedido', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'MetodoPago'
        db.create_table(u'ps_metodo_pago', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('banco', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('monto', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('titular', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('deposito', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['MetodoPago'])

        # Adding unique constraint on 'MetodoPago', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_metodo_pago', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Motivo'
        db.create_table(u'ps_motivo', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('tipo', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Motivo'])

        # Adding unique constraint on 'Motivo', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_motivo', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Pago'
        db.create_table(u'ps_pago', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('id_banco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Banco'], db_column=u'id_banco')),
            ('fecha_documento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('numero_documento', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('titular', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('saldo', self.gf('django.db.models.fields.FloatField')()),
            ('id_cobranza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Cobranza'], db_column=u'id_cobranza')),
            ('id_deposito', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['dbadmin.Deposito'], null=True, db_column=u'id_deposito', blank=True)),
            ('id_metodo_pago', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.MetodoPago'], db_column=u'id_metodo_pago')),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Pago'])

        # Adding unique constraint on 'Pago', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_pago', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Pedido'
        db.create_table(u'ps_pedido', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_entrega', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('orden_de_compra', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('total_bruto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descuento_maestro', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descuento_otro1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descuento_otro2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('sub_total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('impuesto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('otro_impuesto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('flete', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('id_cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Cliente'], db_column=u'id_cliente')),
            ('id_metodo_pago', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.MetodoPago'], db_column=u'id_metodo_pago')),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Pedido'])

        # Adding unique constraint on 'Pedido', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_pedido', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Producto'
        db.create_table(u'ps_producto', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('itemno', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'itemNo')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('precio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cantidad', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('imagen', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=0, max_length=255L, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Producto'])

        # Adding unique constraint on 'Producto', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_producto', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Unidad'
        db.create_table(u'ps_unidad', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('unidad', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Unidad'])

        # Adding unique constraint on 'Unidad', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_unidad', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'Visita'
        db.create_table(u'ps_visita', (
            ('id_surrogate', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'_surrogate_id')),
            ('hora_inicio', self.gf('django.db.models.fields.CharField')(max_length=16L)),
            ('hora_fin', self.gf('django.db.models.fields.CharField')(max_length=16L)),
            ('fecha_reagenda', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('id_motivo_visita', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Motivo'], null=True, db_column=u'id_motivo_visita', blank=True)),
            ('id_motivo_no_visita', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'novisita', null=True, db_column=u'id_motivo_no_visita', to=orm['dbadmin.Motivo'])),
            ('id_motivo_no_cobranza', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'nocobranza', null=True, db_column=u'id_motivo_no_cobranza', to=orm['dbadmin.Motivo'])),
            ('id_motivo_no_pedido', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'nopedido', null=True, db_column=u'id_motivo_no_pedido', to=orm['dbadmin.Motivo'])),
            ('id_cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Cliente'], db_column=u'id_cliente')),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('visitado', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('fecha_modificacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('counter', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'_counter', blank=True)),
            ('field_owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Usuario'], db_column=u'_owner_id')),
            ('field_inst_id', self.gf('django.db.models.fields.CharField')(default=u'backend', max_length=128, db_column=u'_inst_id')),
            ('field_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default=u'admin', to=orm['dbadmin.Grupo'], db_column=u'_group_id')),
            ('field_permissions', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column=u'_permissions')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['Visita'])

        # Adding unique constraint on 'Visita', fields ['field_owner_id', 'field_timestamp_c']
        db.create_unique(u'ps_visita', [u'_owner_id', u'_timestamp_c'])

        # Adding model 'RsGrupoUsuario'
        db.create_table(u'rs_grupo_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Grupo'], db_column=u'nombre')),
            ('username', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Usuario'], db_column=u'username')),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
        ))
        db.send_create_signal(u'dbadmin', ['RsGrupoUsuario'])

        # Adding model 'Usuario'
        db.create_table(u'usuario', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=32L, primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=32L)),
            ('correo', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('field_timestamp_c', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(max_length=22, null=True, db_column=u'_timestamp_c')),
            ('field_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m')),
            ('field_deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'_deleted')),
            ('adminuser', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'dbadmin', ['Usuario'])

        # Adding model 'Secuencia'
        db.create_table(u'dbadmin_secuencia', (
            ('contador', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
        ))
        db.send_create_signal(u'dbadmin', ['Secuencia'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Visita', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_visita', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Unidad', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_unidad', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Producto', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_producto', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Pedido', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_pedido', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Pago', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_pago', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Motivo', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_motivo', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'MetodoPago', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_metodo_pago', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'ItemPedido', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_item_pedido', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Item', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_item', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Direccion', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_direccion', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'DetalleProducto', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_detalle_producto', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Deposito', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_deposito', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'CuentaPorCobrar', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_cuenta_por_cobrar', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Cobranza', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_cobranza', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Cliente', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_cliente', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Categoria', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_categoria', [u'_owner_id', u'_timestamp_c'])

        # Removing unique constraint on 'Banco', fields ['field_owner_id', 'field_timestamp_c']
        db.delete_unique(u'ps_banco', [u'_owner_id', u'_timestamp_c'])

        # Deleting model 'Grupo'
        db.delete_table(u'grupo')

        # Deleting model 'Banco'
        db.delete_table(u'ps_banco')

        # Deleting model 'Categoria'
        db.delete_table(u'ps_categoria')

        # Deleting model 'Cliente'
        db.delete_table(u'ps_cliente')

        # Deleting model 'Cobranza'
        db.delete_table(u'ps_cobranza')

        # Deleting model 'CuentaPorCobrar'
        db.delete_table(u'ps_cuenta_por_cobrar')

        # Deleting model 'Deposito'
        db.delete_table(u'ps_deposito')

        # Deleting model 'DetalleProducto'
        db.delete_table(u'ps_detalle_producto')

        # Deleting model 'Direccion'
        db.delete_table(u'ps_direccion')

        # Deleting model 'Item'
        db.delete_table(u'ps_item')

        # Deleting model 'ItemPedido'
        db.delete_table(u'ps_item_pedido')

        # Deleting model 'MetodoPago'
        db.delete_table(u'ps_metodo_pago')

        # Deleting model 'Motivo'
        db.delete_table(u'ps_motivo')

        # Deleting model 'Pago'
        db.delete_table(u'ps_pago')

        # Deleting model 'Pedido'
        db.delete_table(u'ps_pedido')

        # Deleting model 'Producto'
        db.delete_table(u'ps_producto')

        # Deleting model 'Unidad'
        db.delete_table(u'ps_unidad')

        # Deleting model 'Visita'
        db.delete_table(u'ps_visita')

        # Deleting model 'RsGrupoUsuario'
        db.delete_table(u'rs_grupo_usuario')

        # Deleting model 'Usuario'
        db.delete_table(u'usuario')

        # Deleting model 'Secuencia'
        db.delete_table(u'dbadmin_secuencia')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dbadmin.banco': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Banco', 'db_table': "u'ps_banco'"},
            'counter': ('django.db.models.fields.BigIntegerField', [], {'max_length': '16L', 'db_column': "u'_counter'"}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.categoria': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Categoria', 'db_table': "u'ps_categoria'"},
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_level': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'id_level'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'level': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'parent_id_level': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'parent_id_level'", 'blank': 'True'})
        },
        u'dbadmin.cliente': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Cliente', 'db_table': "u'ps_cliente'"},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'null': 'True'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'descuento_maestro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_otro1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_otro2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'flete': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id_lista_precio': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'identificacion': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'pc_cargo': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'pc_celular': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'pc_correo_electronico': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'pc_fecha_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'pc_nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'pc_telefono': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'telefono1': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'null': 'True', 'blank': 'True'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.cobranza': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Cobranza', 'db_table': "u'ps_cobranza'"},
            'concepto': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_impreso': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_cobrador': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'impreso': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'numero_recibo': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.cuentaporcobrar': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'CuentaPorCobrar', 'db_table': "u'ps_cuenta_por_cobrar'"},
            'cancelada': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'fecha_despacho': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_documento': ('django.db.models.fields.DateField', [], {}),
            'fecha_entrega': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_vencimiento': ('django.db.models.fields.DateField', [], {}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_cobranza': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['dbadmin.Cobranza']", 'null': 'True', 'db_column': "u'id_cobranza'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'monto_original': ('django.db.models.fields.FloatField', [], {}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'procesada': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'saldo_actual': ('django.db.models.fields.FloatField', [], {})
        },
        u'dbadmin.deposito': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Deposito', 'db_table': "u'ps_deposito'"},
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'cuenta': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_banco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Banco']", 'db_column': "u'id_banco'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.detalleproducto': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'DetalleProducto', 'db_table': "u'ps_detalle_producto'"},
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'descripcion_level': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_letter': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'id_level': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_producto': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '64L', 'to': u"orm['dbadmin.Producto']", 'null': 'True', 'db_column': "u'id_producto'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'level': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.direccion': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Direccion', 'db_table': "u'ps_direccion'"},
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'flete': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.grupo': {
            'Meta': {'object_name': 'Grupo', 'db_table': "u'grupo'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '512L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'primary_key': 'True'})
        },
        u'dbadmin.item': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Item', 'db_table': "u'ps_item'"},
            'codigo_barra': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_lista_precio': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'id_producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Producto']", 'max_length': '64L', 'db_column': "u'id_producto'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'id_unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Unidad']", 'max_length': '64L', 'db_column': "u'id_unidad'"}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        u'dbadmin.itempedido': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'ItemPedido', 'db_table': "u'ps_item_pedido'"},
            'cantidad': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'descuento': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_negativo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'direccion_entrega': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'flete': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id_impuesto': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'null': 'True', 'blank': 'True'}),
            'id_pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Pedido']", 'db_column': "u'id_pedido'"}),
            'id_producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Producto']", 'max_length': '64L', 'db_column': "u'id_producto'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'id_unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Unidad']", 'max_length': '64L', 'db_column': "u'id_unidad'"}),
            'monto_impuesto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'monto_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'porcentaje_impuesto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'precio_unidad': ('django.db.models.fields.FloatField', [], {}),
            'tipo_descuento': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.metodopago': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'MetodoPago', 'db_table': "u'ps_metodo_pago'"},
            'banco': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'deposito': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'monto': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'numero': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'titular': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.motivo': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Motivo', 'db_table': "u'ps_motivo'"},
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'tipo': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.pago': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Pago', 'db_table': "u'ps_pago'"},
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'fecha_documento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_banco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Banco']", 'db_column': "u'id_banco'"}),
            'id_cobranza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cobranza']", 'db_column': "u'id_cobranza'"}),
            'id_deposito': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['dbadmin.Deposito']", 'null': 'True', 'db_column': "u'id_deposito'", 'blank': 'True'}),
            'id_metodo_pago': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.MetodoPago']", 'db_column': "u'id_metodo_pago'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'saldo': ('django.db.models.fields.FloatField', [], {}),
            'titular': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.pedido': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Pedido', 'db_table': "u'ps_pedido'"},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'descuento_maestro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_otro1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_otro2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_entrega': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'flete': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_metodo_pago': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.MetodoPago']", 'db_column': "u'id_metodo_pago'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'impuesto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'orden_de_compra': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'otro_impuesto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sub_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_bruto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.producto': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Producto', 'db_table': "u'ps_producto'"},
            'cantidad': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255L', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'imagen': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'itemno': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'itemNo'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'precio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.rsgrupousuario': {
            'Meta': {'object_name': 'RsGrupoUsuario', 'db_table': "u'rs_grupo_usuario'"},
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'nombre'"}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'username'"})
        },
        u'dbadmin.secuencia': {
            'Meta': {'object_name': 'Secuencia'},
            'contador': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'dbadmin.unidad': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Unidad', 'db_table': "u'ps_unidad'"},
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'unidad': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.usuario': {
            'Meta': {'object_name': 'Usuario', 'db_table': "u'usuario'"},
            'adminuser': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '32L'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'primary_key': 'True'})
        },
        u'dbadmin.visita': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Visita', 'db_table': "u'ps_visita'"},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'counter': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'_counter'", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_reagenda': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': "u'backend'", 'max_length': '128', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "u'admin'", 'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'max_length': '22', 'null': 'True', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'hora_fin': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'hora_inicio': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_motivo_no_cobranza': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'nocobranza'", 'null': 'True', 'db_column': "u'id_motivo_no_cobranza'", 'to': u"orm['dbadmin.Motivo']"}),
            'id_motivo_no_pedido': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'nopedido'", 'null': 'True', 'db_column': "u'id_motivo_no_pedido'", 'to': u"orm['dbadmin.Motivo']"}),
            'id_motivo_no_visita': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'novisita'", 'null': 'True', 'db_column': "u'id_motivo_no_visita'", 'to': u"orm['dbadmin.Motivo']"}),
            'id_motivo_visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Motivo']", 'null': 'True', 'db_column': "u'id_motivo_visita'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'visitado': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dbadmin']
