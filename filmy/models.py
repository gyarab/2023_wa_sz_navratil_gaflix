from django.db import models
from datetime import date

class Movie(models.Model):
    name = models.CharField(max_length=300, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    footage = models.PositiveSmallIntegerField(
        blank=True, null=True, help_text="in minutes"
    )
    description = models.TextField(blank=True)
    main_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=300, null=True)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    main_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=300, null=True)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    main_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name