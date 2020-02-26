from django.contrib import admin
from Web.models import retele_de_socializare_utilizator
# Register your models here.

class retele_de_socializare_utilizatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'github', 'facebook', 'instagram', 'gmail', 'youtube', 'linkedin', 'discord', 'skype', 'steam', 'paypal')

admin.site.register(retele_de_socializare_utilizator, retele_de_socializare_utilizatorAdmin)