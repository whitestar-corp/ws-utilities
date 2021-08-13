call activate arcgispro-py3-clone
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\get_wellbore.py"
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\get_operator_data.py"
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\pp_wb.py"
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\procwb.py"
python "D:\Users\rwhite\Documents\texas-wells\wells-service\python-scripts\procp5.py"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\loadp5.fmw"
fme "D:\Users\rwhite\Documents\texas-wells\wells-service\fmw\wb2pg.fmw"

