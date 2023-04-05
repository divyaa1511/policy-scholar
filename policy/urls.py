from django.urls import path
from . import views
from .views import PostListView ,PostCreateView ,PostUpdateView ,PostDeleteView 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    # path('RecommandationsView',views.RecommandationsView.as_view(),name='RecommandationsView'),
    path('social/',views.social,name='social'),
    path('sciTech/',views.sciTech,name='sciTech'),
    path('environment/',views.environment,name='environment'),
    path('economic/',views.economic,name='economic'),
    path('foreign/',views.foreign,name='foreign'),
    path('other/',views.other,name='other'),

    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('',PostListView.as_view(),name='post-home'),

    path('post/new',PostCreateView.as_view(),name='post-new'),

path('post/<int:pk>/',views.PostDetail,name='post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),

    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)