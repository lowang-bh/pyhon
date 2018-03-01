#!/usr/bin/env python
from Utils.log import log
from sqlobject.col import IntCol, StringCol
from sqlobject.dberrors import OperationalError
from sqlobject.main import SQLObjectNotFound

from Orm.db_tables import TimSpecTbl, TomSpecTbl, BoardTimSpecTbl, \
    BoardTomSpecTbl, TimTomSpecTbl, VmTbl, SubSlotTbl, PortTbl, EqptSpecTbl
from Orm.db_utils import insert_tom_spec_tbls, insert_tim_spec_tbls, \
    insert_board_tim_spec_tbls, insert_board_tom_spec_tbls, \
    insert_eqpt_spec_tbls
from Orm.update_tim_tom import get_plugged_tam_from_syspvt, \
    get_plugged_tim_from_syspvt, get_plugged_tom_from_syspvt



def create_tables():
    """
    Clear the the spec table: deletes all entries in the table
    """
    #update_db_schema()
    TimSpecTbl.dropTable(ifExists=True,dropJoinTables=True) 
    TimSpecTbl.createTable(ifNotExists=True, createJoinTables=True)
    TomSpecTbl.dropTable(ifExists =True)
    TomSpecTbl.createTable(ifNotExists=True, createJoinTables=True)
     
    TimTomSpecTbl.dropTable(ifExists=True)
    """This work,just clear the data, but ID will keep increase next time, not increase from 1"""
    #TimTomSpecTbl.clearTable(clearJoinTables=True)
    TimTomSpecTbl.createTable(ifNotExists=True, createJoinTables = False)
    BoardTimSpecTbl.dropTable(ifExists=True)
    BoardTimSpecTbl.createTable(ifNotExists=True, createJoinTables=False)    
    BoardTomSpecTbl.dropTable(ifExists=True)
    BoardTomSpecTbl.createTable(ifNotExists=True, createJoinTables=False)



tom_json_file="/opt/infinera/etc/json/tom_spec.json"
tim_json_file="/opt/infinera/etc/json/tim_spec.json"
eqpt_json_file="/opt/infinera/etc/json/eqpt_spec.json"
board_tim_json_file="/opt/infinera/etc/json/board_tim_spec.json"
board_tom_json_file="/opt/infinera/etc/json/board_tom_spec.json"
xtc_board_json_file="/opt/infinera/etc/json/xtc_boards_spec.json" 
xtc2_board_json_file="/opt/infinera/etc/json/xtc2_boards_spec.json" 

create_tables()
insert_tom_spec_tbls(tom_json_file)
insert_tim_spec_tbls(tim_json_file)
BoardTimSpecTbl.dropTable(ifExists=True)
BoardTimSpecTbl.createTable(ifNotExists=True, createJoinTables=False) 
insert_board_tim_spec_tbls(board_tim_json_file)
BoardTomSpecTbl.dropTable(ifExists=True)
BoardTomSpecTbl.createTable(ifNotExists=True, createJoinTables=False)
insert_board_tom_spec_tbls(board_tom_json_file)
EqptSpecTbl.dropTable(ifExists=True)
EqptSpecTbl.createTable(ifNotExists=True)
insert_eqpt_spec_tbls(eqpt_json_file)
if 1:
    SubSlotTbl.dropTable(ifExists=True)
    SubSlotTbl.createTable(ifNotExists=True)
     
    PortTbl.dropTable(ifExists=True)
    PortTbl.createTable(ifNotExists=True)
    
    get_plugged_tim_from_syspvt()
    get_plugged_tam_from_syspvt()
    get_plugged_tom_from_syspvt()

var = VmTbl.selectBy(id=78)
print list(var)
subSlotVar=SubSlotTbl.selectBy(id=1)
print subSlotVar
print "SUCCESS"
if 0:
    try:
        tom_var=TomSpecTbl.byMinorTypeName("TOM-10G-IR2") 
    except SQLObjectNotFound,e:
        print e
        tom_var= TomSpecTbl.byTomPon("TOM-10G-IR2")
        
        print tom_var  
      
    for i in range(1,48):
        print "\""+str(i)+"\",",
    tom= TomSpecTbl.selectBy(majorTypeName="CFP")    
    print type(tom)
    for item in list(tom):
        print item.minorTypeName,
    print "\n"
    value="TIM1x100GE"
    timspec=TimSpecTbl.byName(value)
    print type(timspec)
    print timspec.id    
     
    timspec=TimSpecTbl.select(TimSpecTbl.q.name == value)
    print type(timspec)
    print list(timspec)[0].id