from django.contrib import admin

# Register your models here.
from app.models import User, Project, Status, Level, Company, Ticket, Role, CompanyProject


class CompanyProjectInlineAdmin(admin.StackedInline):
    model = CompanyProject
    # permet de rechercher le tag dans champs de recherche
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = (CompanyProjectInlineAdmin, )


admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Company)
admin.site.register(Level)
admin.site.register(Role)
admin.site.register(Status)
admin.site.register(Project, ProjectAdmin)

