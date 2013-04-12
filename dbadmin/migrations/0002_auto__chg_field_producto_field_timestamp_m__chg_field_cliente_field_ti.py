# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Producto.field_timestamp_m'
        db.alter_column(u'ps_producto', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Cliente.field_timestamp_m'
        db.alter_column(u'ps_cliente', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'RsGrupoUsuario.field_timestamp_m'
        db.alter_column(u'rs_grupo_usuario', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Direccion.field_timestamp_m'
        db.alter_column(u'ps_direccion', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Visita.field_timestamp_m'
        db.alter_column(u'ps_visita', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Cobranza.field_timestamp_m'
        db.alter_column(u'ps_cobranza', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Item.field_timestamp_m'
        db.alter_column(u'ps_item', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'DetalleProducto.field_timestamp_m'
        db.alter_column(u'ps_detalle_producto', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Unidad.field_timestamp_m'
        db.alter_column(u'ps_unidad', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Motivo.field_timestamp_m'
        db.alter_column(u'ps_motivo', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))
        # Adding field 'Categoria.parent_id_level'
        db.add_column(u'ps_categoria', 'parent_id_level',
                      self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'parent_id_level', blank=True),
                      keep_default=False)


        # Changing field 'Categoria.field_timestamp_m'
        db.alter_column(u'ps_categoria', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'ItemPedido.field_timestamp_m'
        db.alter_column(u'ps_item_pedido', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'MetodoPago.field_timestamp_m'
        db.alter_column(u'ps_metodo_pago', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Banco.field_timestamp_m'
        db.alter_column(u'ps_banco', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Pedido.field_timestamp_m'
        db.alter_column(u'ps_pedido', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Zona.field_timestamp_m'
        db.alter_column(u'ps_zona', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Usuario.field_timestamp_m'
        db.alter_column(u'usuario', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Pago.field_timestamp_m'
        db.alter_column(u'ps_pago', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'CuentaPorCobrar.id_cobranza'
        db.alter_column(u'ps_cuenta_por_cobrar', u'id_cobranza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbadmin.Cobranza'], null=True, db_column=u'id_cobranza'))

        # Changing field 'CuentaPorCobrar.field_timestamp_m'
        db.alter_column(u'ps_cuenta_por_cobrar', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'ZonaUsuario.field_timestamp_m'
        db.alter_column(u'ps_zona_usuario', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Grupo.field_timestamp_m'
        db.alter_column(u'grupo', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

        # Changing field 'Deposito.field_timestamp_m'
        db.alter_column(u'ps_deposito', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(db_column=u'_timestamp_m'))

    def backwards(self, orm):

        # Changing field 'Producto.field_timestamp_m'
        db.alter_column(u'ps_producto', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Cliente.field_timestamp_m'
        db.alter_column(u'ps_cliente', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'RsGrupoUsuario.field_timestamp_m'
        db.alter_column(u'rs_grupo_usuario', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Direccion.field_timestamp_m'
        db.alter_column(u'ps_direccion', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Visita.field_timestamp_m'
        db.alter_column(u'ps_visita', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Cobranza.field_timestamp_m'
        db.alter_column(u'ps_cobranza', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Item.field_timestamp_m'
        db.alter_column(u'ps_item', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'DetalleProducto.field_timestamp_m'
        db.alter_column(u'ps_detalle_producto', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Unidad.field_timestamp_m'
        db.alter_column(u'ps_unidad', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Motivo.field_timestamp_m'
        db.alter_column(u'ps_motivo', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))
        # Deleting field 'Categoria.parent_id_level'
        db.delete_column(u'ps_categoria', u'parent_id_level')


        # Changing field 'Categoria.field_timestamp_m'
        db.alter_column(u'ps_categoria', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'ItemPedido.field_timestamp_m'
        db.alter_column(u'ps_item_pedido', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'MetodoPago.field_timestamp_m'
        db.alter_column(u'ps_metodo_pago', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Banco.field_timestamp_m'
        db.alter_column(u'ps_banco', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Pedido.field_timestamp_m'
        db.alter_column(u'ps_pedido', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Zona.field_timestamp_m'
        db.alter_column(u'ps_zona', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Usuario.field_timestamp_m'
        db.alter_column(u'usuario', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Pago.field_timestamp_m'
        db.alter_column(u'ps_pago', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'CuentaPorCobrar.id_cobranza'
        db.alter_column(u'ps_cuenta_por_cobrar', u'id_cobranza', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['dbadmin.Cobranza'], db_column=u'id_cobranza'))

        # Changing field 'CuentaPorCobrar.field_timestamp_m'
        db.alter_column(u'ps_cuenta_por_cobrar', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'ZonaUsuario.field_timestamp_m'
        db.alter_column(u'ps_zona_usuario', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Grupo.field_timestamp_m'
        db.alter_column(u'grupo', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

        # Changing field 'Deposito.field_timestamp_m'
        db.alter_column(u'ps_deposito', u'_timestamp_m', self.gf('synergy_ventasplus_web_admin.model_util.UnixTimestampField')(null=True, db_column=u'_timestamp_m'))

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
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.categoria': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Categoria', 'db_table': "u'ps_categoria'"},
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'id_level'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'parent_id_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'parent_id_level'", 'blank': 'True'})
        },
        u'dbadmin.cliente': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Cliente', 'db_table': "u'ps_cliente'"},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'descuento_maestro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_otro1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_otro2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'flete': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id_lista_precio': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'id_zona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Zona']", 'db_column': "u'id_zona'"}),
            'identificacion': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'pc_cargo': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'pc_celular': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'pc_correo_electronico': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'pc_fecha_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'pc_nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'pc_telefono': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'telefono1': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.cobranza': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Cobranza', 'db_table': "u'ps_cobranza'"},
            'concepto': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_impreso': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_cobrador': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'impreso': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'numero_recibo': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.cuentaporcobrar': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'CuentaPorCobrar', 'db_table': "u'ps_cuenta_por_cobrar'"},
            'cancelada': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_despacho': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_documento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_entrega': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_vencimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_cobranza': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['dbadmin.Cobranza']", 'null': 'True', 'db_column': "u'id_cobranza'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'monto_original': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'procesada': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'saldo_actual': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.deposito': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Deposito', 'db_table': "u'ps_deposito'"},
            'cuenta': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_banco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Banco']", 'db_column': "u'id_banco'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.detalleproducto': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'DetalleProducto', 'db_table': "u'ps_detalle_producto'"},
            'descripcion_level': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_letter': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'id_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_producto': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '64L', 'to': u"orm['dbadmin.Producto']", 'null': 'True', 'db_column': "u'id_producto'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.direccion': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Direccion', 'db_table': "u'ps_direccion'"},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'flete': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.grupo': {
            'Meta': {'object_name': 'Grupo', 'db_table': "u'grupo'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '512L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'primary_key': 'True'})
        },
        u'dbadmin.item': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Item', 'db_table': "u'ps_item'"},
            'codigo_barra': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_lista_precio': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'id_producto': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '64L', 'to': u"orm['dbadmin.Producto']", 'null': 'True', 'db_column': "u'id_producto'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'id_unidad': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '64L', 'to': u"orm['dbadmin.Unidad']", 'null': 'True', 'db_column': "u'id_unidad'", 'blank': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.itempedido': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'ItemPedido', 'db_table': "u'ps_item_pedido'"},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'descuento': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_negativo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'direccion_entrega': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'flete': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id_impuesto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Pedido']", 'null': 'True', 'db_column': "u'id_pedido'", 'blank': 'True'}),
            'id_producto': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '64L', 'to': u"orm['dbadmin.Producto']", 'null': 'True', 'db_column': "u'id_producto'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'id_unidad': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '64L', 'to': u"orm['dbadmin.Unidad']", 'null': 'True', 'db_column': "u'id_unidad'", 'blank': 'True'}),
            'monto_impuesto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'monto_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'porcentaje_impuesto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'precio_unidad': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_descuento': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.metodopago': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'MetodoPago', 'db_table': "u'ps_metodo_pago'"},
            'banco': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'deposito': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'monto': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'numero': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'titular': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.motivo': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Motivo', 'db_table': "u'ps_motivo'"},
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.pago': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Pago', 'db_table': "u'ps_pago'"},
            'fecha_documento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_banco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Banco']", 'db_column': "u'id_banco'"}),
            'id_cobranza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cobranza']", 'db_column': "u'id_cobranza'"}),
            'id_deposito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Deposito']", 'db_column': "u'id_deposito'"}),
            'id_metodo_pago': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'monto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'saldo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'titular': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.pedido': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Pedido', 'db_table': "u'ps_pedido'"},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'descuento_maestro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_otro1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'descuento_otro2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_entrega': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'flete': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_metodo_pago': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.MetodoPago']", 'db_column': "u'id_metodo_pago'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
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
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255L', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'imagen': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'itemno': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'itemNo'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'precio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.rsgrupousuario': {
            'Meta': {'object_name': 'RsGrupoUsuario', 'db_table': "u'rs_grupo_usuario'"},
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'nombre'"}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'username'"})
        },
        u'dbadmin.unidad': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Unidad', 'db_table': "u'ps_unidad'"},
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'unidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.usuario': {
            'Meta': {'object_name': 'Usuario', 'db_table': "u'usuario'"},
            'adminuser': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '32L'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'primary_key': 'True'})
        },
        u'dbadmin.visita': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Visita', 'db_table': "u'ps_visita'"},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_reagenda': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'hora_fin': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'hora_inicio': ('django.db.models.fields.CharField', [], {'max_length': '16L'}),
            'id_cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Cliente']", 'db_column': "u'id_cliente'"}),
            'id_motivo_no_cobranza': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'nocobranza'", 'null': 'True', 'db_column': "u'id_motivo_no_cobranza'", 'to': u"orm['dbadmin.Motivo']"}),
            'id_motivo_no_pedido': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'nopedido'", 'null': 'True', 'db_column': "u'id_motivo_no_pedido'", 'to': u"orm['dbadmin.Motivo']"}),
            'id_motivo_no_visita': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'novisita'", 'null': 'True', 'db_column': "u'id_motivo_no_visita'", 'to': u"orm['dbadmin.Motivo']"}),
            'id_motivo_visita': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Motivo']", 'null': 'True', 'db_column': "u'id_motivo_visita'", 'blank': 'True'}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'visitado': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dbadmin.zona': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'Zona', 'db_table': "u'ps_zona'"},
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'dbadmin.zonausuario': {
            'Meta': {'unique_together': "((u'field_owner_id', u'field_timestamp_c'),)", 'object_name': 'ZonaUsuario', 'db_table': "u'ps_zona_usuario'"},
            'field_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'_deleted'"}),
            'field_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Grupo']", 'db_column': "u'_group_id'"}),
            'field_inst_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'db_column': "u'_inst_id'"}),
            'field_owner_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbadmin.Usuario']", 'db_column': "u'_owner_id'"}),
            'field_permissions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "u'_permissions'"}),
            'field_timestamp_c': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '22', 'db_column': "u'_timestamp_c'"}),
            'field_timestamp_m': ('synergy_ventasplus_web_admin.model_util.UnixTimestampField', [], {'db_column': "u'_timestamp_m'"}),
            'id_surrogate': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'_surrogate_id'"}),
            'id_usuario_app': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dbadmin']