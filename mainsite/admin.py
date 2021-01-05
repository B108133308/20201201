from django.contrib import admin
from mainsite.models import Post, AccessInfo, Branch, StoreIncome, text1, City, Keep

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
admin.site.register(Branch, BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch', 'income_year',
    'income_month', 'income')

admin.site.register(StoreIncome, StoreIncomeAdmin)

class text1Admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(text1, text1Admin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('cityname', 'cityleader')
admin.site.register(City, CityAdmin)

class KeepAdmin(admin.ModelAdmin):
    list_display = ('city', 'keep_year', 'keep_num')
admin.site.register(Keep, KeepAdmin)