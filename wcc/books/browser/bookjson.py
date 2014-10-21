from five import grok
from Products.CMFCore.interfaces import IContentish
from plone import api
from wcc.books.content.book import IBook
from zope.schema import getFieldsInOrder
import json
from base64 import b64encode

grok.templatedir('templates')


class BookJSON(grok.View):
    grok.context(IContentish)
    grok.name('bookjson')
    grok.require('zope2.View')

    def getbooks(self):

        catalog = api.portal.get_tool("portal_catalog")

        return catalog(portal_type="wcc.books.book", review_state="published")

    def create_json(self):

        books = self.getbooks()

        # remove = ['toc', 'image', 'description']

        fields = [n for n, d in getFieldsInOrder(IBook)]

        # remove unneeded fields
        # for i in remove:
        #    fields.remove(i)

        books_data = list()

        for brain in books:
            single_book = dict()
            obj = brain.getObject()
            for field in fields:
                if field is 'authors':
                    values = getattr(obj, field, None)
                    if values:
                        listvalue = [v.to_object.Title() for v in values]
                        value = ', '.join(listvalue)
                    else:
                        value = None
                elif field is 'image':
                    image = getattr(obj, field, None)
                    if image:
                        value = b64encode(image.data)

                else:
                    value = getattr(obj, field, None)

                if isinstance(value, unicode):
                    value.encode("utf-8")
                elif isinstance(value, str):
                    value = unicode(value, "utf-8").encode("utf-8")

                else:
                    value = unicode(str(value), "utf-8")

                single_book.update({field: value})

            books_data.append(single_book)

        return books_data

    def render(self):

        out = self.create_json()

        filename = "books.json"

        self.request.response.setHeader('Content-Type', 'text/json')
        self.request.response.setHeader('Content-Disposition', ('attachment;'
                                        'filename="%s"') % filename)

        return json.dumps(out)
