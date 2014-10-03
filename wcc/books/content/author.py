from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid, Interface

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent

from wcc.books import MessageFactory as _
from wcc.books.backref import back_references
from operator import itemgetter, attrgetter

from collective import dexteritytextindexer

# Interface class; used to define content-type schema.


class IAuthor(form.Schema, IImageScaleTraversable):
    """

    """

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(title=u'Name')

    description = schema.Text(title=u'Biography')


class IAuthorDataProvider(Interface):
    pass


class AuthorDataProvider(grok.Adapter):
    grok.context(IAuthor)
    grok.implements(IAuthorDataProvider)

    @property
    def related_books(self):
        return sorted(back_references(self.context, 'authors'),
                      key=attrgetter('title'))
