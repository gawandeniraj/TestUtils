from django.shortcuts import render
import string

def index(request):
    params = {'name' : 'niraj', 'place' : 'kalamb'}
    return render(request, 'index.html', params)

def analyze(request):
    test_dj = request.POST.get('text', 'default') # read text value which enter by user on page text area

    # check checkbox value
    removepun = request.POST.get('removepun', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    removespc = request.POST.get('removespc','off')
    extraspac = request.POST.get('extraspac', 'off')
    charcounter = request.POST.get('charcounter', 'off')


    # check conditions for performing action
    if removepun == 'on':
        analyzed = "".join([word for word in test_dj if word not in string.punctuation])
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        test_dj = analyzed
    if uppercase == 'on':
        analyzed = test_dj.upper()
        params = {'purpose': 'Convert To Upper Case', 'analyzed_text': analyzed}
        test_dj = analyzed
    if removespc == 'on':
        analyzed = test_dj.replace(" ","")
        params = {'purpose': 'Remove Space', 'analyzed_text': analyzed}
        test_dj = analyzed
    if extraspac == 'on':
        analyzed = " ".join(test_dj.split()) # split complete string in list and then join with " " this space
        params = {'purpose': 'Original Text', 'analyzed_text': analyzed}  # add value into dictionary
        test_dj = analyzed
    if charcounter == 'on':
        analyzed = len(test_dj) - test_dj.count(' ')
        params = {'purpose': 'Number Of Character', 'analyzed_text': analyzed}
        test_dj = analyzed
    if removepun != 'on' and uppercase != 'on' and removespc != 'on' and extraspac != 'on' and charcounter != 'on':
        analyzed = test_dj
        params = {'purpose': 'Please Select Particular Operation', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)


