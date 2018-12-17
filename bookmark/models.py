from django.db import models
from django.contrib.auth.models import User # 추가


class Bookmark(models.Model):
    # id 필드(Integer, PK, Auto Increment)는 자동 생성됨
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)   # 'url'은 Field.verbose_name(별칭)
    # owner = models.ForeignKey(User, null=True)  # 추가

    def __str__(self):  # 객체를 문자열로 출력할 때 사용하는 함수
        return self.title

