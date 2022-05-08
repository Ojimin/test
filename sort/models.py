from django.db import models


class fileSystem(models.Model):
    title = models.CharField(max_length=100)  # 길이 제한이 있는 문자열
    size = models.IntegerField(default=0)            # 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True)  # 해당 레코드 생성시 현재 시간 자동

    def __str__(self):
        return self.title
