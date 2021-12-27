from django.db import models

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=15)
    postnom = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    phone =  models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.nom} {self.email}"



class Cours(models.Model):
    titre = models.CharField(max_length=15)
    credit = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self):
        return self.titre
    
class GestioCoursEtudiant(models.Model):
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField()
    description =  models.TextField()


    
    
    