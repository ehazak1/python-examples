#! /usr/bin/env python
from __future__ import print_function
from highlight import analyze_python, build_html_page
import os, glob, cgi, shutil, argparse
import sys
from datetime import datetime


setup_instructions_html = """\
    Please download and install Python version
    {version.major}.{version.minor}.{version.micro}.
    Once installed, please run the IDLE Python IDE.
    Even if you already have Python installed, let's standardize with
    <a href='http://bit.ly/py-install{version.major}'>
      Raymond's instructions for installing Python and running IDLE
    </a>.
""".format(version=sys.version_info)


index_template = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
          "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
    <meta http-equiv="refresh" content="15">
    <link rel="shortcut icon" href="http://www.python.org/favicon.ico">
    <title> {title} </title>
    <style type="text/css">
      {css}
    </style>
  </head>
  <body>
    <h2>Python</h2>
    Taught by Michael Selik<br/>
    <a href='mailto:mike@selik.org'>mike@selik.org</a><br/>
    <p>
    <em>Copyright &copy; %d Raymond Hettinger</em><br/>
    <em>Private Content. Please do not redistribute.</em>
    </p>

    <h3>Machine Setup</h3>
    %s

    <h3>Today's Files</h3>
    If you get lost,
    these files will keep you up-to-the-minute with the instructor.<br />
    Run the 'download.py' script at the command prompt<br />
    or execute the script in IDLE to download all dependencies.
    <pre>$ python download.py</pre>
    <ul>
    {links}
    </ul>
  </body>
</html>
""" % (datetime.now().year, setup_instructions_html)


module_template = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
          "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
    <title> {title} </title>
    <link rel="shortcut icon" href="http://www.python.org/favicon.ico">
    <style type="text/css">
      {css}
    </style>
  </head>
  <body>
    {body}
  </body>
</html>
"""


def is_current(sourcefile, destfile):
    'Destination file exists and was modified more recently than source file'
    try:
        return os.stat(destfile).st_mtime > os.stat(sourcefile).st_mtime
    except OSError:
        return False


def publish_pyfile(sourcefile, destfile):
    with open(sourcefile) as sf:
        source = sf.read()
    tokens = analyze_python(source)
    html = build_html_page(tokens, module_template, title=sourcefile)
    with open(destfile, 'w') as df:
        df.write(html)


def publish_index(filename, index, css='body {background-color:#F8FFFF;}'):
    """ Write index.html to destination directory.
    `index` is a dictionary, src --> label, for creating html links.
    """
    fmt = '<li><a href="%s">%s</a></li>'
    links = '\n'.join(fmt % (src, lbl) for src, lbl in sorted(index.items()))
    html = index_template.format(title='Python', css=css, links=links)
    with open(filename, 'w') as f:
        f.write(html)


def publish(destination, filenames=None, linksfile='links.txt'):
    ''' Write HTML versions of Python code files to destination directory.
    Grabs all '.py' files and 'links.txt'
    from current working directory by default.
    '''
    try:
        os.mkdir(destination)
    except OSError:
        pass

    destfile = os.path.join(destination, linksfile)
    if not is_current(linksfile, destfile):
        print(time.ctime(), 'Updating', linksfile, '-->', destfile)
        shutil.copy(linksfile, destination)

    if filenames is None:
        filenames = glob.glob('*.py')

    index = {}
    updates = 0

    for sourcefile in filenames:
        htmlfile = os.path.splitext(os.path.basename(sourcefile))[0] + '.html'
        destfile = os.path.join(destination, htmlfile)
        if not is_current(sourcefile, destfile):
            print(time.ctime(), 'Updating', sourcefile, '-->', destfile)
            publish_pyfile(sourcefile, destfile)
            updates += 1
        index[htmlfile] = sourcefile

    indexfile = os.path.join(destination, 'index.html')
    if updates or not os.path.exists(indexfile):
        print('New index:', indexfile)
        publish_index(indexfile, index)

    return indexfile, updates


def parse_args(*args, **kwargs):
    help_text = 'Publish .py files as .html, with index'
    parser = argparse.ArgumentParser(description=help_text)
    parser.add_argument('pubdir',
                        help='directory to write html')
    parser.add_argument('--clear', nargs='?', default=False,
                        help='delete existing files and build from scratch')
    parser.add_argument('--loop', nargs='?', default=0, type=int,
                        help='publish changes every X seconds, must be > 3')
    return parser.parse_args(*args, **kwargs)


if __name__ == '__main__':
    import sys, time
    args = parse_args()

    if args.clear is not False:
        print('Removing files from', args.pubdir)
        filenames = os.listdir(args.pubdir)
        for path in (os.path.join(args.pubdir, name) for name in filenames):
            print('deleting', path)
            try:
                os.unlink(path)
            except Exception as e:
                print(e)

    print('Starting in:', os.getcwd())
    print('Writing to:', args.pubdir)
    publish(args.pubdir)

    if args.loop > 3:
        while True:
            publish(args.pubdir)
            try:
                time.sleep(args.loop)
            except KeyboardInterrupt as e:
                print('...Stopping')
                sys.exit(0)
