from modeltranslation.translator import register, TranslationOptions
from .models import Category, Sweets


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('title',)


@register(Sweets)
class SweetsTranslation(TranslationOptions):
    fields = ('title',)
