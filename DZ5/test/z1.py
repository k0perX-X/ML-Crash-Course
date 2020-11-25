from test import test
import requests
from flask import render_template
from anime import anime


@test.route('/anime')
def ani():
	#ani = [];for i in anime(): ani.append(i)
	return render_template('anime.html', anime=anime())
@test.route('/')
def index():
	result = requests.get('https://jsonplaceholder.typicode.com/posts').json()
	#print(result)
	return render_template('index.html', posts=result)
