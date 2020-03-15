from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login as auth_login
from django.db.models.functions import Lower
# Create your views here.


#Check valid email
def is_email(string):
    from django.core.validators import EmailValidator
    validator = EmailValidator()
    try:
        validator(string)
    except ValidationError:
        return False

    return True


#Check valid username
def UsernameValidator(string):
    from django.contrib.auth.validators import UnicodeUsernameValidator
    validator = UnicodeUsernameValidator()
    try:
        validator(string)
    except ValidationError:
        return False

    return True


def is_password_eligible(password):
    if password == '': # Nu este un cuvant
        return False, ''

    if len(password) < 5:
        return False, 'The password must contain minimum 5 characters.'

    for litera in password: # Exista spatii
        if litera == ' ':
            return False, 'Password contains forbidden space.'
    return True, ''

def is_password_eligible(password):
    if len(password) < 5:
        return False, 'The password must contain minimum 5 characters.'

    return True, ''


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "GET":
        return render(request, "register.html")

    # Calea cand requestul este POST
    username = request.POST['username'].lower()
    email = request.POST['email'].lower()
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if not UsernameValidator(username):
        messages.info(request, 'Username contains forbidden space or characters!') #Username-ul contine spatiu sau caractere interzise!
        return redirect('register')

    if not is_email(email):
        messages.info(request, 'The email is not valid ("example@gmail.com").') #'Email-ul nu este valid ("exemplu@gmail.com")!'
        return redirect('register')

    if password1 != password2:
        messages.info(request, 'The verification password is not the same.') #Parola de verificare nu este la fel.
        return redirect('register')

    eligible_password, password_error_msg = is_password_eligible(password1)
    if not eligible_password:
        messages.info(request, password_error_msg)
        return redirect('register')

    if User.objects.filter(username=username).exists():
        messages.info(request, 'The username is used.') # Username-ul este folosit.
        return redirect('register')

    if User.objects.filter(email=email).exists():
        messages.info(request, 'The email is used. ') # Email-ul este folosit.
        return redirect('register')

    user = User.objects.create_user(username=username, password=password1, email=email)
    user.save()
    print("User created")
    messages.success(request, 'Contul a fost creat cu succes!')
    user = auth.authenticate(username=username, password=password1)
    auth.login(request, user)
    return redirect("/")


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            print("Logat")
            username = request.POST['username'].lower()
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Welcome back!')
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password!") #Username-ul sau parola nu sunt valide!
                return redirect('login')

        else:
            return render(request, "login.html")

@login_required


def settings(request):
    from django.contrib.auth.hashers import make_password, check_password

    if request.method == "POST":
        user_curent = request.user
        username_input = request.POST['username']
        email_curent = request.POST['email']
        parola_veche_input = request.POST['parola_veche']
        parola_noua1_input = request.POST['parola_noua1']
        parola_noua2_input = request.POST['parola_noua2']
        print(parola_veche_input)
        if (parola_veche_input == '') and (parola_noua1_input == '') and (parola_noua2_input == '') :
            print("Parola nu a fost selectata")
        else:
            #Verificare parola veche cu baza de date;
            if not check_password(parola_veche_input, request.user.password):
                messages.error(request, "The password in the database is not the same as the password in the input.")
                return redirect('settings')

            eligible_password1, password_error_msg = is_password_eligible(parola_veche_input)
            eligible_password2, password_error_msg = is_password_eligible(parola_noua1_input)
            eligible_password3, password_error_msg = is_password_eligible(parola_noua2_input)
            if not eligible_password1 or not eligible_password2 or not eligible_password3:
                messages.error(request, password_error_msg)
                return redirect('settings')

            if parola_noua1_input != parola_noua2_input:
                print("Parola1 si parola2 nu sunt la fel")
                messages.error(request, "The password is not the same!")
                return redirect('settings')

            pass_hash = make_password(parola_noua1_input)
            request.user.password = pass_hash
            username_curent = request.user.username
            request.user.save()
            user = authenticate(request, username=username_curent, password=parola_noua1_input)
            auth_login(request, user)
            messages.success(request, "Password saved!")
            return redirect('settings')

        if user_curent.username == username_input :    #Daca username-ul curent este la fel ca username-ul din input
            if user_curent.email != email_curent:
                if User.objects.filter(email=email_curent).exists():
                    messages.error(request, "The email already exists in the database.") #Email-ul exista deja in baza de date.
                    return redirect('settings')
                user_curent.email = email_curent
                user_curent.save()
                messages.success(request, "The email has been successfully changed!") #Email-ul a fost schimbat cu succes!
                return redirect('settings')
            messages.success(request, "There was nothing to change!") # Nu a fost nimic de modificat!
            return redirect('settings')
        if User.objects.filter(username=username_input).exists():
            messages.error(request, "The nickname already exists in the database.") # Nickname-ul exista deja in baza de date.
            return redirect('settings')
        if User.objects.filter(email=email_curent).exists() and user_curent.email != email_curent:
            messages.error(request, "The email already exists in the database.") # Email-ul exista deja in baza de date.
            return redirect('settings')
        if user_curent.email == email_curent and user_curent.username != username_input:
            user_curent.username = username_input
            user_curent.save()
            messages.success(request, "Your nickname has been successfully changed!") # Nickname-ul a fost schimbat cu succes!
            return redirect('settings')
        user_curent.email = email_curent
        user_curent.username = username_input
        user_curent.save()
        messages.success(request, "The data has been changed!") # Datele au fost schimbate cu succes!
        return redirect('settings')

        # TODO: Adauga sa poti schimba parola!
    else:
        return render(request, "settings.html")


def logout(request):
    auth.logout(request)
    return redirect('/')