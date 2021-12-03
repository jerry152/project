#!/bin/bash

db="boxing.sqlite"
rm -f ${db}
touch ${db}

sqlite3 ${db} < creatingDataBase.sql

