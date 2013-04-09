"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'synergy_ventasplus_web_admin.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    title=_('Administrador de Ventas Plus')
        
        
    def init_with_context(self, context):
        site_name = 'Administrador de Ventas Plus'
                
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Entidades para administrar'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib','dbadmin.models.Visita','dbadmin.models.VisitaReschedule','dbadmin.models.VisitaClose'),
        ))
        

        self.children.append(modules.LinkList(
            _('Visitas'),
            column=1,
            children=[
                {
                    'title': _('Agendar Visitas'),
                    'url': '/admin/dbadmin/visita/add/',
                    'external': False,
                },
                {
                    'title': _('Reagendar Visitas'),
                    'url': '/admin/dbadmin/visitareschedule/',
                    'external': False,
                },
                {
                    'title': _('Cerrar Visitas'),
                    'url': '/admin/dbadmin/visitaclose/',
                    'external': False,
                },                                            
            ]
            
        ))


        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


