#!/usr/bin/python
from time import gmtime, strftime, time
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from itertools import izip_longest

def dates(starttime = time(), count = 20, repeat = 2, decorate = None):
    if decorate is None:
        decorate = [ ('', '') ] * repeat
    for i in xrange(0, count//repeat):
        o = strftime('%Y %b %d', gmtime(starttime + 24*60*60*i))
        for j in xrange(0, repeat):
            yield decorate[j][0] + o + decorate[j][1]

def grouper(iterable, n, fillvalue=None):
    'Collect data into fixed-lenght chunks or blocks'
    # grouper('ABCDEFG', 3, 'x') -> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def dates_table(starttime = time(), rows=26, columns=3):
    decorate = [
            ('    ', ' >>>'),
            ('<<< ', '    ')
            ]
    d = dates(starttime=starttime, count=rows*columns, repeat=2, decorate=decorate)
    g = grouper(d, rows)
    return zip(*g)

doc = SimpleDocTemplate("egg_dates.pdf", pagesize = letter)
elements = []
t =Table(dates_table())
t.setStyle(TableStyle([
    ('FONT', (0,0), (-1,-1), 'Courier-Bold', 15),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black)
    ])) 

elements.append(t)

doc.build(elements)
