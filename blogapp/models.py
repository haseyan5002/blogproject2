from django.db import models

# Create your models here.
class Category(models.Model):
    #カテゴリのフィールド
    title = models.CharField(
        verbose_name = "カテゴリ",
        max_length = 50)

    def __str__(self):
        return self.title

class NewsPost(models.Model):
    CATEGORY = (('domestic', '国内'),
                ('intl', '国際'),
                ('politics', '政治'),
                ('economy', '経済'),
                ('sport', 'スポーツ'),
                )

    #タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    #本文用のフィールド
    content = models.TextField(
        verbose_name = "本文"
        )
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name = "投稿日時",
        auto_now_add = True
        )
    #カテゴリのフィールド
    category = models.CharField(
        verbose_name = "カテゴリ",
        max_length = 50,
        choices = CATEGORY
        )

    def __str__(self):
        return self.title

# class Favorite(models.Model):
#     news = models.ForeignKey(NewsPost, on_delete=models.CASCADE)