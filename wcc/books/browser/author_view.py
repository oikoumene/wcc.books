from five import grok
from plone.directives import dexterity, form
from wcc.books.content.author import IAuthor, IAuthorDataProvider

grok.templatedir('templates')


class Index(dexterity.DisplayForm):
    grok.context(IAuthor)
    grok.require('zope2.View')
    grok.template('author_view')
    grok.name('view')

    def provider(self):
        return IAuthorDataProvider(self.context)
