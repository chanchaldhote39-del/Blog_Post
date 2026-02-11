from django.contrib import admin
from .models import Category
from.models import Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)} # kran apn jeva  bolg ver clik kelyver ty bolg chy url ver hit hoil using slug (title) we do not write mnually  (now you type on title slug atomatic write )
    list_display = ['title', 'category','author','status', 'is_featured']
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
