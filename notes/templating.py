'''
A little demo of templating.
'''


page_template = '''
<html>
    <head>
        <title>%s</title>
        <styles>
            %s
        </styles>
    </head>
    <body>
        %s
    </body>
</html>
'''

item_template = '<li>%s</li>'

names = ['John', 'Paul', 'George', 'Ringo']

items = [item_template % name for name in names]
unordered_list_html = '<ul>%s</ul>' % '\n'.join(items)

page = page_template % ('The Beatles',
                        '',
                        unordered_list_html)
print page
