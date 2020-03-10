from django.contrib import admin
from .models import UserProfile, Publicity_campaign, Product, Recipe, Tag_nfc, Shopping_bag, Register_activity, Product_history, Point



admin.site.register(Publicity_campaign)
admin.site.register(UserProfile)

admin.site.register(Product)
admin.site.register(Product_history)
admin.site.register(Recipe)
admin.site.register(Tag_nfc)
admin.site.register(Shopping_bag)
admin.site.register(Register_activity)
admin.site.register(Point)

# Register your models here.
