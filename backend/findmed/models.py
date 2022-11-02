from django.db import models

class Sintoma(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Medicamento(models.Model):
    CONCENTRACAO = (
        ('mg', 'mg'),
        ('ml', 'ml'),
        ('mcg', 'mcg'),
    )
    nome = models.CharField(max_length=50)
    dose = models.IntegerField()
    concentracao = models.CharField(max_length=3, choices=CONCENTRACAO, blank=False, null=False, default='mg')
    posologia = models.TextField()

    def __str__(self):
        return self.nome

class Indicacao(models.Model):
    sintoma = models.ForeignKey(Sintoma, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)