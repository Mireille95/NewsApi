from flask import render_template
from . import main
from ..request import get_sources, get_articles, search_sources
from ..models import Sources

@main.route('/')
def index():
  
    
    sources = get_sources('business')
    sport_sources  = get_sources('sports')
    entertainment_sources = get_sources('entertainment')
    
    title='News highlighter'
    # search_sources =request.args.get('sources_query')
    
    # if search_sources:
    #     return redirect(url_for('search',source_name=search_sources))
    # else:
    return render_template('index.html',title=title, business=sources,sports=sport_sources,entertainment=entertainment_sources)
  

@main.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_sources(source_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html',sources = searched_sources)

@main.route('/articles/<string:id>')
def source(id):
   
    articles = get_articles(id)
    print(articles)
    return render_template('articles.html',articles=articles)










# from flask import render_template

# from .request import get_sources
# from .request import get_sources,get_source,search_sources
# from flask import render_template,request,redirect,url_for
# from .models import reviews
# from .forms import ReviewForm
# Review = reviews.Review

# # Views
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular source
#     popular_sources = get_sources('popular')
#     upcoming_source = get_sources('upcoming')
#     now_showing_source = get_sources('now_playing')

#     title = 'Home - Welcome to The best source Review Website Online'

#     search_sources = request.args.get('source_query')

#     if search_sources:
#         return redirect(url_for('search',source_name=search_sources))
#     else:
#         return render_template('index.html', title = title, popular = popular_sources, upcoming = upcoming_source, now_showing = now_showing_source )


