from django.contrib import admin
from food.models import Item

# Register your models here.
admin.site.site_header = "Foodie's Favourite Administration"
admin.site.site_title = "Foodie's Favourite Administration"
admin.site.index_title = "Manage Foodie's Favourite"

class ItemAdmin(admin.ModelAdmin):
    def img_desc_to_default(self,request,queryset):
        queryset.update(item_desc='default')

    img_desc_to_default.short_description = 'Image_default'
    list_display = ('item_name','user_name','item_desc','item_price')
    search_fields = ('item_name',)
    actions = (img_desc_to_default,)
    fields = ('item_name','user_name',)
    list_editable = ('item_price',)


admin.site.register(Item,ItemAdmin)
