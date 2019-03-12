from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    role_admin = 0
    role_teacher = 1
    role_student = 2
    role_manager = 3
    role_choices = (
        (role_admin, 'Админ'),
        (role_teacher, 'Преподаватель'),
        (role_student, 'Студент'),
        (role_manager, 'Менеджер'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.SmallIntegerField('Роль', choices=role_choices, default=role_student)
    system_username = models.CharField('Имя пользователя в системе', max_length=100)

def news_upload_to(instance, filename):
    from os.path import join
    return join('news', str(instance.pk), filename)

class News(models.Model):
    pub_date = models.DateTimeField('Дата публикации', auto_now=False, auto_now_add=False)
    creation_date = models.DateTimeField('Дата создания', auto_now=False, auto_now_add=True)
    text = models.TextField('Текст новости')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.DO_NOTHING)
    title = models.TextField('Заголовок')
    thumbnail = models.ImageField('Превью', upload_to=news_upload_to)
