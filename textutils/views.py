#I have created this file - Yahya

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    inputText = request.POST.get('text', 'default')
    rmp = request.POST.get('removePunc','off')
    newLiner = request.POST.get('removeNewLine', 'off')
    spaceR = request.POST.get('removeSpace', 'off')
    fullcap = request.POST.get('fullcaps', 'off')
    charC = request.POST.get('charCounter', 'off')

    if rmp == 'on':
        punctuations = '''?…!.,—––:;“‘[](){}@#$%^&*'''
        analyzed = ""
        for char in inputText:
            if char not in punctuations:
                analyzed = analyzed + char
        paras = {'purpose':'Remove Punctutations', 'removed_text':analyzed}
        inputText = analyzed
        #return render(request, 'analyze.html', paras)
    if fullcap == 'on':
        analyzed = ""
        for char in inputText:
            analyzed = analyzed + char.upper()
        paras = {'purpose': 'Capitalize All', 'removed_text': analyzed}
        inputText = analyzed
        #return render(request, 'analyze.html', paras)
    if newLiner == 'on':
        analyzed = ""
        for char in inputText:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
        paras = {'purpose': 'Remove New Line', 'removed_text': analyzed}
        inputText = analyzed
        #return render(request, 'analyze.html', paras)
    if spaceR == 'on':
        analyzed = ""
        for index, char in enumerate(inputText):
            if not (inputText[index] == ' ' and inputText[index+1] == ' '):
                analyzed = analyzed + char
        paras = {'purpose': 'Remove Space', 'removed_text': analyzed}
        inputText = analyzed
        #return render(request, 'analyze.html', paras)
    if charC == 'on':
        counter = 0
        for char in inputText:
            counter += 1
        paras = {'purpose': 'Character Counter', 'removed_text': counter}
        inputText = analyzed
        #return render(request, 'analyze.html', paras)
    if(rmp != 'on' and fullcap != 'on' and newLiner != 'on' and spaceR != 'on' and charC != 'on'):
        return HttpResponse("Please Select Operatios")
    return render(request, 'analyze.html',paras)

