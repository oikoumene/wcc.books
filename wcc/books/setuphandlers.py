from collective.grok import gs
from wcc.books import MessageFactory as _

@gs.importstep(
    name=u'wcc.books', 
    title=_('wcc.books import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.books.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
