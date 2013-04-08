'''
Created on Apr 7, 2013

@author: jvlucic
'''
from datetime import date

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from dbadmin.models import Categoria
import json

class ProductTreeListFilter(SimpleListFilter):

    title = _('Categoria')
    parameter_name = 'categoria'
    level=0
    basefilterConfigData =  [
                              {'title':_('Categoria'), 'parameter_name':'categoria', 'level':1},
                              {'title':_('Tipo'), 'parameter_name':'tipo', 'level':2},
                              {'title':_('Linea'), 'parameter_name':'linea', 'level':3},
                              {'title':_('Calidad'), 'parameter_name':'calidad', 'level':4},
                              {'title':_('Tamano'), 'parameter_name':'tamano', 'level':5},
                              {'title':_('Color'), 'parameter_name':'color', 'level':6},                          
                            ]
    
                
    def config(self,configData):
        self.title=configData['title']
        self.parameter_name=configData['parameter_name']
        self.level=configData['level']

    def lookups(self, request, model_admin):
        if model_admin.filterConfigData: 
            self.config(model_admin.filterConfigData.pop(0))
        else:
            model_admin.filterConfigData=self.basefilterConfigData[:]
            self.config(model_admin.filterConfigData.pop(0))

        choices=[ ( json.dumps({'id_level':o.id_level, 'level':o.level}) , str(o)) for o in Categoria.objects.filter(level=self.level)]
        return choices

    def queryset(self, request, queryset):
        if self.value() is not None:
            c=json.loads(self.value())
            return queryset.filter(detalleproducto__id_level=c['id_level'],detalleproducto__level=c['level'])    
        return queryset
    
