# I have create this file - ved
from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html', )


def analyzer(request):
    djtext = request.POST.get('text', 'defoult')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove punctuations', 'analyze_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Full capitalized ', 'analyze_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        djtext = djtext.strip()
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover ', 'analyze_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New line remover ', 'analyze_text': analyzed}

    if (newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and removepunc != "on"):
        return HttpResponse("<h1>Please select text Operation and try again!</h1>")

    return render(request, 'analyze.html', params)
