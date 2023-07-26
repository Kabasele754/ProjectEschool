from django.shortcuts import redirect, render
from .models import  Etudiant, Cours

# Create your views here.
def index_view(request,template_name='inscri/index.html'):
    cours = Cours.objects.all()
    context = {}
    
    context['cours'] =cours
    return render(request,template_name, context)

def connect_view(request,template_name='inscri/connexion.html'):
    return render(request,template_name)

def inscription(request,template_name='inscri/inscription.html'):
   
    # Partie selection 
    etudiant = Etudiant.objects.all()
    print("QuerySet",etudiant)
    print("------------------------------Querette SQL Create----------------------------------")
    print("Query", etudiant.query)
    
    context = {}

    context['etudiants'] = etudiant
    
    return render(request,template_name, context)


# Fomction pour Creer une formation et selection les information creer 
def add(request):
    # Partie pour creer
    if request.method == 'POST':
        etudiant_create = Etudiant(
            nom = request.POST['nom'],
            postnom = request.POST['postnom'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            
        ) 
        etudiant_create.save()
        return redirect('inscription')
    

# La fonction pour mise à jour de donnée et selection les informations mise à jour 
def update(request,id,template_name='inscri/modal.html'):
    # Partie Mise à jour
    etudiant = Etudiant.objects.get(id=id)
    print("------------------------------Querette SQL Update ----------------------------------")
    print("Query", etudiant)
    if request.method == 'POST':
        etudiant.nom = request.POST['nom']
        etudiant.postnom = request.POST['postnom']
        etudiant.email = request.POST['email']
        etudiant.phone = request.POST['phone']
        
        etudiant.save()
        
        return redirect('inscription')
     
    # Partie pour la selection des informations
    etudiant_all_update = Etudiant.objects.all()
    context= {}
    context['etudiants'] =   etudiant_all_update
    context['etudiant_update'] = etudiant
    return render(request,template_name, context)
  
 # Fonction pour supprimer une formation   
def delete(request, id):
    etudiant_delete = Etudiant.objects.get(id=id)
    etudiant_delete.delete()
    
    return redirect('inscription')
    
    
    
    
    