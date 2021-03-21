from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=128)
    SN = models.CharField(max_length=128)
    #red = models.CharField(max_length=128)
    #green = models.CharField(max_length=128)
    #blue = models.CharField(max_length=128)

    def __str__(self):
        return f'{[self.name, self.SN]!r}'


if __name__ == '__main__':
    Subscriber()