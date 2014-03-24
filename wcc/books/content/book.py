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

    subtitle = schema.TextLine(
        title=_(u'Subtitle'),
        required=False
        )

    authors = RelationList(
        title=_(u'Authors'),
        value_type=RelationChoice(source=ObjPathSourceBinder()),
        required=False
        )

    image = NamedBlobImage(
        title=_(u'Image'),
        )

    summary = schema.Text(
        title=_(u'Summary'),
        required=False,
        )

    issue_date = schema.Date(
        title=u'Issuing Date',
        )

    price = schema.Float(
        title=u'Price',
        required=False
        )

    note = schema.Text(
        title=u'Note',
        required=False
        )

    pages = schema.Int(
        title=u'Pages',
        required=False
        )

    dexteritytextindexer.searchable('book_subjects')
    book_subjects = schema.Text(
        title=u'Subjects',
        required=False
        )

    dexteritytextindexer.searchable('series_title')
    series_title = schema.Text(
        title=u'Series Title',
        required=False
        )

    isbn = schema.TextLine(
        title=_(u'ISBN'),
        required=False
        )

    edition = schema.TextLine(
        title=u'Edition',
        required=False
        )

    toc = schema.Text(
        title=u'TOC',
        required=False
        )
