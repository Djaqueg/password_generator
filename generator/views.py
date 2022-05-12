from django.shortcuts import render
# from django.http import HttpResponse
import random

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz') #Define the list of the characters to use
    generated_password = '' #It's necessary create the empty variable
    
    length = int(request.GET.get('length')) #Get the propiety length from request
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('specials'):
        characters.extend(list('_!#$%&*()'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    for x in range(length): 
        generated_password += random.choice(characters) #Save the random characters created on the variable
    return render(request, 'password.html', {'password': generated_password}) #Send the data dictionary to password.html
