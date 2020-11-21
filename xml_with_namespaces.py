'''
The easy way to handle XML namespace
'''

from xml.etree import ElementTree

ns = {'nf': 'urn:ietf:params:xml:ns:netconf:base:1.0',
      'x': 'http://www.cisco.com/nxos:1.0:if_manager'}

tree = ElementTree.parse('notes/interfaces.xml')
rpc_reply = tree.getroot()

for address in rpc_reply.findall('.//x:eth_hw_addr', ns):
    print address.text
