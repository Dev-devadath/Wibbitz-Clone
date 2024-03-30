from django.contrib import admin
from web.models import Subscribe, Customers, Features, VideoBlog, Testimonial, MarketingFeatures, Product, Blog, Contact


admin.site.register(Subscribe)


class CustomersAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]

admin.site.register(Customers, CustomersAdmin)


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "testimonial_author", "author_designation", "description"]


admin.site.register(Features, FeaturesAdmin)


admin.site.register(VideoBlog)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "company_name", "is_featured"]


admin.site.register(Testimonial, TestimonialAdmin)


class MarketingFeaturesAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]


admin.site.register(MarketingFeatures, MarketingFeaturesAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"] 


admin.site.register(Product, ProductAdmin)


admin.site.register(Blog)
admin.site.register(Contact)