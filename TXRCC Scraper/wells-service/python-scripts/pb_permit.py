import sys, string
import time
import os

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


fout = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\drilling-permit\perm02.csv','w')

print("da_permit_number|da_permit_sequence_number|da_permit_county_code|da_permit_lease_name|da_permit_district|\
da_permit_well_number|da_permit_total_depth|da_permit_operator_number|da_type_application|\
da_other_explanation|da_address_unique_number|da_zip_code_prefix|da_zip_code_suffix|da_fiche_set_number|\
da_onshore_county|da_received_date|da_permit_issued_date|da_permit_amended_date|da_permit_extended_date|\
da_permit_spud_date|da_permit_surface_casing_date|da_well_status|da_permit_well_status_date|\
da_permit_expired_date|da_permit_cancelled_date|da_cancellation_reason|da_p12_filed_flag|\
da_substandard_acreage_flag|da_rule_36_flag|da_h9_flag|da_rule_37_case_number|da_rule_38_docket_number|\
da_location_formation_flag|da_old_location|da_surface_section|da_surface_block|da_surface_survey|\
da_surface_abstract|da_surface_acres|da_surface_miles_from_city|da_surface_direction_from_city|\
da_surface_nearest_city|da_surface_lease_feet_1|da_surface_lease_direction_1|da_surface_lease_feet_2|\
da_surface_lease_direction_2|da_old_surface_lease_distance|da_surface_survey_feet_1|\
da_surface_survey_direction_1|da_surface_survey_feet_2|da_surface_survey_direction_2|\
da_old_survey_distance|da_nearest_well|da_nearest_well_feet|da_nearest_well_direction|\
da_nearest_well_format|da_final_update|da_cancelled_flag|da_spud_in_flag|da_directional_well_flag|\
da_sidetrack_well_flag|da_moved_indicator|da_permit_conv_issued_date|da_rule_37_granted_code|\
da_horizontal_well_flag|da_duplicate_permit_flag|da_nearest_lease_line|api_number",file=fout,flush='yes',sep="|",end="\n")


