import re
from docx import Document
document = Document()
mcl = open('cover_letter')
readFile = mcl.read()
content = re.findall(r'\S+|\s', readFile)

copies = input('Number of Cover Letters: ')
default_city = input('Default city: ')
default_website = input('Default website: ')
if not copies: 
    copies = 1

for copy in range(copies):
    company = input('Enter company name: ') + ','
    city = input('Enter city name: ')
    website = input('Enter website name: ')
    if not city:
        city = default_city
    if not website:
        website = default_website
    content[content.index('COMPANY,')] = company
    content[content.index('CITY')] = city
    content[content.index('WEBSITE')] = website
    contentString = ''.join(content)

    newCoverLetter = open('Hood_CoverLetter_%s' % company[:-1], 'w')
    newCoverLetter.write(contentString)
    newCoverLetter.close()
    document.add_paragraph(contentString)
    document.save('Hood_CoverLetter_%s.docx' % company[:-1])

    
