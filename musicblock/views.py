# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render 

from .forms import MusicForm 
from .models import Music 


# Create your views here. 


def music_list(request): 
	Musics = Music.objects.all() 
	return render(request, 'musicblock/music_list.html', {'Musics': Musics}) 


def music_create(request): 
	if request.method == "POST": 
		form = MusicForm(request.POST) 
		if form.is_valid(): 
			Music = form.save() 
			return redirect('music_list') 
	else: 
		form = MusicForm() 
	return render(request, 'musicblock/Music_form.html', {'form': form}) 

