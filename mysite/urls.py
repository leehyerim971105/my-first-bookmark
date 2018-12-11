from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView
# 회원 가입 처리 뷰 임포트
from mysite.views import UserCreateView, UserCreateDoneTV         # ch11 1/2

urlpatterns = [
  url(r'^admin/', include(admin.site.urls)),
  # 아래 인증 관련 3행 추가                                        # ch11 2/2
  # 장고 인증 URLconf를 인클루드하여 활용하는데,
  #   여기에 정의된 /login, /logout 등이
  #   실제로는 /accounts/login, /accounts/logout 등으로 처리됨
  url(r'^accounts/', include('django.contrib.auth.urls')),
  # 계정 가입 처리하는 URL
  url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
  # 계정 가입 완료될 때 보여줄 URL
  url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

  url(r'^$', HomeView.as_view(), name='home'),
  url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
  url(r'^blog/', include('blog.urls', namespace='blog')),
  url(r'^photo/', include('photo.urls', namespace='photo')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
