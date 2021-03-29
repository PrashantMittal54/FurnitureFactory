from django.contrib import admin

from restoration.apps.furniture.models import Legs, Feet, Tables


class LegsAdmin(admin.ModelAdmin):
    fieldsets = [
        # Basic Information
        ("Leg Info", {
            'fields':
                [
                    ('name',),
                    ('size', 'created_ts'),
                ],
        }),
    ]

    search_fields = ('id', 'name')
    list_display = ('id', 'name', 'size', 'created_ts')
    readonly_fields = ('created_ts', )


class FeetAdmin(admin.ModelAdmin):
    fieldsets = [
        # Basic Information
        ("Feet Info", {
            'fields':
                [
                    ('name', 'radius',),
                    ('length', 'width', 'created_ts'),
                ],
        }),
    ]

    search_fields = ('id', 'name', 'width', 'length', 'radius',)
    list_display = ('id', 'name', 'width', 'length', 'radius', 'created_ts')
    readonly_fields = ('created_ts', )


class TableAdmin(admin.ModelAdmin):
    fieldsets = [
        # Basic Information
        ("table Info", {
            'fields':
                [
                    ('name',),
                    ('legs', 'leg_count',),
                    ('feet', 'feet_count',),
                    ('created_ts',),
                ],
        }),
    ]

    search_fields = ('id', 'name',)
    list_display = ('id', 'name', 'legs', 'feet', 'created_ts')
    readonly_fields = ('created_ts', 'updated_ts')


admin.site.register(Legs, LegsAdmin)
admin.site.register(Feet, FeetAdmin)
admin.site.register(Tables, TableAdmin)
