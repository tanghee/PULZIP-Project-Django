from django.db import models


class Slide(models.Model):
    image = models.ImageField()

    class Meta:
        db_table = 'slide'
