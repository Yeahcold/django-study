from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name = "작성일시", auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name = "수정일시", auto_now = True)

    class Meta:
        abstract = True


class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
    
class Post(BaseModel):

    CHOICES = (
        ('DIARY', '일기'),
        ('STUDY', '공부'),
        ('ETC', '기타')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name = "제목", max_length = 20)
    content = models.TextField(verbose_name="내용")
    writer = models.CharField(verbose_name = "작성자", max_length = 10)
    category = models.CharField(choices = CHOICES, max_length = 20)
    hashtag = models.ManyToManyField(Hashtag, blank= True)

class Comment(BaseModel):
    id = models.AutoField(primary_key= True)
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, default = '')
    content = models.TextField(verbose_name= "내용")
    writer = models.CharField(verbose_name= "작성자", max_length= 20)


