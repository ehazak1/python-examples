'''
Making vCards for the brother-in-law.
'''

# import urllib

try:
    from urllib.request import urlopen    
except ImportError:
    from urllib import urlopen


vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s
ORG:California Raisin Co.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:%s
END:VCARD
'''

qr_url_template = 'https://chart.googleapis.com/chart?cht=qr&chl=%s&choe=UTF-8&chs=300x300'

with open('notes/raisin_team.csv') as contacts_file:
    for line in contacts_file:
        last, first, title, email, phone = line.rstrip().split(',')
        fullname = '%s %s' % (first, last)
        vcard_text = vcard_template % (last, first, fullname, title, phone, email)

        filename = '%s.%s.vcf' % (last, first)
        with open(filename, 'w') as vcard_file:
            vcard_file.write(vcard_text)

        qr_url = qr_url_template % vcard_text
        response = urlopen(qr_url)
        qr_img = response.read()
        
        filename = '%s.%s.png' % (last, first)
        with open(filename, 'wb') as qr_img_file:
            qr_img_file.write(qr_img)
