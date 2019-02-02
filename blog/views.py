from django.shortcuts import render
from .models import Post,List
# Create your views here.
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def list_2(request):
	# получить состояние кнопки
	button_state = True
	if request.method == 'POST':
		state = request.POST.get('state') # on off
		button_state = state == 'on'
		#вызвать скрипт
	return render(request, 'blog/list_2.html', {'button_state': button_state, })

def list_3(request):
	# получить состояние кнопки
	button_state = True
	if request.method == 'POST':
		state = request.POST.get('light_203b') # on off
		button_state = state == 'on'
		#вызвать скрипт
	return render(request, 'blog/list_3.html', {'button_state': button_state, })
	

'''
import os
import re
import time
os.popen("service knxd start")
time.sleep(10)
print "time end"
os.popen("mosquitto_pub -h 192.168.15.8 -t /devices/knx/controls/data/on -m \"g:3/3/3 GroupValueWrite 0x01\"")
os.popen("mosquitto_pub -h 192.168.15.8 -t /devices/knx/controls/data/on -m \"g:3/3/4 GroupValueWrite 0x01\"")
os.popen("mosquitto_pub -h 192.168.15.8 -t /devices/knx/controls/data/on -m \"g:3/3/2 GroupValueWrite 0x01\"")


print "read dev " +" vid"

os.popen("service knxd stop")
'''
