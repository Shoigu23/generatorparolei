from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from main.models import Pass
import random
from django.contrib import messages


# Create your views here.
def main(request):
    if request.method == 'POST':
        lenth = int(request.POST.get('title'))
        lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        dig = list('qwertyuiopasdfghjklzxcvbnm')
        upper = list('QWERTYUIOPASDFGHJKLZXCVBNM')
        simb = ['!', '@', '$', '%', '&', '*']
        # g = ''
        pas = lst
        if request.POST.get('Большие буквы'):
            pas += upper
            messages.success(request, 'Приняты большие буквы')
        if request.POST.get('Маленькие буквы'):
            pas += dig
            messages.success(request, 'Приняты маленькие буквы')
        if request.POST.get('Спец символы'):
            pas += simb
            messages.success(request, 'Приняты специальные символы')
    t = ''
    for r in range(int(lenth)):
        t += random.choice(lst)
    if lenth < 8:
        messages.error(request, 'Слишком маленький пароль')
        return render(request, 'index.html')
    elif lenth > 30:
        messages.error(request, 'Слишком длинный пароль')
        return render(request, 'index.html')

    return render(request, 'index.html', {'t': t})
