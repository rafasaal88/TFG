from django.contrib import admin
from .models import UserProfile, Company, Publicity_campaign, Product, Recipe, Tag_nfc, Shopping_bag, Register_activity




admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(Publicity_campaign)
admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(Tag_nfc)
admin.site.register(Shopping_bag)
admin.site.register(Register_activity)

# Register your models here.
