#!/usr/bin/python
from time import gmtime, strftime, time
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak, Paragraph, Spacer
from itertools import izip_longest


styles = getSampleStyleSheet()
def feed(ducks, min_eggs=0, conv=1000/2.2, base_feed=0.3, egg_feed=0.1):
    return map(
        lambda x: '%d' % ((ducks*base_feed + x*egg_feed)*conv,),
        xrange(min_eggs, ducks+1)
        )

def feed_table(ducks, min_ducks=1, min_eggs=0, conv=1000/2.2):
    return [['b\e'] + range(min_eggs, ducks+1)] + map(lambda x: [x] + feed(x, min_eggs, conv=conv),
            xrange(ducks, min_ducks - 1, -1))


doc = SimpleDocTemplate("feeding.pdf", pagesize = landscape(letter))
elements = []
ts = TableStyle([
    ('FONT', (0,0), (-1,-1), 'Helvetica', 8),
    ('ALIGN', (0,0), (-1,-1), 'RIGHT'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black)
    ])

p = Paragraph('Eggs vs Ducks Feed Table: Grams', styles['Heading1'])
elements.append(p)

t = Table(feed_table(20))
t.setStyle(ts)

elements.append(t)
elements.append(PageBreak())
elements.append(Paragraph('Eggs vs Ducks Feed Table: Ounces', styles['Heading1']))

t = Table(feed_table(20,conv=16))
t.setStyle(ts)
elements.append(t)

doc.build(elements)
