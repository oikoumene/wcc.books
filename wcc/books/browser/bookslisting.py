from five import grok
from plone.app.collection.interfaces import ICollection
from Products.ATContentTypes.interfaces import IATFolder

grok.templatedir('templates')


class BooksListing(grok.View):
    grok.context(IATFolder)
    grok.name('bookslisting')
    grok.require('zope2.View')
    grok.template('bookslisting')


class BooksListingCollection(BooksListing):
    grok.context(ICollection)
