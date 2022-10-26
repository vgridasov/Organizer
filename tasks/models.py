from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class TaskStatus(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name="Статус")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['id']


# ------- user profile block
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=50, verbose_name="Отчество", blank=True)
    fio = models.CharField(max_length=50, verbose_name="Фамилия, Инициалы")
    company = models.CharField(max_length=50, verbose_name="Организация", blank=True)
    department = models.CharField(max_length=50, verbose_name="Подразделение", blank=True)
    position = models.CharField(max_length=50, verbose_name="Должность", blank=True)
    location = models.CharField(max_length=50, verbose_name="Местоположение", blank=True)
    phone = models.CharField(max_length=50, verbose_name="Телефон", blank=True)
    email = models.EmailField(max_length=50, verbose_name="E-mail", blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", )

    def __str__(self):
        return '%s %s' % (self.id, self.fio)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# ------- end user profile block


class Task(models.Model):
    task_name = models.CharField(max_length=200, verbose_name="Задача")
    task_from = models.CharField(max_length=200, verbose_name="Источник")
    task_description = models.TextField(verbose_name="Описание", blank=True)
    task_status = models.ForeignKey(TaskStatus, on_delete=models.SET_NULL, blank=True, null=True)
    task_assign_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_ended = models.BooleanField(default=True, verbose_name="Завершена")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_id': self.pk})

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
