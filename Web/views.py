from django.shortcuts import render, redirect
from django.contrib import messages
from .models import retele_de_socializare_utilizator


# Create your views here.

def home(request):

    # Pt. render pagina cand este ceruta cu "GET" and user is login
    if request.method == "GET" and request.user.is_authenticated:
        # Create a object when doesn't exist.
        if not retele_de_socializare_utilizator.objects.filter(user=request.user).exists():
            # up to object 'retele_de_socializare_utilizator'
            retele_de_socializare_utilizator_object = retele_de_socializare_utilizator(
                user=request.user,
                github="https://github.com/",
                facebook="https://www.facebook.com/",
                instagram="https://www.instagram.com/",
                gmail="",
                youtube="https://www.youtube.com/channel/",
                linkedin="https://www.linkedin.com/in/",
                discord="",
                skype="",
                steam="https://steamcommunity.com/profiles/",
                paypal="paypal.me/",
            )
            retele_de_socializare_utilizator_object.save()

            print("Obiectul a fost creat (user:  ", request.user, ")")
            return redirect('home')

        # Put inputs from database
        inputs_retele_socializare = retele_de_socializare_utilizator.objects.filter(user=request.user).first()
        return render(
            request,
            'home.html',
            {
                'inputs_retele_socializare': inputs_retele_socializare,
            }
        )
    # Pt. render pagina cand este ceruta cu "GET" and user is NOT login
    if request.method == "GET":
        return render(
            request,
            'home.html',
        )

    ## When you click on "UPDATE"

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

def name_profile_function(request, name_profile):
    return render(
        request, 'profile_show.html',
        {
            'name_profile': name_profile
        }
    )