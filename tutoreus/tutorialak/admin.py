from tutoreus.tutorialak.models import Tutoriala, Gaia, Zailtasuna
from django.contrib import admin
from tutoreus.tutorialak.forms import TutorialAdminForm

from datetime import datetime
from django.utils import timezone

class TutoAdmin(admin.ModelAdmin):
    list_display = ('izenburua', 'slug','zailtasuna', 'aplikazioa','pub_date', 'erabiltzailea','publikoa_da')
    prepopulated_fields = {"slug": ("izenburua",)}
    form = TutorialAdminForm
    
class GaiaAdmin(admin.ModelAdmin):
    list_display = ('izena','slug')
    prepopulated_fields = {"slug": ("izena",)}
    
class ZailtasunAdmin(admin.ModelAdmin):
    list_display = ('izena',)

admin.site.register(Tutoriala, TutoAdmin)
admin.site.register(Gaia, GaiaAdmin)
admin.site.register(Zailtasuna, ZailtasunAdmin)
