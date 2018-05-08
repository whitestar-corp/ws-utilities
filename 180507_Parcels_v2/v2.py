import psycopg2
import PeteSql
import sys

# settings things
_verbose=True
_dontExecute=False
_exitOnError=True

# read tables from a file called tables
fname="tables.txt"
with open(fname) as f:
    _tables = f.readlines()

# connect to staging 
try:
    sta_conn = psycopg2.connect(dbname='postgis20', user='postgres', host='pg-staging.whitestar.com', password='M;B4at%L4gkUmG' , port='7457')
    sta_conn.autocommit = True # needed for vacuum analyze to work
   
except:
    print "Could not connect to database!"
    exit()

# get a cursor
sta_cur = sta_conn.cursor()

# connect to the class that provides SQL statements
psql = PeteSql.PeteSql()

# for each table, replace the table names and execute each query
for table in _tables:

    orig_table = table.rstrip()
    out_table = orig_table + "_v2"

    if not _dontExecute:
	    print("Previewing " + orig_table)
    else:
	    print "Executing for " + orig_table
    
    for query in psql._queries:
        query = query.replace('<orig_table>',orig_table)
        query = query.replace('<out_table>', out_table)

        if _verbose:
        	print("\n" + query)

        try:
            if not _dontExecute:
		        sta_cur.execute(query)
		        sta_conn.commit()
		        print 'OK!'
        except:
			print "Error executing " + query  +"\n"
			print sys.exc_info()

			if _exitOnError:
				exit()