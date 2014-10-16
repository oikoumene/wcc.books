from five import grok
from Products.CMFCore.interfaces import IContentish
from Products.ATContentTypes.interfaces import IATFolder
from plone.app.collection.interfaces import ICollection
from wcc.books.content.author import IAuthorDataProvider


grok.templatedir('templates')


class AuthorListing(grok.View):
    grok.context(IATFolder)
    grok.name('authorlisting')
    grok.require('zope2.View')
    grok.template('authorlisting')

    def authorprovider(self, item):
        return IAuthorDataProvider(item.getObject())


class AuthorListingCollection(AuthorListing):
    grok.context(ICollection)
