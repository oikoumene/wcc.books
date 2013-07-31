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

from wcc.books import MessageFactory as _


# Interface class; used to define content-type schema.

class IBook(form.Schema, IImageScaleTraversable):
    """
    
    """

    subtitle = schema.TextLine(required=False)

    authors = RelationList(
            title=_(u'Authors'),
            value_type=RelationChoice(
                source=ObjPathSourceBinder()
            ),
            required=False
    )

    image = NamedBlobImage(
        title=_(u'Image'),
    )

    issue_date = schema.Date(title=u'Issuing Date')

    price = schema.Float(title=u'Price', required=False)

    note = schema.Text(title=u'Note', required=False)

    pages = schema.Int(title=u'Pages', required=False)

    book_subjects = schema.TextLine(title=u'Subjects',
            required=False)

    series_title = schema.TextLine(
            title=u'Series Title',
            required=False)

    edition = schema.TextLine(
            title=u'Edition',
            required=False)

    toc = schema.Text(
            title=u'TOC',
            required=False)
