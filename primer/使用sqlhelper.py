from sqlhelper import db

with db as cursor:
    cursor.exeute('select 1')
