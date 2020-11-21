'''
Simple usage of XML.
'''

from xml.etree import ElementTree

tree = ElementTree.parse('notes/books.xml')
catalog = tree.getroot()

# get the title of bk110
for book in catalog.findall('book'):
    if book.get('id') == 'bk110':
        title = book.find('title')
        print title.text

# sum all the prices
total = 0
for price in catalog.findall('book/price'):
    total += float(price.text)
print total
