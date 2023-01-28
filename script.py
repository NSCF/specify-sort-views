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
      click.echo('we can only format Specify forms xml files')
      return

    with open(file, 'r') as f:
      xml = f.read()

    sortedviewsxml = sortAndFormatXmlElems(xml, 'views')
    sortedviewdefsxml = sortAndFormatXmlElems(sortedviewsxml, 'viewdefs')

    with open(file, 'w') as f:
      f.write(sortedviewdefsxml)

    click.echo('all done')
  else:
    click.echo('please provide a valid filename')
  
  return

if __name__ == '__main__':
  format()