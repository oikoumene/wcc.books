from plone.indexer import indexer
from wcc.books.content.book import IBook


@indexer(IBook)
def book_subjects(obj):
    return obj.book_subjects.split('\r\n')


@indexer(IBook)
def book_categories(obj):
    return obj.book_categories.split('\r\n')


@indexer(IBook)
def book_series_title(obj):
    return obj.series_title.split('\r\n')
