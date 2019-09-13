import urllib.request,json
from .models import Sources,Articles

api_key = None
base_url = None
base_url_articles = None

def configure_request(app):
    global api_key,base_url,base_url_articles
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEW_API_BASE_URL']
    base_url_articles = app.config['NEWS_URL_ARTICLES']

    print('base_url')
    # print(base_url_articles)
    print('apikey')

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)


    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')


        sources_object = Sources(id,name,description,url,category,language,country)
        sources_results.append(sources_object)

    return sources_results

def get_articles(id):
    '''
    function that gets the json response to url
    '''
    print(base_url_articles)
    print(id)
    print(api_key)
    get_articles_url = base_url_articles.format(id,api_key)

    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None
        if get_articles_response['articles']:
            articles_results_list =  get_articles_response['articles']
            articles_results = process_article_results(articles_results_list)

    return articles_results


def process_article_results(articles_list):
    articles_results = []

    for article_item in articles_list:
        source = article_item.get('source')
        author = article_item.get('author')
        title= article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')



        articles_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
        articles_results.append(articles_object)
    return articles_results
    
def search_sources(movie_name):
    search_sources_url = 'https://newsapi.org/v2/search/sources?api_key={}&query={}'.format(api_key,source_name)
    with urllib.request.urlopen(search_sources_url) as url:
        search_sources_data = url.read()
        search_sources_response = json.loads(search_sources_data)

        search_sources_results = None

        if search_sources_response['results']:
            search_sources_list = search_sources_response['results']
            search_sources_results = process_results(search_sources_list)


    return search_sources_results

    # "https://newsapi.org/v2/sources?language&category={}&apiKey={}"