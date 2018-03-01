str="""
<html>
    <head>
        <title>Example page</title>
    </head>
    <body>
        <p>Moved to <a href="http://example.org/">example.org</a>
        or <a href="http://example.com/">example.com</a>.</p>
    </body>
</html>"""
country="""<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
tree=ElementTree()
element = ET.fromstring(str)
for item in list(element):
    print item.tag,item.attrib
ctydata = ET.fromstring(country)
print ctydata.tag,ctydata.attrib
for elem in ctydata:
    print elem.attrib["name"] + "\trank\t" + list(elem)[0].text
    for e in list(elem):
        print e.tag +"\t",
        if e.attrib:
            print "name=" + e.attrib['name'] 
        if e.text:
            print e.text
    print 
            
for child in ctydata.iter("rank"):
    print child.attrib,child.text
    
#Xpath example
print ctydata.findall(".")
print ctydata.findall("./country/neighbor")
text= ctydata.findall(".//*[@name='Singapore']/year")
print list(text)[0].text
