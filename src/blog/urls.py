from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('blog/', views.blog_page, name='blog_page'),
    path('<slug:slug>/', views.article_view, name='article'),
    path('category/<slug:category_slug>/', views.category_page, name='category'),
    path('<slug:slug>/', views.post_detail, name='post_detail')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
