import sys

fout = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\pp_dbf900.txt','w') 

with open(r"D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\dbf900.txt") as pp:
    
    for line in pp:
        rec_id = line[0:2]
        
        if (rec_id == '01') :
            api_cnty = line[2:5]
            api_uniq = line[5:10]
            
        print("XX"+api_cnty+api_uniq+line,file=fout,end='')
            
fout.close()
