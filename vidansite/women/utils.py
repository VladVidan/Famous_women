from .models import *
from django.db.models import Count
from django.core.cache import cache

menu = [{'title': 'Про сайт', 'url_name': 'about'},
        {'title': 'Додати статтю', 'url_name': 'add_page'},
        {'title': "Зворотній зв'язок", 'url_name': 'contact'},
        ]


class DataMixin:
    """Mixin class for views.py classes"""
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('women'))
            cache.set('cats', cats, 60)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context