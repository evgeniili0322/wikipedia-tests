from dataclasses import dataclass


@dataclass
class SearchQuery:
    single_article = 'Selenium'
    multiple_articles = 'Python'
    no_match = 'wikiemptyresult'


search_query = SearchQuery()
