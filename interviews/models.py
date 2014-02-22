from django.db import models
from django.utils.timezone import now


class Interview(models.Model):
    portrait = models.ImageField(upload_to='media/interviews', blank=True)
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    date = models.DateField()
    question_0 = models.TextField()
    question_1 = models.TextField()
    question_2 = models.TextField()
    question_3 = models.TextField()
    published = models.BooleanField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('interviews_interview_detail', (), {'pk': self.pk})
