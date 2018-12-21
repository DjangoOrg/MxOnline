from django.db import models

# Create your models here.


class Course(models.Model):
    degree_choices = (
        ('cj','初级'),
        ('zj','中级'),
        ('gj','高级'),
    )
    name = models.CharField(max_length=100,verbose_name='课程名称')
    desc = models.CharField(max_length=300,verbose_name='课程描叙')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(max_length=4,choices=degree_choices,default='cj',verbose_name='课程难度')
    learn_times = models.IntegerField(default=0,verbose_name='课程时长')
    students = models.IntegerField(default=0,verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m',max_length=100,verbose_name='封面图片')
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    name = models.CharField(max_length=100,verbose_name='章节名称')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    def __str__(self):
        return '%s<%s>' % (self.name,self.course.name)
    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    def __str__(self):
        return '%s<%s:%s>' % (self.name,self.lesson.course.name,self.lesson.name)
    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='资源名称')
    download = models.FileField(upload_to='courses/resource/%Y/%m',max_length=100,verbose_name='文件')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    def __str__(self):
        return '%s<%s>' % (self.name,self.course.name)
    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name