'''
Show 'up' interfaces.
'''

from xml.etree import ElementTree

tree = ElementTree.parse('notes/show_int_brief.xml')
ins_api = tree.getroot()
for row in ins_api.findall('.//ROW_interface'):
    status = row.find('state')
    if status.text == 'up':
        print row.find('interface').text

