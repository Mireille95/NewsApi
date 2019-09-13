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







