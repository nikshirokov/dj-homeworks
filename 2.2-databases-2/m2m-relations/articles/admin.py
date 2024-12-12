from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif not count:
            raise ValidationError('Укажите основной раздел')
        return super().clean()
        # for form in self.forms:
        #     # В form.cleaned_data будет словарь с данными
        #     # каждой отдельной формы, которые вы можете проверить
        #     form.cleaned_data
        #     # вызовом исключения ValidationError можно указать админке о наличие ошибки
        #     # таким образом объект не будет сохранен,
        #     # а пользователю выведется соответствующее сообщение об ошибке
        #     raise ValidationError('Тут всегда ошибка')
        # return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]


@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    pass
