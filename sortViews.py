#sorts the views and viewdefs in a views.xml file
#moves the name attribute first
#note this replaces the original file, so commit first...
import shlex

fileName = 'common/common.views.xml'

def getElemName(xmlStr):
  nameAttrStart = xmlStr.index('name')
  #now we need the closing quote
  nameStart = xmlStr.index('"', nameAttrStart) + 1
  nameEnd = xmlStr.index('"', nameStart)
  name = xmlStr[nameStart:nameEnd]
  return name.lower()

def quoteAttribute(attr):
  if '=' in attr:
    parts = attr.split('=')
    parts[1] = '"' + parts[1] + '"'
    return '='.join(parts)
  else:
    return attr


#takes a view or viewdef element and puts the name first, sets 'tabs', and removes white space before the end of the tag
def formatFirstElement(elemStr):
  endIndex = elemStr.index('>') #we want the first one, ie the opening tag and it's elements
  tagAndAttrs = elemStr[0:endIndex] #this excludes the closing caret
  theRest = elemStr[(endIndex + 1):len(elemStr)]
  tagAndAttrsList = shlex.split(tagAndAttrs) #use schlex because of attributes with spaces, but then
  tagAndAttrsList = list(map(quoteAttribute, tagAndAttrsList))#apparently we need to remove any empty strings...

  #move the name attr to second place in list
  if not tagAndAttrsList[1].startswith('name'): #this is what we want
    nameAttrIndex = getNameAttrIndex(tagAndAttrsList)
    nameAttr = tagAndAttrsList[nameAttrIndex]
    del tagAndAttrsList[nameAttrIndex]
    tagAndAttrsList.insert(1, nameAttr)

  #add the necessary line breaks and tabs
  tagAndAttrsList[0] = tagAndAttrsList[0] + ' ' #space after the tag
  for ind in range(2, len(tagAndAttrsList)):
    tagAndAttrsList[ind] = '\n' + ('\t' * 3) + tagAndAttrsList[ind]

  tagAndAttrsList.append('>') #add the closing caret for the tag again
  cleanFirstTag = ''.join(tagAndAttrsList)
  updatedElemStr = cleanFirstTag + theRest
  
  return updatedElemStr


def getNameAttrIndex(elemAttrList):
  for (index, item) in enumerate(elemAttrList):
    if(item.startswith('name')):
      return index


def sortAndFormatXmlElems(xmlstr, section):

  openingtag = '<' + section + '>'
  closingtag = '</' + section + '>'

  xmlStart = xmlstr.index(openingtag)
  xmlEnd = xmlstr.index(closingtag) + len(closingtag)
  xmlString = xmlstr[xmlStart:xmlEnd]

  #split into individual views
  elements = []
  searchStart = len(openingtag) + 1
  elemOpeningTag = '<' + section[:-1]
  elemClosingTag = '</' + section[:-1] + '>'
  while searchStart < len(xmlString):
    try:
      elemStart = xmlString.index(elemOpeningTag, searchStart)
    except:
      break

    elemEnd = xmlString.index(elemClosingTag, searchStart) + len(elemClosingTag)
    elem = xmlString[elemStart:elemEnd]
    formattedElem = formatFirstElement(elem)
    elements.append(formattedElem)

    searchStart = elemEnd + 1
  
  elements.sort(key=getElemName)

  #strings are immutable so we have to do this
  firstxml = xmlstr[0:xmlStart]
  lastxml = xmlstr[xmlEnd:]
  newxml = firstxml + openingtag + '\n\n\t\t' + '\n\n\t\t'.join(elements) + '\n\n\t' + closingtag + lastxml

  return newxml