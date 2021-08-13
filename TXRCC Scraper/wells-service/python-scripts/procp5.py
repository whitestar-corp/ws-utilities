import sys
import time

def ValDate(rawDate):
    """ Valdate verifies a date string is all numbers, is 8 characters long, and that strtime approves of it. """
    # Has to be 8 characters long, e.g. 20190527
    
    rawDate = rawDate.strip()
    
    if (rawDate == '00000000') :
        return('')
    
    if (len(rawDate) == 6) :
        rawDate = rawDate+'01'
      
    if (len(rawDate) != 8):
        return('')
       
   # Must be all digits
    if not str.isdigit(rawDate):
        return('')
    
    yy = rawDate[0:4]
    mm = rawDate[4:6]
    dd = rawDate[6:8]
   
    # Sometimes days are not reported and left 0.  Fix this.
    if (dd == '00'):
        dd = '01'
   
    ymd = yy + mm + dd
 
    try:
        t = time.strptime(ymd,"%Y%m%d")
        result = str(t.tm_year) + str(t.tm_mon).zfill(2) + str(t.tm_mday).zfill(2)
        return(result)
    except:
        return('')
    
    return('')

fout01 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\operator\p501.csv','w') 
print("oror_org_operator_number|oror_org_orgnization_name|oror_refiling_required_flag|oror_p5_status|\
oror_hold_mail_code|oror_renewal_letter_code|oror_organization_code|oror_organ_other_comment|\
oror_gatherer_code|oror_org_addr_line1|oror_org_addr_line2|oror_org_add_city|oror_org_addr_state|\
oror_org_addr_zip|oror_org_addr_zip_suffix|oror_location_addr_line1|oror_location_addr_line2|\
oror_location_addr_city|oror_location_addr_state|oror_location_addr_zip|oror_location_addr_suffix|\
oror_date_built|oror_date_inactive|oror_phone_number|oror_refile_notice_month|oror_refile_letter_date|\
oror_refile_notice_date|oror_refile_received_date|oror_last_p5_received_date|oror_other_organization_no|\
oror_filing_problem_date|oror_filing_problem_ltr_code|oror_telephone_verify_flag|oror_op_num_multi_used_flag|\
oror_oil_gatherer_status|oror_gas_gatherer_status|oror_tax_cert|oror_emer_phone_number",file=fout01,end='\n')



with open(r"D:\Users\rwhite\Documents\texas-wells\wells-service\data\operator\orf850.txt") as pp:
    for line in pp:
        tmp = line.replace('|','1')
        line = tmp
        
        rec_id = line[0:1]
        
        # wellbore record type 01 - Root
        if (rec_id == 'A') :
           
            #oror_org_operator_number
            print(line[2:8].strip()+'|',file=fout01,end='')

            #oror_org_orgnization_name
            print(line[8:40].strip()+'|',file=fout01,end='')

            #oror_refiling_required_flag
            print(line[40:41].strip()+'|',file=fout01,end='')

            #oror_p5_status
            print(line[41:42].strip()+'|',file=fout01,end='')

            #oror_hold_mail_code
            print(line[42:43].strip()+'|',file=fout01,end='')

            #oror_renewal_letter_code
            print(line[43:44].strip()+'|',file=fout01,end='')

            #oror_organization_code
            print(line[44:45].strip()+'|',file=fout01,end='')

            #oror_organ_other_comment
            print(line[45:65].strip()+'|',file=fout01,end='')

            #oror_gatherer_code
            print(line[65:70].strip()+'|',file=fout01,end='')

            #oror_org_addr_line1
            print(line[70:101].strip()+'|',file=fout01,end='')

            #oror_org_addr_line2
            print(line[101:132].strip()+'|',file=fout01,end='')

            #oror_org_add_city
            print(line[132:145].strip()+'|',file=fout01,end='')

            #oror_org_addr_state
            print(line[145:147].strip()+'|',file=fout01,end='')

            #oror_org_addr_zip
            print(line[147:152].strip()+'|',file=fout01,end='')

            #oror_org_addr_zip_suffix
            print(line[152:146].strip()+'|',file=fout01,end='')

            #oror_location_addr_line1
            print(line[156:187].strip()+'|',file=fout01,end='')

            #oror_location_addr_line2
            print(line[187:218].strip()+'|',file=fout01,end='')

            #oror_location_addr_city
            print(line[218:231].strip()+'|',file=fout01,end='')

            #oror_location_addr_state
            print(line[231:233].strip()+'|',file=fout01,end='')

            #oror_location_addr_zip
            print(line[233:238].strip()+'|',file=fout01,end='')

            #oror_location_addr_suffix
            print(line[238:242].strip()+'|',file=fout01,end='')

            #oror_date_built
            print(ValDate(line[242:250])+'|',file=fout01,end='')

            #oror_date_inactive
            print(ValDate(line[250:258])+'|',file=fout01,end='')

            #oror_phone_number
            print(line[258:268].strip()+'|',file=fout01,end='')

            #oror_refile_notice_month
            print(line[268:270].strip()+'|',file=fout01,end='')

            #oror_refile_letter_date
            print(ValDate(line[270:278])+'|',file=fout01,end='')

            #oror_refile_notice_date
            print(ValDate(line[278:286])+'|',file=fout01,end='')

            #oror_refile_received_date
            print(ValDate(line[286:294])+'|',file=fout01,end='')

            #oror_last_p5_received_date
            print(ValDate(line[294:302])+'|',file=fout01,end='')

            #oror_other_organization_no
            print(line[302:308].strip()+'|',file=fout01,end='')

            #oror_filing_problem_date
            print(ValDate(line[308:316])+'|',file=fout01,end='')

            #oror_filing_problem_ltr_code
            print(line[316:319].strip()+'|',file=fout01,end='')

            #oror_telephone_verify_flag
            print(line[319:320].strip()+'|',file=fout01,end='')

            #oror_op_num_multi_used_flag
            print(line[320:321].strip()+'|',file=fout01,end='')

            #oror_oil_gatherer_status
            print(line[321:322].strip()+'|',file=fout01,end='')

            #oror_gas_gatherer_status
            print(line[322:323].strip()+'|',file=fout01,end='')

            #oror_tax_cert
            print(line[323:324].strip()+'|',file=fout01,end='')

            #oror_emer_phone_number
            print(line[324:334].strip(),file=fout01,end='')

            #end of line
            print("\n",file=fout01,end='') 
        
fout01.close()
