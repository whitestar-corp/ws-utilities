call activate arcgispro-py3-clone
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\get_wells.py"
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\get_api.py" 
python "D:\Users\rwhite\Documents\texas-wells\piplines\python-scripts\get_pipe.py"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\giswell2pg.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\loadtxapi.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits_bh.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\well_dem_intersector_and_preprocessor.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\permits.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\loadpipelines.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\cum_merge.fmw"
psql -h pg.whitestar.com -U postgres -d postgis20 -p 7457 < D:\Users\rwhite\Documents\texas-wells\wells-service\sql-scripts\calculate_nwells_for_texas.sql
psql -h pg.whitestar.com -U postgres -d postgis20 -p 7457 < D:\Users\rwhite\Documents\texas-wells\wells-service\sql-scripts\swapout_tx_header.sql



