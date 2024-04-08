from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Category,SongiYangiliklar,Voqealar
from django.contrib import admin



# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['nom',"slug",'chopetilishVaqti','holati']
#     list_filter = ['nom','chopetilishVaqti','holati']
#     prepopulated_fields = {"slug":('nom',)}
#     search_fields = ['nom','kontent']
#     date_hierarchy = 'chopetilishVaqti'
#     ordering = ['holati','chopetilishVaqti']
@admin.register(SongiYangiliklar)
class SongiyangiliklarAdmin(admin.ModelAdmin):
    list_display = ['nom',"slug",'chopetilishVaqti','holati']
    list_filter = ['nom','chopetilishVaqti','holati']
    prepopulated_fields = {"slug":('nom',)}
    search_fields = ['nom','kontent']
    date_hierarchy = 'chopetilishVaqti'
    ordering = ['holati','chopetilishVaqti']
@admin.register(Voqealar)
class VoqealarAdmin(admin.ModelAdmin):
    list_display = ['nom',"slug",'chopetilishVaqti','holati']
    list_filter = ['nom','chopetilishVaqti','holati']
    prepopulated_fields = {"slug":('nom',)}
    search_fields = ['nom','kontent']
    date_hierarchy = 'chopetilishVaqti'
    ordering = ['holati','chopetilishVaqti']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi']
# @admin.register(yangilik_video)
# class yangilik_video_Admin(admin.ModelAdmin):
#     list_display = ['nom']
#     list_filter = ['nom', 'chopetilishVaqti']
#     date_hierarchy = 'chopetilishVaqti'
# @admin.register(yangilikDetel)
# class yangilikdetelAdmin(admin.ModelAdmin):
#     list_display = ['nom']
#     list_filter = ['nom', 'chopetilishVaqti']
#     date_hierarchy = 'chopetilishVaqti'

# @admin.register(Comments)
# class commentsAdmin(admin.ModelAdmin):
#     list_display = ['user','news','body','active']
#     list_filter = ['active', 'user']
#     search_fields = ["body"]
#     actions = ["ochiribtashlash","active_comments"]
#
#     def ochiribtashlash(self,request,queryset):
#         queryset.update(active=False)
#
#     def active_comments(self,request,queryset):
#         queryset.update(active=True)