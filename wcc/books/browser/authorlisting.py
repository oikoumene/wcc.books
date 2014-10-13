from five import grok
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class AuthorListing(grok.View):
    grok.context(IContentish)
    grok.name('authorlisting')
    grok.require('zope2.View')
    grok.template('authorlisting')
