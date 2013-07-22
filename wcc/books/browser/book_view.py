from five import grok
from plone.directives import dexterity, form
from wcc.books.content.book import IBook

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IBook)
    grok.require('zope2.View')
    grok.template('book_view')
    grok.name('view')

