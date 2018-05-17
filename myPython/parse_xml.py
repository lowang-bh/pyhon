#!/usr/bin/python
# coding=UTF-8
'''
Created on Aug 31, 2016

@author: lowang
'''

from xml.etree.ElementTree import ElementTree, iselement
import re, os


def is_CX_card(pon_desc=None, chassis_type=None, card_type=None):
    '''
    '''
    if isinstance(pon_desc, str):
        if pon_desc.startswith("CX-") or pon_desc.startswith("CX_"):
            return True
    elif "CX1200" == chassis_type:
        return True
    elif "XMM2" == card_type:
        return True
    else:
        return False


class TestCaseXMLParse(object):
    '''
    This class provide the basic EQPT and CONNECTION parse of CSIM xml
    '''

    def __init__(self):
        self.ne_data = {}
        self.conn_data = {"IGCC": [], "OSC": [], "SCG": [], "OCH": [], "OCG": [], "FBM": [], "SLTE": []}
        self.all_data = (self.ne_data, self.conn_data)
        self.tree = ElementTree()

    def parse_xml(self, xml_file):
        if not os.path.isfile(xml_file):
            raise Exception("%s does not exist." % xml_file)
        self.tree.parse(xml_file)
        neList = self.tree.findall("NE")
        if not neList:
            global_log.error("No NEs found")
            return None
        # parse all eqpt information
        for ne in neList:
            neName = ne.attrib['Value']
            chassisInfo = self.parse_chassis(ne)
            self.ne_data[neName] = {'dcnIp': ne.attrib['DcnIp'], 'neType': ne.attrib['NeType'],
                                    'chassisInfo': chassisInfo}

        # parse all connection information
        connElems = self.tree.findall("connection")
        conn_list = [list(conn)[0] for conn in connElems]
        for connElem in conn_list:
            conn = self.parse_connect(connElem)
            self.conn_data[conn.keys()[0]].append(conn.values()[0])

    def parse_connect(self, conn_element):
        '''
        '''
        tag = conn_element.tag
        conn_dic = {}
        pa, pb = {}, {}

        if tag == "OSC" or tag == "IGCC":  # osc or igcc
            pointA, pointB = conn_element.find('PointA'), conn_element.find('PointB').find('Board')
            pa['NE'] = pointA.attrib['NE']
            pa['Chassis'] = pointA.attrib['Chassis']
            pa['Board'] = pointA.attrib['Board']
            if "SCH" in pointA.attrib:
                pa["SCH"] = pointA.attrib['SCH']
            pa['dcnIp'] = self.ne_data[pa['NE']]['dcnIp']
            pa['shelfId'] = self.ne_data[pa['NE']]['chassisInfo'][pa['Chassis']]['shelfId']
            pa['chsCategory'] = self.ne_data[pa['NE']]['chassisInfo'][pa['Chassis']]['chsCategory']
            pa['Pon'] = self.ne_data[pa['NE']]['chassisInfo'][pa['Chassis']]['cardInfo'][pa['Board']]['Pon']
            conn_dic['PointA'] = pa
            if pointB is not None:
                pb['NE'] = pointB.attrib['NE']
                pb['Chassis'] = pointB.attrib['Chassis']
                pb['Board'] = pointB.attrib['Board']
                if "SCH" in pointB.attrib:
                    pb["SCH"] = pointB.attrib['SCH']
                pb['dcnIp'] = self.ne_data[pb['NE']]['dcnIp']
                pb['shelfId'] = self.ne_data[pb['NE']]['chassisInfo'][pb['Chassis']]['shelfId']
                pb['chsCategory'] = self.ne_data[pb['NE']]['chassisInfo'][pb['Chassis']]['chsCategory']
                pb['Pon'] = self.ne_data[pb['NE']]['chassisInfo'][pb['Chassis']]['cardInfo'][pb['Board']]['Pon']
            else:
                pb['Vlan'] = conn_element.find('TRUNK-VLAN').text
            conn_dic['PointB'] = pb

            return {tag: conn_dic}
        elif tag == "OCG" or tag == "OCH":
            pointA, pointB = conn_element.find('PointA'), conn_element.find('PointB')
        else:
            pointA, pointB = conn_element.find('remote'), conn_element.find('local')

        # OPSIM connction information
        pa['NE'], pb['NE'] = pointA.attrib['NE'], pointB.attrib['NE']
        pa['Chassis'], pb['Chassis'] = pointA.attrib['Chassis'], pointB.attrib['Chassis']
        pa['Board'], pb['Board'] = pointA.attrib['Board'], pointB.attrib['Board']
        pa['port'] = pointA.attrib['port'] if 'port' in pointA.attrib else ""
        pb['port'] = pointB.attrib['port'] if 'port' in pointB.attrib else ""
        # end-point Node infor
        pa['dcnIp'] = self.ne_data[pa['NE']]['dcnIp']
        pa['shelfId'] = self.ne_data[pa['NE']]['chassisInfo'][pa['Chassis']]['shelfId']
        pa['chsCategory'] = self.ne_data[pa['NE']]['chassisInfo'][pa['Chassis']]['chsCategory']
        pb['dcnIp'] = self.ne_data[pb['NE']]['dcnIp']
        pb['shelfId'] = self.ne_data[pb['NE']]['chassisInfo'][pb['Chassis']]['shelfId']
        pb['chsCategory'] = self.ne_data[pb['NE']]['chassisInfo'][pb['Chassis']]['chsCategory']

        conn_dic['PointA'], conn_dic['PointB'] = pa, pb
        return {tag: conn_dic}

    def parse_chassis(self, ne_element):
        if not iselement(ne_element):
            raise Exception("%s is not an element." % ne_element)
        chassis_list = list(ne_element)
        chassisInfo = {}
        for chassis in chassis_list:
            chassisName = chassis.attrib['Value']
            chs_element = list(chassis)[0]
            cardInfo = self.parse_cards(chs_element)
            chassisInfo[chassisName] = {'shelfId': chassis.attrib['aid'], 'chassisNo': chassis.attrib['CHASSERNO'],
                                        'chsCategory': chs_element.tag, 'cardInfo': cardInfo}
        return chassisInfo

    def parse_cards(self, chassis_element):
        if not iselement(chassis_element):
            raise Exception("%s is not an element." % chassis_element)

        card_list = list(chassis_element)
        card_info = {}
        for card in card_list:
            cardName = card.attrib['Value']
            card_info[cardName] = {"aid": card.attrib['aid'], "Pon": card.attrib['PON']}

        return card_info


