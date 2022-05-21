from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from cake.models import Category, Sweets, Feedback, Subscription, Order


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass


@admin.register(Sweets)
class SweetsAdmin(TranslationAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'messages')
