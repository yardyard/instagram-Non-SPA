
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.decorators import login_required
from django_pydenticon.views import image as pydenticon_image


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/' , include('accounts.urls')),
    path('insta/', include('insta.urls')), 

    path('', RedirectView.as_view(pattern_name='insta:index'), name='root' ), # re_path를 사용하면 모든 주소에 매칭이 된다.
    path('identicon/images/<path:data>/', pydenticon_image, name='pydenticon_image'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]