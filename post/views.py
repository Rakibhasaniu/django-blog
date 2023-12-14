from django.shortcuts import render, redirect
from . import forms
from post.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST) # user er post request data ekhane capture korlam
        if post_form.is_valid(): # post kora data gula amra valid kina check kortechi
            # post_form.cleaned_data['author'] =request.user
            post_form.instance.author = request.user
            post_form.save() # jodi data valid hoy taile database e save korbo
            return redirect('add_post') # sob thik thakle take add author ei url e pathiye dibo
    
    else: # user normally website e gele blank form pabe
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : post_form})



@login_required
def edit_post(request,id):
    post = Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST': 
        post_form = forms.PostForm(request.POST, instance=post) 
        if post_form.is_valid(): 
            post_form.instance.author = request.user
            post_form.save() 
            return redirect('homepage') 
    
    # else: 
    #     post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : post_form})

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage') 

