#!/bin/bash
cd /opt/infinera/admin
SCRIPTS_DIR='/opt/infinera/scripts'
db_tools.py --create-tbl

echo "Update the schema of the db table"
db_tools.py --update-schema

db_tools.py --clear-tbl
db_tools.py --insert-board-spec-tbls ${SCRIPTS_DIR}/../etc/json/dtc_boards_spec.json
db_tools.py --insert-board-spec-tbls ${SCRIPTS_DIR}/../etc/json/otc_boards_spec.json
db_tools.py --insert-board-spec-tbls ${SCRIPTS_DIR}/../etc/json/xtc_boards_spec.json
db_tools.py --insert-board-spec-tbls ${SCRIPTS_DIR}/../etc/json/itc_boards_spec.json

if [ -f ${SCRIPTS_DIR}/../etc/json/fmx_boards_spec.json ];then
        db_tools.py --insert-board-spec-tbls ${SCRIPTS_DIR}/../etc/json/fmx_boards_spec.json
fi

if [ -f ${SCRIPTS_DIR}/../etc/json/xtc2_boards_spec.json ];then
        db_tools.py --insert-board-spec-tbls ${SCRIPTS_DIR}/../etc/json/xtc2_boards_spec.json
fi

db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/dtc_spec.json
db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/otc_spec.json
db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/xtc_spec.json
db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/xtc4_spec.json
db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/itc_spec.json
db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/mtc9_spec.json
db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/mtc6_spec.json
if [ -f ${SCRIPTS_DIR}/../etc/json/fmx_spec.json ];then
        db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/fmx_spec.json
fi
if [ -f ${SCRIPTS_DIR}/../etc/json/xtc2_spec.json ];then
        db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/xtc2_spec.json
        db_tools.py --insert-chassis-spec-tbls ${SCRIPTS_DIR}/../etc/json/xtc2e_spec.json
fi

db_tools.py --migrate-tbl
echo "Inserting spec tables about tam/tim/tom ......"
#tom_spec insert must before tim_spec
if [ -f ${SCRIPTS_DIR}/../etc/json/tom_spec.json ];then
        db_tools.py --insert-tom-spec-tbls ${SCRIPTS_DIR}/../etc/json/tom_spec.json
fi

if [ -f ${SCRIPTS_DIR}/../etc/json/tim_spec.json ];then
        db_tools.py --insert-tim-spec-tbls ${SCRIPTS_DIR}/../etc/json/tim_spec.json
fi

if [ -f ${SCRIPTS_DIR}/../etc/json/board_tim_spec.json ];then
        db_tools.py --insert-board-tim-spec-tbls ${SCRIPTS_DIR}/../etc/json/board_tim_spec.json
fi
if [ -f ${SCRIPTS_DIR}/../etc/json/board_tom_spec.json ];then
        db_tools.py --insert-board-tom-spec-tbls ${SCRIPTS_DIR}/../etc/json/board_tom_spec.json
fi
if [ -f ${SCRIPTS_DIR}/../etc/json/eqpt_spec.json ];then
        db_tools.py --insert-eqpt-spec-tbls ${SCRIPTS_DIR}/../etc/json/eqpt_spec.json
fi

echo "---------------------------------------------"
echo "Flush link connection, TIM/TAM/TOM to database,Please wait......"
db_tools.py --flush-db
echo "Done"
