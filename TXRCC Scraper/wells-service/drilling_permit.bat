call activate arcgispro-py3-clone
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\get_drilling_permit_master.py"
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\pb_permit.py"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_casing.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_liner.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_perforations.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_formation.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_remarks.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_squeeze.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_tubing.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_water.fmw"
psql -h pg.whitestar.com -U postgres -d postgis20 -p 7457 < D:\Users\rwhite\Documents\texas-wells\wells-service\sql-scripts\swapout_tx_permits.sql