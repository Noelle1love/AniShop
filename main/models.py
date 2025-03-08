from django.db import models


# Create your models here.
class Main(models.Model):
    site_name = models.CharField(verbose_name="Имя сайта", max_length=50)
    logo = models.ImageField(verbose_name="Логтоип Сайта", upload_to='logo/')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name ='Настройка'
        verbose_name_plural = 'Настройки'

class AboutUs(models.Model):
    photo = models.ImageField(upload_to='about_photo/')
    description = models.TextField("Описание")
    year_in_buisness = models.IntegerField("Лет в бизнесе")
    happy_people = models.IntegerField("Довольных клиентов")
    sales = models.IntegerField("Продаж")
    award_winning = models.IntegerField("Наград")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class Team(models.Model):
    photo = models.ImageField("Фотография", upload_to='team_photo/')
    name = models.CharField("Имя", max_length=50)
    job_title = models.CharField("Должность", max_length=100)
    instagram = models.URLField('Инстаграм', null=True,blank=True)
    facebook = models.URLField('Фейсбук', null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудника"
        verbose_name_plural = "Команда"


class Blog(models.Model):
    title = models.CharField("Заголовок", max_length=400)
    photo = models.ImageField("Фото", upload_to='blog_photo/')
    description = models.TextField("Содержание")
    created_at = models.DateTimeField("Дата публикаций", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class ContactSupport(models.Model):
    coordinates = models.CharField("Координаты",max_length=11)
    hot_line = models.IntegerField("[хот линия")
    email_support = models.EmailField("Имейл помощи")
    email_info = models.EmailField("Инфо-Имейл")

    def __str__(self):
        return self.email_info

    class Meta:
        verbose_name = "Форма"
        verbose_name_plural = "Поддержка"


