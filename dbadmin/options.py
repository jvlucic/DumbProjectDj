'''
Created on Apr 10, 2013

@author: jvlucic
'''
import warnings
from django.contrib.admin.options import ModelAdmin, csrf_protect_m
from django.utils.encoding import force_text
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse, Http404
from django.utils.html import escape, escapejs
from django.utils.translation import ugettext as _
from django.contrib.admin import helpers
from django.db import transaction, router
from django.contrib.admin.util import unquote, get_deleted_objects,\
    model_ngettext, flatten_fieldsets
from django.core.exceptions import PermissionDenied
from django.template.response import TemplateResponse
from dbadmin.models import Usuario

def custom_delete_selected(modeladmin, request, queryset):
        """
        Default action which deletes the selected objects.
    
        This action first displays a confirmation page whichs shows all the
        deleteable objects, or, if the user has no permission one of the related
        childs (foreignkeys), a "permission denied" message.
    
        Next, it delets all selected objects and redirects back to the change list.
        """
        opts = modeladmin.model._meta
        app_label = opts.app_label
    
        # Check that the user has delete permission for the actual model
        if not modeladmin.has_delete_permission(request):
            raise PermissionDenied
    
        using = router.db_for_write(modeladmin.model)
    
        # Populate deletable_objects, a data structure of all related objects that
        # will also be deleted.
        deletable_objects, perms_needed, protected = get_deleted_objects(
            queryset, opts, request.user, modeladmin.admin_site, using)
    
        # The user has already confirmed the deletion.
        # Do the deletion and return a None to display the change list view again.
        if request.POST.get('post'):
            if perms_needed:
                raise PermissionDenied
            n = queryset.count()
            if n:
                for obj in queryset:
                    obj_display = force_text(obj)
                    modeladmin.log_deletion(request, obj, obj_display)
                queryset.delete()
                 
                modeladmin.message_user(request, _("Fue(ron) eliminado(s) %(count)d %(items)s(s) satisfactoriamente.") % {
                    "count": n, "items": model_ngettext(modeladmin.opts, n)
                })
                 
            return None

        if len(queryset) == 1:
            objects_name = force_text(opts.verbose_name)
        else:
            objects_name = force_text(opts.verbose_name_plural)
    
        if perms_needed or protected:
            title = _("Cannot delete %(name)s") % {"name": objects_name}
        else:
            title = _("Are you sure?")
    
        context = {
            "title": title,
            "objects_name": objects_name,
            "deletable_objects": [deletable_objects],
            'queryset': queryset,
            "perms_lacking": perms_needed,
            "protected": protected,
            "opts": opts,
            "app_label": app_label,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
            "action_name":'custom_delete_selected',
        }
    
        # Display the confirmation page
        return TemplateResponse(request, modeladmin.delete_selected_confirmation_template or [
            "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()),
            "admin/%s/delete_selected_confirmation.html" % app_label,
            "admin/delete_selected_confirmation.html"
        ], context, current_app=modeladmin.admin_site.name)
    
custom_delete_selected.short_description = _("Eliminar")

