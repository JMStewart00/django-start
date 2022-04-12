from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    difficulty = models.IntegerField(default=1, blank=False, null=False)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    recipe = models.ManyToManyField(Recipe)

    def starts_with_c(self):
        return self.name[0] == 'C'

    def __str__(self):
        return self.name
