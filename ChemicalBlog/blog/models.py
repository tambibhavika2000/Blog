from django.db import models

# Create your models here.
class Articles(models.Model):
    article_id=models.AutoField
    article_title=models.CharField(max_length=500)
    article_by=models.CharField(max_length=50000,default="",blank=True)
    head1 = models.CharField(max_length=500, default="", blank=True)
    para1 = models.CharField(max_length=50000, default="", blank=True)
    head2 = models.CharField(max_length=500, default="", blank=True)
    para2 = models.CharField(max_length=50000, default="", blank=True)
    head3 = models.CharField(max_length=50000, default="", blank=True)
    para3 = models.CharField(max_length=50000, default="", blank=True)
    head4 = models.CharField(max_length=500, default="", blank=True)
    para4 = models.CharField(max_length=50000, default="", blank=True)
    pub_date = models.DateField()
    image1 = models.ImageField(upload_to='assets', default="", blank=True)
    image2 = models.ImageField(upload_to='assets', default="", blank=True)
    image3 = models.ImageField(upload_to='assets', default="", blank=True)
    image4 = models.ImageField(upload_to='assets', default="", blank=True)
    other=models.CharField(max_length=50000,default="",blank=True)

    def __str__(self):
        return self.article_title

class News(models.Model):
    news_id=models.AutoField
    news_title=models.CharField(max_length=500)
    head1 = models.CharField(max_length=500,default="",blank=True)
    para1 = models.CharField(max_length=50000,default="",blank=True)
    head2 = models.CharField(max_length=500,default="",blank=True)
    para2 = models.CharField(max_length=50000,default="",blank=True)
    head3 = models.CharField(max_length=50000,default="",blank=True)
    para3 = models.CharField(max_length=50000,default="",blank=True)
    head4 = models.CharField(max_length=500,default="",blank=True)
    para4 = models.CharField(max_length=50000,default="",blank=True)
    pub_date=models.DateField()
    image1=models.ImageField(upload_to='blog/assets', default="",blank=True)
    image2 = models.ImageField(upload_to='blog/assets', default="",blank=True)
    image3 = models.ImageField(upload_to='blog/assets', default="",blank=True)
    image4 = models.ImageField(upload_to='blog/assets', default="",blank=True)
    other=models.CharField(max_length=50000,default="",blank=True)

    def __str__(self):
        return self.news_title

class Interview(models.Model):
    interview_id=models.AutoField
    interview_title=models.CharField(max_length=500)
    person=models.CharField(max_length=50000,default="",blank=True)
    clg = models.CharField(max_length=50000, default="", blank=True)
    position=models.CharField(max_length=20)
    head1 = models.CharField(max_length=500,default="",blank=True)
    para1 = models.CharField(max_length=50000,default="",blank=True)
    head2 = models.CharField(max_length=500,default="",blank=True)
    para2 = models.CharField(max_length=50000,default="",blank=True)
    head3 = models.CharField(max_length=50000,default="",blank=True)
    para3 = models.CharField(max_length=50000,default="",blank=True)
    head4 = models.CharField(max_length=500,default="",blank=True)
    para4 = models.CharField(max_length=50000,default="",blank=True)
    pub_date=models.DateField()
    image1=models.ImageField(upload_to='blog/assets', default="",blank=True)
    image2 = models.ImageField(upload_to='blog/assets', default="",blank=True)
    image3 = models.ImageField(upload_to='blog/assets', default="",blank=True)
    image4 = models.ImageField(upload_to='blog/assets', default="",blank=True)
    other=models.CharField(max_length=50000,default="",blank=True)

    def __str__(self):
        return self.interview_title