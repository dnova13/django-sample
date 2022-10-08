import uuid
from django.db import models
from core import models as core_models
from django.core.exceptions import ValidationError


class files(core_models.TimeStampedModel):

    """Files Model Definition"""

    class Meta:
        verbose_name = "files"

    file_name = models.CharField(
        verbose_name='파일 이름',
        max_length=100,
        null=True,
    )
    uuid = models.UUIDField(
        verbose_name='파일 uuid',
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    mime_type = models.CharField(
        verbose_name='파일 이름',
        max_length=100,
        null=True,
    )
    file_type = models.IntegerField(
        verbose_name='파일 타입',
        null=True,
        choices=(
            (0, "이미지"),
            (1, "일반 파일"),
        )
    )
    size = models.IntegerField(
        verbose_name='파일 사이즈',
        null=True,
    )
    path = models.FileField(
        verbose_name='파일 경로',
        upload_to=""
    )
    duration = models.BigIntegerField(
        verbose_name='영상 길이',
        default=0
    )
