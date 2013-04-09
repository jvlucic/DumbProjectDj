'''
Created on Apr 7, 2013

@author: jvlucic
'''
from datetime import date

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from dbadmin.models import Categoria
import json
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models
from django.forms.widgets import DateInput


class DateRangeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        field_name = kwargs.pop('field_name')
        super(DateRangeForm, self).__init__(*args, **kwargs)

#        self.fields['%s__gte' % field_name] = forms.DateField(label='', widget=AdminDateWidget(attrs={'placeholder': _('From date')}), localize=True,required=False)
        self.fields['%s__gte' % field_name] = forms.DateField(label='', widget=DateInput(attrs={'placeholder': _('Desde')  , 'class':'vDateField' }), localize=True,required=False)
        self.fields['%s__lte' % field_name] = forms.DateField(label='', widget=DateInput(attrs={'placeholder': _('Hasta')  , 'class':'vDateField' }), localize=True,required=False)

    class Media:
        js = ("js/grappelli_custom_datepicker_template.js",)

class DateRangeFilter(admin.filters.FieldListFilter):
    template = 'daterange_filter/filterCustom.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg_since = '%s__gte' % field_path
        self.lookup_kwarg_upto = '%s__lte' % field_path
        super(DateRangeFilter, self).__init__(
            field, request, params, model, model_admin, field_path)
        self.form = self.get_form(request)

    def choices(self, cl):
        return []

    def expected_parameters(self):
        return [self.lookup_kwarg_since, self.lookup_kwarg_upto]

    def get_form(self, request):
        return DateRangeForm(data=self.used_parameters,
                             field_name=self.field_path)

    def queryset(self, request, queryset):
        if self.form.is_valid():
            # get no null params
            filter_params = dict(filter(lambda x: bool(x[1]),
                                        self.form.cleaned_data.items()))
            return queryset.filter(**filter_params)
        else:
            return queryset


# register the filter
admin.filters.FieldListFilter.register(
    lambda f: isinstance(f, models.DateField), DateRangeFilter)

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
    
