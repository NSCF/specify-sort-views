import os
import click
from sortViews import sortAndFormatXmlElems

@click.command(help="A utility for formatting Specify views.xml files so they are easier to work with")
@click.option('--file', help='The target file name (and relative path)')

def format(file):

  if not file:
    print('a file name is required, try sortviews --help')
    return
    
  if os.path.isfile(file):

    #just check we're working with a views.xml file
    if not file.endswith('views.xml'):
      print('we can only format Specify forms xml files')
      return

    with open(file, 'r') as f:
      xml = f.read()

    sortedviewsxml = sortAndFormatXmlElems(xml, 'views')
    sortedviewdefsxml = sortAndFormatXmlElems(sortedviewsxml, 'viewdefs')

    with open(file, 'w') as f:
      f.write(sortedviewdefsxml)

    print('all done')
  else:
    print('please provide a valid filename')
  
  return

if __name__ == '__main__':
  format()