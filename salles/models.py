from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# class Compte(models.Model):
# 	GRADE = (
# 		('licence', 'Licence'),
# 		('master', 'Master'),
# 		('doctorat', 'Doctorat'),
# 	)

# 	CIVILITE = (
# 		('marie', 'Marié(e)'),
# 		('divorce', 'Divorcé(e)'),
# 		('celibataire', 'Célibataire'),
# 	)

# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	profil = models.ImageField()
# 	grade = models.CharField(max_length=9, choices=GRADE)
# 	civilite = models.CharField(max_length=12, choices=CIVILITE)


class Formation(models.Model):
	CYCLES = (
		('licence', 'Licence'),
		('master', 'Master'),
		('doctorat', 'Doctorat'),
	)

	libelle = models.CharField(max_length=60)
	cycle = models.CharField(max_length=9, choices=CYCLES)

	def __str__(self):
		return '%s %s'%(self.libelle, self.cycle)


# class Section(models.Model):
# 	libelle = models.CharField(max_length=60)
# 	formation = models.ForeignKey(Formation, on_delete=models.SET_NULL)

# 	def __str__(self):
# 		return '%s'%(self.libelle)


# class Groupe(models.Model):
# 	libelle = models.CharField(max_length=60)
# 	section = models.ForeignKey(Section, on_delete=models.SET_NULL)


# class Semestre(models.Model):
# 	libelle = models.CharField(max_length=60)
# 	date_debut_trimestre = models.DateTimeField()
# 	date_fin_trimestre = models.DateTimeField()


# class Module(models.Model):
# 	libelle = models.CharField(max_length=60)
# 	formation = models.ForeignKey(Formation, on_delete=models.SET_NULL)
# 	semestre = models.ForeignKey(Semestre, on_delete=models.SET_NULL)
# 	volume_horaire = models.IntegerField()


# class Salle(models.Model):
# 	libelle = models.CharField(max_length=60)
# 	type_salle = models.CharField()
# 	bloc_salle = models.CharField()
# 	capacite = models.IntegerField()


# class Seance(models.Model):
# 	JOUR = (
# 		('Lu', 'Lundi'),
# 		('Ma', 'Mardi'),
# 		('Me', 'Mercredi'),
# 		('Je', 'Jeudi'),
# 		('Ve', 'Vendredi'),
# 	)
# 	module = models.ForeignKey(Module, on_delete=models.SET_NULL)
# 	user = models.ForeignKey(User, on_delete=models.SET_NULL)
# 	salle = models.ForeignKey(Salle, on_delete=models.SET_NULL)
# 	section = models.ForeignKey(Section, on_delete=models.SET_NULL)
# 	groupe = models.ForeignKey(Groupe, on_delete=models.SET_NULL)
# 	libelle = models.CharField(max_length=60)
# 	type_seance = models.CharField()
# 	plage_horaire = models.CharField()
# 	semestre = models.ForeignKey(Semestre, on_delete=models.SET_NULL)
# 	formation = models.ForeignKey(Formation, on_delete=models.SET_NULL)
# 	jour = models.CharField(max_length=2, choices=JOUR)
# 	anne_universitaire = models.CharField()


# class Voeux(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.SET_NULL)
# 	module = models.ForeignKey(Module, on_delete=models.SET_NULL)
# 	anne_universitaire = models.CharField()


# class Disponibilite(models.Model):
# 	JOUR = (
# 		('Lu', 'Lundi'),
# 		('Ma', 'Mardi'),
# 		('Me', 'Mercredi'),
# 		('Je', 'Jeudi'),
# 		('Ve', 'Vendredi'),
# 	)

# 	user = models.ForeignKey(User, on_delete=models.SET_NULL)
# 	semestre = models.ForeignKey(Semestre, on_delete=models.SET_NULL)
# 	plage_horaire = models.CharField()
# 	jour = models.CharField(max_length=2, choices=JOUR)
# 	anne_universitaire = models.CharField()
# 	disponible = models.CharField()