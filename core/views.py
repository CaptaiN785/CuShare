from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return redirect('server')
    ## directly redirected to server page
    return render(request, 'core/index.html')
