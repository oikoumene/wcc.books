from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer


from wcc.books import MessageFactory as _


# Interface class; used to define content-type schema.

class IBook(form.Schema, IImageScaleTraversable):
    """
    Schema for Book contenttype
    """

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(u'Title'),
        )

    subtitle = schema.TextLine(
        title=_(u'Subtitle'),
        required=False
        )

    description = schema.Text(
        title=_(u'Description'),
        )

    summary = RichText(
        title=_(u'Summary'),
        )
    
    authors = RelationList(
        title=_(u'Authors'),
        value_type=RelationChoice(source=ObjPathSourceBinder()),
        required=False
        )

    image = NamedBlobImage(
        title=_(u'Image'),
        required=False
        )

    issue_date = schema.Date(
        title=u'Issuing Date',
        )

    price = schema.TextLine(
        title=u'Price',
        required=False
        )

    pages = schema.Int(
        title=u'Pages',
        required=False
        )

    dexteritytextindexer.searchable('series_title')
    series_title = schema.Text(
        title=u'Series Title',
        required=False
        )

    dexteritytextindexer.searchable('isbn10')
    isbn10 = schema.TextLine(
        title=_(u'ISBN10'),
        max_length=10,
        )

    dexteritytextindexer.searchable('isbn13')
    isbn13 = schema.TextLine(
        title=_(u'ISBN13'),
        max_length=13,
        )

    edition = schema.TextLine(
        title=u'Edition',
        required=False
        )

    toc = schema.Text(
        title=u'TOC',
        required=False
        )
