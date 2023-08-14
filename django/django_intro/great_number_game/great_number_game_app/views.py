from django.http import HttpResponse
from django.shortcuts import redirect, render
import random

# Create your views here.


def index(request):
    if 'rand_num' not in request.session:
        request.session['rand_num'] = random.randint(1, 100)

    if not 'attempts' in request.session:
        request.session['attempts'] = {
            'number': 0, 'message': 'attempts before guessing the correct number'}

    return render(request, "index.html")


def guess(request):
    rand = int(request.session['rand_num'])
    input_num = int(request.POST['guess_num'])

    if input_num < rand:
        request.session['attempts']['number'] += 1
        request.session['result'] = {'state': 'Too low!', 'color': 'red'}
        print(request.session['result'])
    elif input_num > rand:
        request.session['attempts']['number'] += 1
        request.session['result'] = {'state': 'Too high!', 'color': 'red'}
    else:
        request.session['result'] = {
            'state': str(rand) + ' was the number!', 'color': 'green'}

    return redirect('/')


def delete_session(request):
    del request.session['attempts']
    del request.session['rand_num']
    del request.session['result']
    return redirect('/')

# SENSEI BONUS: If they win, allow the user to submit their name. Have a link to a leaderboard page that shows winners' names and how many attempts they took to guess correctly.
