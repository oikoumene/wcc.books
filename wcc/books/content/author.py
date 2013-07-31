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

class IAuthor(form.Schema, IImageScaleTraversable):
    """
    
    """
    
    name = schema.TextLine(title=u'Name')
    surname = schema.TextLine(title=u'Surname')

    form.widget(biography="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    biography = schema.Text(title=u'Biography')


