from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="BlogHome"),
    path('news/', views.news, name="News"),
    path('interview/', views.interview, name="Interviews"),
    path('blog/', views.blog, name="Blog"),
    path('blog/<str:slug>/',views.post ,name="post"),
    path('interview/<str:slug>/',views.intpost,name="intPost"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)