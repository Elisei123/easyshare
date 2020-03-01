from django.shortcuts import render, redirect
from django.contrib import messages
from .models import retele_de_socializare_utilizator

# Create your views here.

def home(request):
    if request.method == "GET": # Pt. render pagina cand este ceruta cu "GET"
        # Put inputs from database
        return render(request, 'home.html')

    # Take inputs
    github = request.POST['Github_input']
    facebook = request.POST['Facebook_input']
    instagram = request.POST['Instagram_input']
    gmail = request.POST['Gmail_input']
    youtube = request.POST['Youtube_input']
    linkedin = request.POST['Linkedin_input']
    discord = request.POST['Discord_input']
    skype = request.POST['Skype_input']
    steam = request.POST['Steam_input']
    paypal = request.POST['Paypal_input']

    ## When you click on "UPDATE"
    if not retele_de_socializare_utilizator.objects.filter(user=request.user).exists():

        # up to object 'retele_de_socializare_utilizator'
        retele_de_socializare_utilizator_object = retele_de_socializare_utilizator(
            user=request.user,
            github=github,
            facebook=facebook,
            instagram=instagram,
            gmail=gmail,
            youtube=youtube,
            linkedin=linkedin,
            discord=discord,
            skype=skype,
            steam=steam,
            paypal=paypal
        )
        retele_de_socializare_utilizator_object.save()

        print("Obiectul a fost creat (user:  ", request.user, ")")
        return redirect('home')

    # if object exist in database, you must update on them
    retele_de_socializare_utilizator.objects.filter(user=request.user).update(
        user=request.user,
        github=github,
        facebook=facebook,
        instagram=instagram,
        gmail=gmail,
        youtube=youtube,
        linkedin=linkedin,
        discord=discord,
        skype=skype,
        steam=steam,
        paypal=paypal
    )
    print("Obiectul a fost modificat (user:  ", request.user, ")")
    return redirect('home')

#TODO: Vezi ca se salveaza o singura coloana(atribut) P.S: Este pt ca ia din inputs, si in inputs sunt mereu default.
#TODO: Cred ca trebuie sa ii dai update in value, si astfel se ia bine ;)
