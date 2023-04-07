# point to the config folder and sort all views.xml files in one go...

import os
from sortViews import sortAndFormatXmlElems

configPath = r'C:\DevProjects\specify6\config'

formFiles = []

print('reading xml files')
for path, currentDirectory, files in os.walk(configPath):
  for file in files:
    if file.endswith('.views.xml'):
      formFiles.append(os.path.join(path, file))

print('formatting files')
for file in formFiles:
  with open(file, 'r') as f:
    xml = f.read()

  sortedviewsxml = sortAndFormatXmlElems(xml, 'views')
  sortedviewdefsxml = sortAndFormatXmlElems(sortedviewsxml, 'viewdefs')

  with open(file, 'w') as f:
    f.write(sortedviewdefsxml)

print('all done...')