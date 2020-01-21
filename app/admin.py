from django.contrib import admin

# Register your models here.
from app.models import Employee, Project, Status, Level, Company, Ticket, CompanyProject


class CompanyProjectInlineAdmin(admin.StackedInline):
    model = CompanyProject
    # permet de rechercher le tag dans champs de recherche
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = (CompanyProjectInlineAdmin, )


admin.site.register(Employee)
admin.site.register(Ticket)
admin.site.register(Company)
admin.site.register(Level)
admin.site.register(Status)
admin.site.register(Project, ProjectAdmin)

