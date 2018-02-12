# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
import requests, json
class HomePageView(TemplateView):
    template_name = 'home.html'

def news_page(request):
	return render(request, 'news.html')

def anime_page(request):
	anime_data = json.loads(json.dumps(get_seasonal_anime()))
	return render(request, 'anime.html', {'anime_data' : anime_data['data']['Page']['media']})

def get_seasonal_anime():
	# Here we define our query as a multi-line string
	query = '''
	{
	  Page{
	    pageInfo {
	      total
	    }
	    media(type:ANIME, season:FALL, seasonYear:2017) {
	      title {
	        english
	      },
	      id,
	      season,
	      averageScore,
	      popularity
	    }
	  }
	}
	'''

	# Define our query variables and values that will be used in the query request
	variables = {
	    'tezt': 15125
	}

	url = 'https://graphql.anilist.co'

	# Make the HTTP Api request
	response = requests.post(url, json={'query': query, 'variables': variables})
	return response.json()