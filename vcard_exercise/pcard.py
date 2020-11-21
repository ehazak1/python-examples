'''
Making vCards for the brother-in-law
'''

import urllib

vcard_template = '''
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

        vcard_filename = '%s_%s.vcf' % (last, first)
        with open(vcard_filename, 'w') as vcard_fhandle:
            vcard_fhandle.write(vcard_text.lstrip())

        qr_url = qr_url_template % vcard_text
        response = urllib.urlopen(qr_url)
        qr_img = response.read()
        qr_img_name = '%s_%s.png' % (last, first)
        with open(qr_img_name, 'wb') as qr_filename:
            qr_filename.write(qr_img)
            