class VentasPlusModelAdmin(ModelAdmin):

    dateformat='%d/%m/%Y '
    add_continue_message='The %(name)s "%(obj)s" was added successfully. You may edit it again below.'
    add_another_message='The %(name)s "%(obj)s" was added successfully. You may add another %(name)s below.'
    add_message='The %(name)s "%(obj)s" was added successfully.'
    
    change_continue_message='The %(name)s "%(obj)s" was changed successfully. You may edit it again below.'
    change_saveasnew_message='The %(name)s "%(obj)s" was added successfully. You may edit it again below.'
    change_another_message='The %(name)s "%(obj)s" was changed successfully. You may add another %(name)s below.'
    change_message='The %(name)s "%(obj)s" was added successfully.'
    
    delete_message='The %(name)s "%(obj)s" was deleted successfully.'
    
    msg_dict=None
    change_msg_dict=None
    delete_msg_dict=None
    
    actions= [custom_delete_selected]
    exclude = ('id_surrogate','counter','field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id')

    def save_model(self, request, obj, form, change):
        obj.field_owner_id = Usuario.objects.get(pk=request.user.usuario.username) 
        obj.save()
        
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        if self.exclude:
            excludeList=list(self.exclude)
        else:
            excludeList=['field_owner_id','field_inst_id','field_permissions','field_timestamp_c','field_timestamp_m','field_deleted','field_group_id']

        if self.declared_fieldsets:
            fields=flatten_fieldsets(self.declared_fieldsets)
        else:
            fields=list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))

        return list(set(fields) ^ set(excludeList))
                
    def has_add_permission(self, request):
          
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
        
    
    def get_formsets(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            fs = inline.get_formset(request, obj)
            if obj:
                fs.extra = 0            
            yield fs
    
# Override empty label    
    def get_form(self, request, obj=None, **kwargs):
        form=super(VentasPlusModelAdmin, self).get_form(request)
        for name,field in form.base_fields.iteritems():
            if hasattr(field, 'empty_label'):
                    field.empty_label = u"Seleccione una opci\xF3n"
        return form
            
    def get_actions(self, request):
        actions = super(VentasPlusModelAdmin, self).get_actions(request)
        del actions['delete_selected']
        if not request.user.is_superuser:
            del actions['custom_delete_selected']
        return actions        
        
    def response_add(self, request, obj, post_url_continue=None):
            """
            Determines the HttpResponse for the add_view stage.
            """
            opts = obj._meta
            pk_value = obj._get_pk_val()
            
            if not self.msg_dict:
                msg_dict = {'name': force_text(opts.verbose_name), 'obj': force_text(obj)}
            else:
                msg_dict = self.msg_dict
            
            # Here, we distinguish between different save types by checking for
            # the presence of keys in request.POST.
            if "_continue" in request.POST:
                msg = _(self.add_continue_message) % msg_dict
                self.message_user(request, msg)
                if post_url_continue is None:
                    post_url_continue = reverse('admin:%s_%s_change' %
                                                (opts.app_label, opts.module_name),
                                                args=(pk_value,),
                                                current_app=self.admin_site.name)
                else:
                    try:
                        post_url_continue = post_url_continue % pk_value
                        warnings.warn(
                            "The use of string formats for post_url_continue "
                            "in ModelAdmin.response_add() is deprecated. Provide "
                            "a pre-formatted url instead.",
                            DeprecationWarning, stacklevel=2)
                    except TypeError:
                        pass
                if "_popup" in request.POST:
                    post_url_continue += "?_popup=1"
                return HttpResponseRedirect(post_url_continue)
    
            if "_popup" in request.POST:
                return HttpResponse(
                    '<!DOCTYPE html><html><head><title></title></head><body>'
                    '<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script></body></html>' % \
                    # escape() calls force_text.
                    (escape(pk_value), escapejs(obj)))
            elif "_addanother" in request.POST:
                msg = _(self.add_another_message) % msg_dict
                self.message_user(request, msg)
                return HttpResponseRedirect(request.path)
            else:
#                msg = _('The %(name)s "%(obj)s" was added successfully.') % msg_dict
                msg = _(self.add_message) % msg_dict               
                self.message_user(request, msg)
                return self.response_post_save_add(request, obj)

    def response_change(self, request, obj):
        """
        Determines the HttpResponse for the change_view stage.
        """

                
        opts = self.model._meta

        pk_value = obj._get_pk_val()

        if not self.change_msg_dict:
            msg_dict = {'name': force_text(opts.verbose_name), 'obj': force_text(obj)}
        else:
            msg_dict = self.change_msg_dict
            
        if "_continue" in request.POST:
            msg = _(self.change_continue_message) % msg_dict
            self.message_user(request, msg)
            if "_popup" in request.REQUEST:
                return HttpResponseRedirect(request.path + "?_popup=1")
            else:
                return HttpResponseRedirect(request.path)
        elif "_saveasnew" in request.POST:
            msg = _(self.change_saveasnew_message) % msg_dict
            self.message_user(request, msg)
            return HttpResponseRedirect(reverse('admin:%s_%s_change' %
                                        (opts.app_label, opts.module_name),
                                        args=(pk_value,),
                                        current_app=self.admin_site.name))
        elif "_addanother" in request.POST:
            msg = _(self.change_another_message) % msg_dict
            self.message_user(request, msg)
            return HttpResponseRedirect(reverse('admin:%s_%s_add' %
                                        (opts.app_label, opts.module_name),
                                        current_app=self.admin_site.name))
        else:
            msg = _(self.change_message) % msg_dict
            self.message_user(request, msg)
            return self.response_post_save_change(request, obj)
        
    def response_action(self, request, queryset):
        """
        Handle an admin action. This is called if a request is POSTed to the
        changelist; it returns an HttpResponse if the action was handled, and
        None otherwise.
        """

        # There can be multiple action forms on the page (at the top
        # and bottom of the change list, for example). Get the action
        # whose button was pushed.
        try:
            action_index = int(request.POST.get('index', 0))
        except ValueError:
            action_index = 0

        # Construct the action form.
        data = request.POST.copy()
        data.pop(helpers.ACTION_CHECKBOX_NAME, None)
        data.pop("index", None)

        # Use the action whose button was pushed
        try:
            data.update({'action': data.getlist('action')[action_index]})
        except IndexError:
            # If we didn't get an action from the chosen form that's invalid
            # POST data, so by deleting action it'll fail the validation check
            # below. So no need to do anything here
            pass

        action_form = self.action_form(data, auto_id=None)
        action_form.fields['action'].choices = self.get_action_choices(request)

        # If the form's valid we can handle the action.
        if action_form.is_valid():
            action = action_form.cleaned_data['action']
            select_across = action_form.cleaned_data['select_across']
            func, name, description = self.get_actions(request)[action]

            # Get the list of selected PKs. If nothing's selected, we can't
            # perform an action on it, so bail. Except we want to perform
            # the action explicitly on all objects.
            selected = request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)
            if not selected and not select_across:
                # Reminder that something needs to be selected or nothing will happen
                msg = _("Items must be selected in order to perform "
                        "actions on them. No items have been changed.")
                self.message_user(request, msg)
                return None

            if not select_across:
                # Perform the action only on the selected objects
                queryset = queryset.filter(pk__in=selected)

            response = func(self, request, queryset)

            # Actions may return an HttpResponse, which will be used as the
            # response from the POST. If not, we'll be a good little HTTP
            # citizen and redirect back to the changelist page.
            if isinstance(response, HttpResponse):
                return response
            else:
                return HttpResponseRedirect(request.get_full_path())
        else:
            msg = _("No action selected.")
            self.message_user(request, msg)
            return None
        
    @csrf_protect_m
    @transaction.commit_on_success
    def delete_view(self, request, object_id, extra_context=None):
        "The 'delete' admin view for this model."
        opts = self.model._meta
        app_label = opts.app_label

        if not self.delete_msg_dict:
            msg_dict = {'name': force_text(opts.verbose_name), 'key': escape(object_id)}
        else:
            msg_dict = self.delete_msg_dict
            
        obj = self.get_object(request, unquote(object_id))

        if not self.has_delete_permission(request, obj):
            raise PermissionDenied

        if obj is None:
            raise Http404(_('%(name)s object with primary key %(key)r does not exist.') % msg_dict)

        using = router.db_for_write(self.model)

        # Populate deleted_objects, a data structure of all related objects that
        # will also be deleted.
        (deleted_objects, perms_needed, protected) = get_deleted_objects(
            [obj], opts, request.user, self.admin_site, using)

        if request.POST: # The user has already confirmed the deletion.
            if perms_needed:
                raise PermissionDenied
            obj_display = force_text(obj)
            self.log_deletion(request, obj, obj_display)
            self.delete_model(request, obj)

            self.message_user(request, _(self.delete_message) % {'name': force_text(opts.verbose_name), 'obj': force_text(obj_display)})

            if not self.has_change_permission(request, None):
                return HttpResponseRedirect(reverse('admin:index',
                                                    current_app=self.admin_site.name))
            return HttpResponseRedirect(reverse('admin:%s_%s_changelist' %
                                        (opts.app_label, opts.module_name),
                                        current_app=self.admin_site.name))

        object_name = force_text(opts.verbose_name)

        if perms_needed or protected:
            title = _("Cannot delete %(name)s") % {"name": object_name}
        else:
            title = _("Are you sure?")

        context = {
            "title": title,
            "object_name": object_name,
            "object": obj,
            "deleted_objects": deleted_objects,
            "perms_lacking": perms_needed,
            "protected": protected,
            "opts": opts,
            "app_label": app_label,
        }
        context.update(extra_context or {})

        return TemplateResponse(request, self.delete_confirmation_template or [
            "admin/%s/%s/delete_confirmation.html" % (app_label, opts.object_name.lower()),
            "admin/%s/delete_confirmation.html" % app_label,
            "admin/delete_confirmation.html"
        ], context, current_app=self.admin_site.name)

class VisitaVentasPlusModelAdmin(VentasPlusModelAdmin):
    actions = [custom_delete_selected]
    
        
    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields
                    
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return True