'''
Created on Mar 10, 2017

@author: lowang
xml parse return conn_data is organized as following:
{'IGCC': [     
            {'PointA': {'dcnIp': '10.220.36.192', 'Chassis': 'Chassis01', 'shelfId': '1', 'NE': 'Node4', 'Board': 'OLM 1-A-1'}, 
             'PointB': {'Vlan': '1001'}
            }, 
            {'PointA': {'dcnIp': '10.220.36.193', 'Chassis': 'Chassis14', 'shelfId': '1', 'NE': 'Node5', 'Board': 'XMM 14-A-1'},
             'PointB': {'dcnIp': '10.220.36.194', 'Chassis': 'Chassis15', 'shelfId': '1', 'NE': 'Node6', 'Board': 'XMM 15-A-1'}
            }
          ],
'SCG': [
            {'PointA': {'shelfId': '1', 'NE': 'Node4', 'Chassis': 'Chassis01', 'dcnIp': '10.220.36.192', 'port': '', 'Board': 'OLM 1-A-1'},
             'PointB': {'shelfId': '4', 'NE': 'Node4', 'Chassis': 'Chassis04', 'dcnIp': '10.220.36.192', 'port': '1', 'Board': 'FRM4D 4-A-4'}
            }
       ]
}

'''


import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs

def xml_data_combination(xml_parsed_data1, xml_parsed_data2):
    '''
    combine two xml's connection data
    '''
    if not isinstance(xml_parsed_data1, TestCaseXMLParse) or not isinstance(xml_parsed_data2, TestCaseXMLParse):
        global_log.error("Iput parameters is incorrect, should be instance of TestCaseXMLParse")
        return None

    for conn_type in xml_parsed_data1.conn_data:
        #IGCC or OSC merge to one node
        if conn_type == "OSC" or conn_type == "IGCC":
            osc_igcc_list1 = xml_parsed_data1.conn_data[conn_type]
            osc_igcc_list2 = xml_parsed_data2.conn_data[conn_type]
            for conn1 in osc_igcc_list1:
                if "Vlan" in conn1['PointB']:
                    vlanId = conn1['PointB']['Vlan']
                else:
                    continue
                for conn2 in osc_igcc_list2:
                    if "Vlan" in conn2['PointB'] and conn2['PointB']['Vlan'] == vlanId:
                        conn1['PointB'] = conn2['PointA']
                        conn1['PointB']['Vlan'] = vlanId
                        break
            for conn2 in osc_igcc_list2:
                if "Vlan" not in conn2['PointB']:
                    xml_parsed_data1.conn_data[conn_type].append(conn2)
        # Opsim merge
        else:
            xml_parsed_data1.conn_data[conn_type].extend(xml_parsed_data2.conn_data[conn_type])
    for ne in xml_parsed_data2.ne_data:
        if ne not in xml_parsed_data1.ne_data:
            xml_parsed_data1.ne_data[ne] = xml_parsed_data2.ne_data[ne]

    return xml_parsed_data1

def conn_data_combination(xml_file_list):
    '''
    merge the xml file data. It support multiple xmls
    '''
    if not isinstance(xml_file_list, list):
        global_log.error("Input xml file incorrect: is should be a list")
        return None
    xml_file1 = xml_file_list[0]
    xml_data_base = TestCaseXMLParse()
    xml_data_base.parse_xml(xml_file1)
    for xml_file2 in xml_file_list[1:]:
        xml_parsed_data2 = TestCaseXMLParse()
        xml_parsed_data2.parse_xml(xml_file2)
        xml_data_base = xml_data_combination(xml_data_base, xml_parsed_data2)
    return xml_data_base

# CombineData = conn_data_combination(XmlFileList)

if __name__ == "__main__":
    import os
    curdir = os.getcwd()
    xml_file1 = os.path.join(curdir, "../env/gnmxml/csim_regression/csim_newest_csim_36.191.xml")
    xml_file2 = os.path.join(curdir, "../env/gnmxml/csim_regression/csim_newest_csim_33.41.xml")
    XmlFileList = [xml_file1, xml_file2]
    CombineData = conn_data_combination(XmlFileList)
    xml_parsed_data1 = TestCaseXMLParse()
    with Timer() as t:
        xml_parsed_data1.parse_xml(xml_file1)
    print "==>> elasped time: %s s" % t.secs
    xml_parsed_data2 = TestCaseXMLParse()
    xml_parsed_data2.parse_xml(xml_file2)
    for key, value in sorted(xml_parsed_data1.conn_data.items()):
        for conns in value:
            print conns
    for key, value in sorted(xml_parsed_data2.conn_data.items()):
        for conns in value:
            print conns
    # test = xml_data_combination(xml_parsed_data1, xml_parsed_data2)
    test = CombineData
    for ne in sorted(test.ne_data):
        print ne, test.ne_data[ne]['dcnIp']
    for key, value in sorted(test.conn_data.items()):
        print key
        for conns in value:
            print conns
