from newsapi import NewsApiClient # pip install newsapi-python

newsapi = NewsApiClient(api_key='API_KEY')

# Chercher les articles sur un sujet donné
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en')

dt = top_headlines["articles"]

for x,y in enumerate(dt):
    print(f'{x} {y["description"]}')