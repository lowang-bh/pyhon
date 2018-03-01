#!/usr/bin/env python
import logging as log
from lxml import etree
from xml.etree.ElementTree import ElementTree
import  sys

def validate(schemaFile, xmlFile):
    try:
        f = open(schemaFile)
        # pylint: disable=no-member
        schemaDoc = etree.parse(f)
        print schemaDoc
        print schemaDoc.getroot()
        schema = etree.XMLSchema(schemaDoc)
        print schema
        f.close()

        f = open(xmlFile)
        xmlDoc = etree.parse(f)
        print xmlDoc
        f.close()
        schema.assert_(xmlDoc)
    except Exception, e:
        log.info(str(e))

        return False

    return True
xml_str="""<?xml version="1.0"?>
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

def xml_pase(xmlFileName):
    tree = ElementTree()
    tree.parse(xmlFileName)
    for child in tree.getroot():
        print (child.tag,child.attrib)
    
    neList = tree.findall("NE")
    print neList
    for s in neList:
        print (s.tag,s.attrib)
        chassislist = list(s)
        for row in chassislist:
            print "for row in chassislist:%s"%row.attrib['Value']
            print row.attrib
            cfgMode = row.get('ConfigMode')
            if cfgMode:
                print "cfgMode is %s\n" %cfgMode
            elem=list(row)[0]
            print  elem,elem.tag,list(row)
            vmlist= list(elem)
            for vm in vmlist:
                print "vm is %s" %vm
                print vm.tag,vm.attrib
                print vm.items()#return (key,value) sequence
                print "list vm:%s" %vm
                for tam in list(vm):
                    print tam.tag,tam.attrib
                


schemaFile = r"testdir\sim_server.xsd"
xmlFile= r"testdir\test.xml"
print schemaFile,xmlFile
print validate(schemaFile, xmlFile)
xml_pase(xmlFile)
