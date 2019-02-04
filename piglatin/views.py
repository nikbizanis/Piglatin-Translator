

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def translate(request):
    originalText = request.GET['original text']

    translation = ''

    for word in originalText.split():

        if word[0] in ['a', 'e', 'i', 'o' 'u']:
            translation += word
            translation += ' yay '
        else:
            translation += word[1:]
            translation += word[0]
            translation += ' ay '

    return render(request, 'translate.html', {'original': originalText,
                                              'translated': translation})


def about(request):
    return render(request, 'about.html')
