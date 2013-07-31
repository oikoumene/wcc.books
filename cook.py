import json
import copy
import re
import base64

def load_items(f):
    placehold = ''
    for l in open(f):
        placehold += l
        if l.strip() == '}':
            yield json.loads(placehold)
            placehold = ''



BOOKS = list(load_items('pubwcc.books.json'))
AUTHORS = list(load_items('pubwcc.authors.json'))
AUTHORS_BY_ID = {}

for a in AUTHORS:
    AUTHORS_BY_ID[a['id'].strip()] = a

CATEGORY = list(load_items('pubwcc.category.json'))

CATEGORY_BY_ID = {}

for c in CATEGORY:
    CATEGORY_BY_ID[c['uid'].strip()] = c


def get_authors_from_ids(authors):
    result = []
    for i in authors.split(','):
        a = AUTHORS_BY_ID.get(i.strip(), None)
        if a:
            result.append(a)
    return result

def get_categories_by_ids(categories):
    result = []
    for i in categories.split(','):
        c = CATEGORY_BY_ID.get(i.strip(), None)
        if c:
            result.append(c['title'].strip())
    return result

def get_pages(book):
    pattern = re.compile('pages: (\d+)')    
    for k in ['remark_1', 'remark_2']:
        val = book.get(k, None)
        match = pattern.match(val)
        if match:
            return int(match.groups()[0])

class Matcher(object):

    def __init__(self, pattern, process):
        self.pattern = re.compile(pattern)
        self._process = process

    def match(self, val):
        return self.pattern.match(val)

    def process(self, val):
        groups = self.pattern.match(val).groups()

        return self._process(groups)

def get_editiondata(book):
    patterns = [
        Matcher('edition: (.*?), series title: (.*?), subject: (.*?)$',
            lambda x: {'edition': x[0], 'series title': x[1], 'subject': x[2]}),
        Matcher('series title: (.*?), subject: (.*?)$',
            lambda x: {'series title': x[0], 'subject': x[1]}),
        Matcher('edition: (.*?), subject: (.*?)$',
            lambda x: {'edition': x[0], 'subject': x[1]}),
        Matcher('subject: (.*?)$', 
            lambda x: {'subject': x[0]})
    ]
    result = {'edition': '', 'series title':'', 'subject': ''}

    for k in ['remark_1', 'remark_2']:
        val = book[k].strip()
        for p in patterns:
            if p.match(val):
                r = p.process(val)
                result.update(r)
                return result

    return result


def get_imagedata(imagename):
    if not imagename:
        return ''

    try:
        image = open('images/%s' % imagename).read()
    except:
        return ''

    return base64.b64encode(image)

def main():
    data = []
    
    for b in BOOKS:
        book = copy.copy(b)
        book['authors'] = [i.strip() for i in b['authors'].split(',')]
        book['category'] = get_categories_by_ids(book['category'])
        book['pages'] = get_pages(book)
        book['image_data'] = get_imagedata(book['image'])
        editiondata = get_editiondata(book)
        book.update(editiondata)
        data.append(book)

    open('out-books.json', 'w').write(json.dumps(data))
    open('out-authors.json', 'w').write(json.dumps(AUTHORS))

main()
