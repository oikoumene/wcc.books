from collective.grok import gs
from Products.CMFCore.utils import getToolByName
from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.app.intid.interfaces import IIntIds
from z3c.relationfield.event import _relations, updateRelations

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.books to 2',
                description=u'Upgrade wcc.books to 2',
                source='1', destination='2',
                sortkey=1, profile='wcc.books:default')
def to2(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.books.upgrades:to2')

    portal_catalog = getToolByName(context, 'portal_catalog')

    intids = getUtility(IIntIds)

    for b in portal_catalog(
            portal_type=['wcc.books.book'],
            Language='all'):
        obj = b.getObject()
        for name, relation in _relations(obj):
            try:
                relation.to_id = intids.getId(relation.to_object)
            except KeyError:
                continue
        updateRelations(obj, None)
