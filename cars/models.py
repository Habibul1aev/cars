from django.db import models

class Category(models.Model):
    class Mate:
        verbose_name = 'Категория'
        verbose_name_populer = 'Категории'

    name_category = models.CharField(max_length = 10, verbose_name = 'Марка')

    def __str__(self):  
        return f'{self.id}) {self.name_category}'


class Cars(models.Model):

    class Mate:
        verbose_name = 'Маркa'
        verbose_name_populer = 'Марки'
        

    name = models.CharField(max_length = 50, verbose_name = 'Марка')
    photo = models.ImageField(verbose_name='Фото', upload_to='imgs/')
    volume = models.CharField(max_length = 3, verbose_name = 'Объем')
    model = models.CharField(max_length = 20, verbose_name = 'Модель')
    info = models.TextField(verbose_name = 'Информация')
    data = models.DateField(verbose_name = 'Дата создания', auto_now_add = True)
    updata = models.DateField(verbose_name = 'Изменить дату', auto_now = True)
    price = models.CharField(max_length = 12,verbose_name = 'Цена')
    category = models.ForeignKey('Category', on_delete = models.PROTECT, related_name='cars', verbose_name='категория')
    teg = models.ManyToManyField('cars.Hesh', related_name='cars', verbose_name='теги', blank=True)
    views = models.IntegerField(default=0, verbose_name = 'Просмотры')
    is_publish = models.BooleanField(verbose_name = 'публикация', default = True)

    
    def __str__(self):
        return f'{self.id}) {self.name}'
    

class Hesh(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    name = models.CharField(max_length=100, verbose_name='название')
    
    def __str__(self):
        return self.name


class NetWorkLink(models.Model):

    cars = models.OneToOneField('cars.Cars', on_delete=models.CASCADE, related_name='link')
    name= models.CharField(max_length = 30,verbose_name = 'название')
    name_link = models.CharField(max_length = 40, verbose_name = 'ссылка')
    

    def __str__(self):
        return self.name