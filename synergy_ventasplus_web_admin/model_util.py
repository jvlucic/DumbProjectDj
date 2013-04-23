from django.db import models
from datetime import datetime
from time import strftime
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^synergy_ventasplus_web_admin\.model_util\.UnixTimestampField"])
#
# Custom field types in here.
#

class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """
    def __init__(self, null=False, blank=False, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to
        # cheat a little:
        self.blank, self.isnull = blank, null
        if null:
            self.null = True # To prevent the framework from shoving in "not null".
        else:
            self.null = False
            
    def db_type(self, connection):
        typ=['TIMESTAMP']
        # See above!
        if self.isnull:
            typ += ['NULL']
        else:
            typ += ['NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        if self.auto_created:
            typ += ['NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value==None:
            return None
        if hasattr(value, 'timetuple'):
            return strftime('%Y%m%d%H%M%S',value.timetuple())

        return value

    def to_python(self, value):
        return value