with open (r"D:\Users\rwhite\Documents\texas-wells\wells-service\data\drilling-permit\daf804.txt") as f:
    
    for line in f:
        rec_no = line[0:2]      
       
        if (rec_no == '02') :
        
            da_permit_number =                    line[2:9]
            da_permit_sequence_number =           line[9:11]
            da_permit_county_code =               line[11:14]
            da_permit_lease_name =                line[14:46]
            da_permit_district =                  line[46:48]
            da_permit_well_number =               line[48:54]
            da_permit_total_depth =               line[54:59]
            da_permit_operator_number =           line[59:65]
            da_type_application =                 line[65:67]
            da_other_explanation =                line[67:97]
            da_address_unique_number =            line[97:103]
            da_zip_code_prefix =                  line[103:108]
            da_zip_code_suffix =                  line[108:112]
            da_fiche_set_number =                 line[112:118]
            da_onshore_county =                   line[118:121]
            da_received_date =                    line[121:129]
            da_permit_issued_date =               line[129:137]
            da_permit_amended_date =              line[137:145]
            da_permit_extended_date =             line[145:153]
            da_permit_spud_date =                 line[153:161]
            da_permit_surface_casing_date =       line[161:169]
            da_well_status =                      line[169:170]
            da_permit_well_status_date =          line[170:178]
            da_permit_expired_date =              line[178:186]
            da_permit_cancelled_date =            line[186:194]
            da_cancellation_reason =              line[194:224]
            da_p12_filed_flag =                   line[224:225]
            da_substandard_acreage_flag =         line[225:226]
            da_rule_36_flag =                     line[226:227]
            da_h9_flag =                          line[227:228]
            da_rule_37_case_number =              line[228:235]
            da_rule_38_docket_number =            line[235:242]
            da_location_formation_flag =          line[242:243]
            da_old_location =                     line[243:295]
            
            if (da_location_formation_flag == 'N') :
                da_surface_section =                  line[243:251]
                da_surface_block =                    line[251:261]
                da_surface_survey =                   line[261:316]
                da_surface_abstract =                 line[316:322]
                try :
                    da_surface_acres =                    str(float(line[325:333]) / 100.0)
                except :
                    da_surface_acres = '0.0'
                da_surface_miles_from_city =          str(float(line[333:339]) / 100.0)
                da_surface_direction_from_city =      line[339:345]
                da_surface_nearest_city =             line[345:358]
                da_surface_lease_feet_1 =             str(float(line[358:366]) / 100.0)
                da_surface_lease_direction_1 =        line[366:379]
                da_surface_lease_feet_2 =             str(float(line[379:387]) / 100.0)
                da_surface_lease_direction_2 =        line[387:400]
                da_surface_survey_feet_1 =            str(float(line[400:408]) / 100.0)
                da_surface_survey_direction_1 =       line[408:421]
                da_surface_survey_feet_2 =            str(float(line[421:429]) / 100.0)
                da_surface_survey_direction_2 =       line[429:442]
                da_old_surface_lease_distance =       ''
                da_old_survey_distance =              ''
            else :
                da_old_surface_lease_distance =       line[358:386]
                da_old_survey_distance        =       line[400:428]
                da_nearest_well_format =              line[470:471]
                da_surface_section =                  ''
                da_surface_block =                    ''
                da_surface_survey =                   ''
                da_surface_abstract =                 ''
                da_surface_acres =                    ''
                da_surface_miles_from_city =          ''
                da_surface_direction_from_city =      ''
                da_surface_nearest_city =             ''
                da_surface_lease_feet_1 =             ''
                da_surface_lease_direction_1 =        ''
                da_surface_lease_feet_2 =             ''
                da_surface_lease_direction_2 =        ''
                da_surface_survey_feet_1 =            ''
                da_surface_survey_direction_1 =       ''
                da_surface_survey_feet_2 =            ''
                da_surface_survey_direction_2 =       ''
            
            da_nearest_well =                         line[442:470]
            if (da_nearest_well_format == 'N') :
                da_nearest_well_feet =                line[442:450]
                da_nearest_well_direction =           line[450:463]
            else :
                da_nearest_well_feet =                ''
                da_nearest_well_direction =           ''                
                
            da_final_update =                     line[471:479]
            da_cancelled_flag =                   line[479:480]
            da_spud_in_flag =                     line[480:481]
            da_directional_well_flag =            line[481:482]
            da_sidetrack_well_flag =              line[482:483]
            da_moved_indicator =                  line[483:484]
            da_permit_conv_issued_date =          line[484:492]
            da_rule_37_granted_code =             line[492:493]
            da_horizontal_well_flag =             line[493:494]
            da_duplicate_permit_flag =            line[494:495]
            da_nearest_lease_line =               line[495:502]
            api_number =                          line[502:510]
            
            
            print (da_permit_number.strip(),\
            da_permit_sequence_number.strip(),\
            da_permit_county_code.strip(),\
            da_permit_lease_name.strip(),\
            da_permit_district.strip(),\
            da_permit_well_number.strip(),\
            da_permit_total_depth.strip(),\
            da_permit_operator_number.strip(),\
            da_type_application.strip(),\
            da_other_explanation.strip(),\
            da_address_unique_number.strip(),\
            da_zip_code_prefix.strip(),\
            da_zip_code_suffix.strip(),\
            da_fiche_set_number.strip(),\
            da_onshore_county.strip(),\
            da_received_date.strip(),\
            ValDate(da_permit_issued_date.strip()),\
            ValDate(da_permit_amended_date.strip()),\
            ValDate(da_permit_extended_date.strip()),\
            ValDate(da_permit_spud_date.strip()),\
            ValDate(da_permit_surface_casing_date.strip()),\
            da_well_status.strip(),\
            ValDate(da_permit_well_status_date.strip()),\
            ValDate(da_permit_expired_date.strip()),\
            ValDate(da_permit_cancelled_date.strip()),\
            da_cancellation_reason.strip(),\
            da_p12_filed_flag.strip(),\
            da_substandard_acreage_flag.strip(),\
            da_rule_36_flag.strip(),\
            da_h9_flag.strip(),\
            da_rule_37_case_number.strip(),\
            da_rule_38_docket_number.strip(),\
            da_location_formation_flag.strip(),\
            da_old_location.strip(),\
            da_surface_section.strip(),\
            da_surface_block.strip(),\
            da_surface_survey.strip(),\
            da_surface_abstract.strip(),\
            da_surface_acres.strip(),\
            da_surface_miles_from_city.strip(),\
            da_surface_direction_from_city.strip(),\
            da_surface_nearest_city.strip(),\
            da_surface_lease_feet_1.strip(),\
            da_surface_lease_direction_1.strip(),\
            da_surface_lease_feet_2.strip(),\
            da_surface_lease_direction_2.strip(),\
            da_old_surface_lease_distance.strip(),\
            da_surface_survey_feet_1.strip(),\
            da_surface_survey_direction_1.strip(),\
            da_surface_survey_feet_2.strip(),\
            da_surface_survey_direction_2.strip(),\
            da_old_survey_distance.strip(),\
            da_nearest_well.strip(),\
            da_nearest_well_feet.strip(),\
            da_nearest_well_direction.strip(),\
            da_nearest_well_format.strip(),\
            ValDate(da_final_update.strip()),\
            da_cancelled_flag.strip(),\
            da_spud_in_flag.strip(),\
            da_directional_well_flag.strip(),\
            da_sidetrack_well_flag.strip(),\
            da_moved_indicator.strip(),\
            ValDate(da_permit_conv_issued_date.strip()),\
            da_rule_37_granted_code.strip(),\
            da_horizontal_well_flag.strip(),\
            da_duplicate_permit_flag.strip(),\
            da_nearest_lease_line.strip(),\
            api_number.strip(),\
            file=fout,flush='yes',sep="|",end="\n")
            
            
fout.close()
f.close()


#printable = set(string.printable)
#with open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\drilling-permit\perm02_junk.csv','r') as infile, \
#open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\drilling-permit\perm02.csv', 'w') as outfile:
    #for line in infile:
        #data = ''.join(filter(lambda x: x in printable, line))
        #outfile.write(data)
#os.remove(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\drilling-permit\perm02_junk.csv')       
