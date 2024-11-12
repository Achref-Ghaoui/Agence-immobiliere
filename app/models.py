from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



# Create your models here.
class Book (models.Model):
    titre=models.CharField(max_length=20)
    description=models.CharField(max_length=400)
    image=models.ImageField(upload_to='photos',null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True, related_name='maisons')

    def __str__(self):
        return self.titre

class MaisonInline(admin.StackedInline):
    model = Book
    extra = 1

class CustomUserAdmin(UserAdmin):
    inlines = (MaisonInline,)
    list_display = UserAdmin.list_display + ('get_maisons',)

    def get_maisons(self, obj):
        return ", ".join([maison.titre for maison in obj.maisons.all()])
    get_maisons.short_description = 'Maisons'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
