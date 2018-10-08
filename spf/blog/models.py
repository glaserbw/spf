from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=280)
    subhead = models.CharField(max_length=140)
    pub_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    cover_url = models.TextField() # Cover image for the article 
    tags = models.ManyToManyField('Tag', blank=True, through='ArticleTag')

    def __str__(self):
        return self.title

class Tag(models.Model):
    articles = models.ManyToManyField('Article', blank=False, through='ArticleTag')
    tag = models.CharField(max_length=140, default='All')

    def __str__(self):
        return self.tag

# Relational join table to connect Article + Tag
class ArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


# Photo class to define that one article can have many photos 
class Photo(models.Model):
    photo = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='photos')
    photo_urls = models.TextField(max_length=240)
    caption = models.CharField(max_length=240)

    def __str__(self):
        return self.photo_urls



