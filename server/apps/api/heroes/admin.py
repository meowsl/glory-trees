from django.contrib import (
    admin,
    messages
)
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
import os
from .models import (
    Heroes,
    Application,
    Archive
)
from .forms import ApplicationAdminForm

@admin.register(Heroes)
class HeroesAdmin(admin.ModelAdmin):
    list_display = (
        "firstname",
        "lastname",
        "event"
    )

@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = (
        "application",
        "reason",
        "status"
    )

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = ('lastname', 'firstname', 'event',)
    list_filter = ('event',)
    search_fields = ('lastname', 'firstname')
    actions = ['approve_applications', 'reject_applications']

    # change_form_template = 'C:/work/meowsl/glory-trees/server/templates/admin/application_change_form.html'
    change_form_template = f'{os.getcwd()}/server/templates/admin/application_change_form.html'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(archive__isnull=True)

    @admin.action(description="Подтвердить все")
    def approve_applications(self, request, queryset):
        for application in queryset:
            hero = Heroes.objects.create(
                lastname=application.lastname,
                firstname=application.firstname,
                midname=application.midname,
                photo=application.photo,
                birthday=application.birthday,
                birth_place=application.birth_place,
                deathdate=application.deathdate,
                grave_place=application.grave_place,
                rank=application.rank,
                feat=application.feat,
                event=application.event,
            )
            archive = Archive.objects.create(
                application=application,
                reason=request.POST.get('reason'),
                status=Archive.ApplicationStatus.APPROVED
            )

            application.save()
            messages.success(request, f'{hero.lastname} {hero.firstname} {hero.midname} was approved.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    @admin.action(description="Отклонить все")
    def reject_applications(self, request, queryset):
        for application in queryset:
            archive = Archive.objects.create(
                application=application,
                reason=request.POST.get('reason'),
                status=Archive.ApplicationStatus.REJECTED
            )
            application.save()
            messages.success(request, f'{application.lastname} {application.firstname} {application.midname} was rejected.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    def response_change(self, request, obj):
        if '_approve' in request.POST:
            hero = Heroes.objects.create(
                lastname=obj.lastname,
                firstname=obj.firstname,
                midname=obj.midname,
                photo=obj.photo,
                birthday=obj.birthday,
                birth_place=obj.birth_place,
                deathdate=obj.deathdate,
                grave_place=obj.grave_place,
                rank=obj.rank,
                feat=obj.feat,
                event=obj.event,
            )
            archive = Archive.objects.create(
                application=obj,
                reason=request.POST.get('reason'),
                status=Archive.ApplicationStatus.APPROVED
            )
            obj.save()
            messages.success(request, f'{hero.lastname} {hero.firstname} {hero.midname} was approved.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif '_reject' in request.POST:
            archive = Archive.objects.create(
                application=obj,
                reason=request.POST.get('reason'),
                status=Archive.ApplicationStatus.REJECTED
            )
            obj.save()
            messages.success(request, f'{obj.lastname} {obj.firstname} {obj.midname} was rejected.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            return super().response_change(request, obj)

    def has_add_permission(self, request):
        return False