from five import grok
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class BooksListing(grok.View):
    grok.context(IContentish)
    grok.name('bookslisting')
    grok.require('zope2.View')
    grok.template('bookslisting')
