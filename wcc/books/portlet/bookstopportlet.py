from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.books import MessageFactory as _
from plone.api.portal import get_tool

class IBookstopportlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(IBookstopportlet)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('Books top portlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/bookstopportlet.pt')

    @property
    def available(self):
        return True

    def get_top(self, index_name):
        #https://developer.plone.org/searching_and_indexing/query.html
        #counting-value-of-an-specific-index
        stats = {}
        x = get_tool('portal_catalog')
        index = x._catalog.indexes[index_name]
        for key in index.uniqueValues():
            t = index._index.get(key)
            if type(t) is not int:
                stats[str(key)] = len(t)
            else:
                stats[str(key)] = 1

        return sorted(stats, key=stats.get, reverse=True)[:3]


class AddForm(base.AddForm):
    form_fields = form.Fields(IBookstopportlet)
    label = _(u"Add Books top portlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(IBookstopportlet)
    label = _(u"Edit Books top portlet")
    description = _(u"")
