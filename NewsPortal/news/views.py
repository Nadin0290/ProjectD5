from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from .filters import PostFilter
from .models import Post, Category
from datetime import datetime
from .forms import PostForm # Импортируем нашу форму
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PostList(ListView):
    model = Post # Указываем модель (сущность в таблице базы данных) которую нужно вывести
    template_name = 'flatpages/news.html' # Путь к html-фалу с инструкциями вывода пользователю этих объектов
    context_object_name = 'news' # Указываем на имя списка, в котором лежат все объекты для html-шаблона
    queryset = Post.objects.order_by('-dateCreation') # Переопределяем все новости от новых к старым
    paginate_by = 10
    form_class = PostForm # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class PostDetailView(DetailView):
    template_name = 'flatpages/post_detail.html' # Путь к html-файлу с инструкциями вывода деталей модели (сущности)
    context_object_name = 'post'
    queryset = Post.objects.all()


class PostSearch(PostList):
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    queryset = Post.objects.all()
    paginate_by = 1


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'flatpages/post_create.html'
    context_object_name = 'post_create'
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'flatpages/post_update.html'
    form_class = PostForm

    def get_object(self, **kwargs): # Вместо queryset, чтобы получить информацию о редактируемом объекте
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView): # Дженерик для удаления новости
    template_name = 'flatpages/post_delete.html'
    context_object_name = 'post'
    queryset = Post.objects.all()
    success_url = '/news/'
