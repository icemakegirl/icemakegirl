from django.db import models

# Create your models here.


class cadastro(models.Model):
    nome=models.CharField(max_length=100)
    quantia=models.DecimalField(max_digits=10,decimal_places=2)
    data=models.DateField()
    def __str__(self):
        return self.nome
