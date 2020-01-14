from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.


class Jogo(models.Model):
	#campeonato = models.ForeignKey('Campeonato',related_name="jogos")
	time1 = models.CharField(max_length=200)
	time2 = models.CharField(max_length=200)
	data_hora = models.CharField(max_length=200)
	gols_time1 = models.PositiveSmallIntegerField(blank=True,null=True)
	gols_time2 = models.PositiveSmallIntegerField(blank=True,null=True)

	def __str__(self):
		return "%s x %s" % (self.time1, self.time2)


class Aposta(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	jogo = models.ForeignKey('Jogo', related_name="apostas", on_delete=models.CASCADE)
	gols_time1 = models.PositiveSmallIntegerField(blank=True,null=True)
	gols_time2 = models.PositiveSmallIntegerField(blank=True,null=True)
	