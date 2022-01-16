from django.db.models import Count

from .models import *
from django.core.cache import cache


menu = [{'title': "Site subject", 'url_name': 'about'},
        {'title': "Add object", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        #{'title': "To come in", 'url_name': 'login'}
]


class DataMixin:
        paginate_by = 3

        def get_user_context(self, **kwargs):
                context = kwargs
                cats = cache.get('cats')
                if not cats:
                        cats = Category.objects.annotate(Count('object'))
                        cache.set('cats', cats, 10)
                cats = Category.objects.all()
                context['menu'] = menu
                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context
