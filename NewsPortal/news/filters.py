from django_filters import FilterSet, CharFilter, RangeFilter, DateFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = ('author', 'categoryType', 'title', 'text')