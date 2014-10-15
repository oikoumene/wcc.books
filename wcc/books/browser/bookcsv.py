from five import grok
from Products.CMFCore.interfaces import IContentish
from plone import api
from wcc.books.content.book import IBook
from StringIO import StringIO
from zope.schema import getFieldsInOrder
import csv

grok.templatedir('templates')


class BookCsv(grok.View):
    grok.context(IContentish)
    grok.name('bookcsv')
    grok.require('zope2.View')

    def getbooks(self):

        catalog = api.portal.get_tool("portal_catalog")

        return catalog(portal_type="wcc.books.book", review_state="published")

    def writebooks(self, books):
        out = StringIO()
        writer = csv.writer(out,dialect='excel')

        remove = ['toc', 'image', 'description']

        fields = [n for n, d in getFieldsInOrder(IBook)]

        # remove unneeded fields
        for i in remove:
            fields.remove(i)

        # Header
        writer.writerow(fields)

        # Body

        for b in books:
            data = list()
            for i in fields:
                if i is 'authors':
                    values = getattr(b.getObject(), i)
                    listvalue = [n.to_object.Title() for n in values]
                    value = ', '.join(listvalue)
                else:
                    value = getattr(b.getObject(), i)
                    if value is None:
                        value = ''

                if isinstance(value, unicode):
                    value.encode("utf-8")
                elif isinstance(value, str):
                    value = unicode(value, "utf-8").encode("utf-8")
                data.append(value)

            writer.writerow(data)

        return out

    def render(self):

        books = self.getbooks()

        out = self.writebooks(books)

        filename = "books.csv"

        self.request.response.setHeader('Content-Type', 'text/csv')
        self.request.response.setHeader('Content-Disposition', ('attachment;'
                                        'filename="%s"') % filename)

        return out.getvalue()
