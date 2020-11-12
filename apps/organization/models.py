
from django.db import models
from datetime import datetime
# Create your models here.

# CityDict        城市信息
class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name='城市')
    desc = models.CharField(max_length=200,verbose_name='描述')
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


#CourseOrg  课程机构基本信息
class CourseOrg(models.Model):
    ORG_CHOICES = (
        ("pxjg",'培训机构'),
        ('gx','高校'),
        ('gr','个人')
    )
    name = models.CharField(max_length=50,verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    category = models.CharField(max_length=20,choices=ORG_CHOICES,default="pxjg",verbose_name='机构类别')
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    students = models.IntegerField(default=0,verbose_name="学习人数")
    course_nums = models.IntegerField(default=0,verbose_name='课程数')
    image = models.ImageField(upload_to='org/%Y/%m',max_length=100,verbose_name='封面图')
    address = models.CharField(max_length=150,verbose_name='机构地址')
    city = models.ForeignKey(CityDict,verbose_name='所在城市',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 获取机构的教师数
        return self.teacher_set.all().count()


# Teacher       教师基本信息
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name='所属机构',on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name='教师名')
    work_years = models.IntegerField(default=0,verbose_name='工作年限')
    work_company = models.CharField(max_length=50,verbose_name='就职公司')
    work_position = models.CharField(max_length=50,verbose_name='公司职位')
    points = models.CharField(max_length=50,verbose_name='教学特点')
    click_nums= models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    image = models.ImageField(default='',upload_to="teacher/%Y/%m",verbose_name="头像",max_length=100)
    add_time = models.DateTimeField(default=datetime.now)
    teacher_age = models.IntegerField('年龄', default=25)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[{0}]的教师：{1}'.format(self.org,self.name)

    def get_course_nums(self):
        return self.course_set.all().count()

