from django.urls import path
from blog.views import *
from django.conf.urls.static import static

urlpatterns = [
                  path('home/', home, name='home'),
                  path('categries/', show_all_categories, name='categories'),
                  path('posts/', show_posts, name='posts'),
                  path('single_post/<slug:pk>', single_post, name='post'),
                  path('cat_posts/<str:category>', cat_posts, name='category')
            ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
