from django.db import models


'''class Categories(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
        category_id = models.CharField(Categories, on_delete=models.CASCADE)
        '''


class Dishes(models.Model):
    objects = None
    nameofdishes = models.CharField('Название', max_length=100, null=True)
    description = models.TextField()
    howTOcook = models.TextField()


    def __str__(self): #вывод объекта класса на экран
        return self.nameofdishes
