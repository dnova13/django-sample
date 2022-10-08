
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    avatar = models.ForeignKey(
        verbose_name='아바타 그림파일',
        to='file.Files',
        on_delete=models.SET_NULL,
        null=True,
        related_name='avatar',
    )
    nickname = models.CharField(
        max_length=100,
        verbose_name='닉네임',
        null=True,
    )
    phone_number = models.CharField(
        verbose_name='폰 번호',
        max_length=15,
        null=True,
        blank=True,
    )
    level = models.IntegerField(
        verbose_name='회원 레벨',
        default=False,
        choices=(
            (1, '일반 회원'),
            (101, '판매자'),
            (256, '슈퍼관리자'),
        ),
    )
    modify_at = models.DateTimeField(
        auto_now=True
    )
    remove_at = models.DateTimeField(
        null=True,
        blank=True,
    )
