from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Relationship, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        if not len([form for form in self.forms if form.cleaned_data.get('is_main')]) == 1:
            raise ValidationError('Основной раздел должен быть один!')
        else:
            return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Scope)
class ObjectAdmin(admin.ModelAdmin):
    pass
