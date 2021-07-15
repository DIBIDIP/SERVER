from django.contrib import admin
from django.utils.html import mark_safe
from . import models




class PhotoInline(admin.TabularInline):
    model = models.Photo

    
@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):

    """ RoomAdmin Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info: 기본정보 작성해주세요",
            {
                "fields": (
                    "name",
                    "price",
                    "description",
                )
            },
        ),
        (
            "nutrients information: 영양성분 작성",
            {
                "fields": ( 
                    "kcal",
                    "size",
                    "carbohydrate",
                    "sugars",
                    "protain",
                    "fat",
                    "saturated_Fat",
                    "trans_Fat",
                    "cholesterol",
                    "sodium",
                )
            },

        ),

        (
            "알러지 사항 선택",
            {"fields": ("allergies",)},
        ),


        (
            "원재료 작성",
            {"fields": ("ingredients",)},
        ),
    )

    # Home > Menus > menus에 보일 것들
    list_display = (
        "name",
        "price",
        "kcal"
    )

    # Home > Menus > menus에서 우측 필터
    #list_filter = (
    #    "allergies",
    #)

    
    #filter_horizontal = ("allergies", "ingredients",)



    def count_menus(self, obj):
        return obj.menus.count()

    count_menus.short_description = "Menus Count"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"



@admin.register(models.Ingredient, models.Allergy )
class ItemAdmin(admin.ModelAdmin):

    """ Itrem Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj) :
        return obj.menus.count()
    used_by.short_description= "첨가된 메뉴 수"

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    list_display = ('__str__', 'get_thumbnail' )
    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')
    get_thumbnail.short_description = "Thumnail"