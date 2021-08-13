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

fout01 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb01_junk.csv','w') 
print("wb_api|wb_nxt_avail_suffix|wb_nxt_avail_hole_chge_nbr|wb_field_district|\
wb_res_cnty_code|wb_orig_cmpl_cc|wb_orig_compl_date|wb_total_depth|wb_valid_fluid_level|wb_certification_revoked_date|\
wb_certification_denial_date|wb_denial_reason_flag|wb_error_api_assign_code|wb_refer_correct_api_nbr|\
wb_dummy_api_number|wb_date_dummy_replaced|wb_newest_drl_pmt_nbr|wb_cancel_expire_code|wb_except_13_a|\
wb_fresh_water_flag|wb_plug_flag|wb_previous_api_nbr|wb_completion_data_ind|wb_hist_date_source_flag|\
wb_ex14b2_count|wb_designation_hb_1975_flag|wb_designation_effective_date|wb_designation_revised_date|\
wb_designation_letter_date|wb_certification_effect_date|wb_water_land_code|wb_total_bonded_depth|\
wb_override_est_plug_cost|wb_shut_in_date|wb_override_bonded_depth|wb_subj_to_14b2_flag|wb_pend_removal_14b2_flag|\
wb_orphan_well_hold_flag|wb_w3x_well_flag",file=fout01,end='\n')

fout02 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb02_junk.csv','w')
print("wb_api|wb_og_code|wb_oil_dist|wb_oil_lse_nbr|wb_oil_well_nbr|wb_gas_rrc|wb_gas_dist|wb_gas_well_no|\
wb_multi_well_rec_nbr|wb_api_suffix|wb_active_inactive_code|wb_dwn_hole_commingle_code|wb_created_from_pi_flag|\
wb_rule_37_nbr|wb_p_15|wb_p_12|wb_plug_date_ptr",file=fout02,end='\n')

fout03 = open (r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb03_junk.csv','w')
print("wb_api|wb_file_key|wb_file_date|wb_except_rule_11|wb_cement_affidavit|wb_g_5|wb_w_12|wb_dir_survey|\
wb_w2_g1_date|wb_compl_date|wb_drl_compl_date|wb_plugb_depth1|wb_plugb_depth2|wb_water_injection_nbr|\
wb_salt_wtr|wb_remarks|wb_elevation|wb_elevation_code|wb_log_file_rba|wb_docket_nbr|wb_psa_well_flag|\
wb_allocation_well_flag",file=fout03,end='\n')

fout04 = open (r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb04_junk.csv','w')
print("wb_api|wb_rmk_line_cnt|wb_rmk_type_code|wb_remarks",file=fout04,end='\n')

fout05 = open (r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb05_junk.csv','w')
print("wb_api|wb_segment_counter|wb_tubing_inches|wb_tubing_numerator|wb_tubing_denominator|wb_depth_set|\
wb_packer_set",file=fout05,end='\n')

fout06 = open (r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb06_junk.csv','w')
print("wb_api|wb_casing_count|wb_cas_inch|wb_cas_fracnum|wb_case_fracdenom|wb_cas_wt_table|wb_casing_depth_set|\
wb_mlti_stg_tool_dpth|wb_amount_of_cement|wb_cement_measurement|wb_hole_inch|wb_hole_frac_num|wb_hole_frac_denom|\
wb_top_of_cement_casing|wb_amount_casing_left",file=fout06,end='\n')

fout07 = open (r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb07_junk.csv','w')
print("wb_api|wb_perf_count|wb_from_perf|wb_to_perf|wb_open_hole_code",file=fout07,end='\n')

fout08 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb08_junk.csv','w')
print("wb_api|wb_line_count|wb_lin_inch|wb_lin_frac_num|wb_lin_frac_denom|wb_sacks_of_cement|wb_top_of_liner|\
wb_bottom_of_liner",file=fout08,end='\n')

fout09 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb09_junk.csv','w')
print("wb_api|wb_formation_cntr|wb_formation_name|wb_formation_depth",file=fout09,end='\n')

fout10 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb10_junk.csv','w')
print("wb_api|wb_squeeze_cntr|wb_squeeze_upper_depth|wb_squeeze_lower_depth|\
wb_squeeze_kind_amount",file=fout10,end='\n')

fout11 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb11_junk.csv','w')
print("wb_api|wb_fresh_water_cntr|wb_twdb_date|wb_surace_casing_deter_code|\
wb_uqwp_from|wb_uqwp_to",file=fout11,end='\n')

fout12 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb12_junk.csv','w')
print("wb_api|wb_lease_name|wb_sec_blk_survey_loc|wb_well_loc_miles|wb_well_loc_direction|wb_well_loc_nearest_town|\
wb_dist_from_survey_lines|wb_dist_direct_near_well",file=fout12,end='\n')

fout13 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb13_junk.csv','w')
print("wb_api|wb_loc_county|wb_abstract|wb_survey|wb_block_number|wb_section|wb_alt_section|wb_alt_abstract|\
wb_feet_from_sur_sect_1|wb_direc_from_ur_ect_1|wb_feet_from_sur_sect_2|wb_direc_from_sur_sect_2|\
wb_wgs84_latitude|wb_wgs84_longitude|wb_plane_zone|wb_plane_coordinate_east|wb_plane_coordinate_north|\
wb_verification_flag",file=fout13,end='\n')

fout14 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb14_junk.csv','w')
print("wb_api|wb_date_w3_filed|wb_date_well_bore_plugged|wb_plug_total_depth|wb_plug_cement_comp|wb_plug_mud_filled|\
wb_plug_mud_applied|wb_plug_mud_weight|wb_plug_dril_perm_date|wb_plug_dril_perm_no|wb_plug_dril_comp_date|\
wb_plug_log_attached|wb_plug_log_released_to|wb_plug_type_log|wb_plug_fresh_water_depth|wb_plug_from_uwqp1|\
wb_plug_to_uwqp1|wb_plug_from_uwqp2|wb_plug_to_uwqp2|wb_plug_from_uwqp3|wb_plug_to_uwqp3|wb_plug_from_uwqp4|\
wb_plug_to_uwqp4|wb_plug_material_left|wb_plug_code|wb_plug_oil_dist|wb_plug_oil_lse_nbr|wb_plug_oil_well_nbr|\
wb_plug_gas_rrc_id|wb_plug_gas_dist|wb_plug_gas_well_no|wb_plug_type_well|\
wb_plug_multi_compl_flag|wb_plug_cem_aff|wb_plug_13a|wb_plug_log_released_date|wb_plug_log_file_rba|\
wb_state_funded_plug_number",file=fout14,end='\n')

fout15 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb15_junk.csv','w')
print("wb_api|wb_plug_rmk_line_cnt|wb_plug_rmk_type_code|wb_plug_remarks",file=fout15,end='\n')

fout16 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb16_junk.csv','w')
print("wb_api|wb_plug_number|wb_nbr_of_cement_sacks|wb_meas_top_of_plug|wb_bottom_tube_pipe_depth|wb_plug_calc_top|\
wb_plug_type_cement",file=fout16,end='\n')

fout17 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb17_junk.csv','w')
print("wb_api|wb_plg_cas_counter|wb_plug_cas_inch|wb_plug_cas_frac_num|wb_plug_cas_frac_denom|wb_plug_wgt_wgt_whole|\
wb_plug_wgt_tenths|wb_plug_amt_put|wb_plug_amt_left|wb_plug_hole_inch|wb_plug_hole_frac_num|\
wb_plug_hole_frac_denom",file=fout17,end='\n')

fout18 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb18_junk.csv','w')
print("wb_api|wb_plug_perf_counter|wb_plug_from_perf|wb_plug_to_perf|\
wb_plug_open_hole_indicator",file=fout18,end='\n')

fout19 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb19_junk.csv','w')
print("wb_api|wb_plug_field_no|wb_plug_field_name|wb_plug_oper_no|wb_plug_oper_name|\
wb_plug_lease_name",file=fout19,end='\n')

fout20 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb20_junk.csv','w')
print("wb_api|wb_permit_number",file=fout20,end='\n')

fout21 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb21_junk.csv','w')
print("wb_api|wb_code|wb_oil_district|wb_oil_lse_number|wb_oil_well_number|wb_gas_rrcid",file=fout21,end='\n')

fout22 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb22_junk.csv','w')
print("wb_api|wb_14b2_oil_code|wb_14b2_oil_district|wb_14b2_oil_lease_number|wb_14b2_oil_well_number|\
wb_14b2_gas_rrc_id|wb_14b2_application_number|wb_14b2_gas_district|wb_14b2_ext_status_flag|\
wb_14b2_ext_cancelled_reason|wb_14b2_ext_approved_date|wb_14b2_ext_exp_date|wb_14b2_ext_denied_date|\
wb_14b2_ext_hist_date|wb_14b2_mech_integ_viol_flag|wb_14b2_plug_order_sf_hold_flag|wb_14b2_pollution_viol_flag|\
wb_14b2_field_ops_hold|wb_14b2_h15_problem_flag|wb_14b2_h15_not_filed_flag|wb_14b2_oper_delq_flag|\
wb_14b2_district_hold_sfp|wb_14b2_dist_sf_clean_up_flag|wb_14b2_dist_state_plug_flag|\
wb_14b2_good_faith_viol_flag|wb_14b2_well_other_viol_flag|wb_14b2_w3c_surf_eqp_viol_flag|\
wb_14b2_w3x_viol_flag|wb_14b2_hb2259_wex_pub_ent|wb_14b2_hb2259_w3x_10pct|wb_14b2_hb2259_w3x_bonding|\
wb_14b2_hb2259_w3x_h13_eor|wb_14b2_hb2259_w3x_aop|wb_14b2_hb2259_w3x_mit|wb_14b2_hb2259_w3x_escrow|\
wb_14b2_w3x_filing_key|wb_14b2_w3x_aop_received_date|wb_14b2_w3x_aop_fee_rcvd_date|\
wb_14b2_w3x_h15_fee_rcvd_date|wb_14b2_w3x_escrow_funds|wb_14b2_60_day_letter_sent_flag|\
wb_14b2_w1x_36_needs_bond_flag|wb_14b2_w1x_36_type_coverage|wb_14b2_w1x_36_amt_filed|\
wb_14b2_w1x_36_surety|wb_14b2_w1x_36_exp_date|wb_14b2_12x_36_bond_number",file=fout22,end='\n')

fout23 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb23_junk.csv','w')
print("wb_api|wb_h15_date_key|wb_h15_status|wb_h15_operator|wb_h15_next_test_due_date|wb_h15_district|\
wb_h15_field|wb_h15_hist_wellbore_flag|wb_h15_hist_well_ccyymmdd|wb_h15_w1x_well|wb_15_oil_gas_code|\
wb_h15_lease_nbr|wb_h15_well_nbr|wb_h15_gasid_nbr|wb_h15_test_date|wb_h15_base_usable_water|\
wb_h15_type_test_flag|wb_h15_top_of_fluid|wb_h15_fluid_test_flag|wb_h15_mech_integ_test_flag|\
wb_h15_mech_test_reason_flag|wb_h15_alternate_test_period|wb_h15_other_mit_test_type|wb_h15_status_date|\
wb_h15_no_date_well_flag|wb_h15_record_from_edi_flag|wb_h15_keyed_date|wb_h15_changed_date|\
wb_h15_previous_status|wb_h15_uic_test_flag|wb_h15_2yrs_approved_flag|wb_h15_mail_hold_flag|\
wb_h15_10yr_inactive_flag|wb_h15_w3x_well_flag",file=fout23,end='\n')

fout24 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb24_junk.csv','w')
print("wb_api|wb_h15_remark_key|wb_h15_remark_text",file=fout24,end='\n')

fout25 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb25_junk.csv','w')
print("wb_api|wb_sb126_designation_flag|wb_sb126_desig_effective_date|wb_sb126_desig_revised_date|\
wb_sb126_desig_letter_date|wb_sb126_cert_effect_date|wb_sb126_cert_revoked_date|wb_sb126_cert_denial_date|\
wb_sb126_denial_reason_flag",file=fout25,end='\n')

fout26 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb26_junk.csv','w')
print("wb_api|wb_dastat_stat_num|wb_dastat_uniq_num|wb_dastat_deleted_flag",file=fout26,end='\n')

fout27 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb27_junk.csv','w')
print("wb_api|wb_w3c_1yr_flag|wb_w3c_1yr_filed_date|wb_w3c_1yr_filing_oper|wb_w3c_5yr_flag|\
wb_w3c_5yr_filed_date|wb_w3c_5yr_filing_oper|wb_w3c_10yr_flag|wb_w3c_10yr_filed_date|\
wb_w3c_10yr_filing_oper|wb_w3c_14b2_removal_date|wb_w3c_extension_flag|wb_w3c_extension_date|\
wb_w3c_5yr_flag_previous|wb_w3c_10yr_flag_previous",file=fout27,end='\n')

fout28 = open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\wb28_junk.csv','w')
print("wb_api|wb_14b2_rmk_line_cnt|wb_14b2_rmk_date|wb_14b2_rmk_userid|wb_14b2_remarks",file=fout28,end='\n')


with open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\pp_dbf900.txt') as pp:
    for line in pp:
        well_id = line[2:10]
        rec_id = line[10:12]
        
        # wellbore record type 01 - Root
        if (rec_id == '01') :
            #wellid
            print(well_id+"|",file=fout01,end='')
            
            #wb_nxt_avail_suffix
            print(line[20:22]+"|",file=fout01,end='')
            
            #wb_nxt_avail_hole_chge_nbr
            print(line[22:24]+"|",file=fout01,end='')
            
            #wb_wb_field_district
            print(line[24:26]+"|",file=fout01,end='')
            
            #wb_res_cnty_code
            print(line[26:29]+"|",file=fout01,end='')
            
            #wb_orig_cmpl_cc
            print(line[29:30]+"|",file=fout01,end='')
             
            #wb_orig_cmpl_date
            print(ValDate(line[30:38])+"|",file=fout01,end='')
            
            #wb_total_depth
            print(line[38:43]+"|",file=fout01,end='')
            
            #wb_valid_fluid_level
            print(line[43:48]+"|",file=fout01,end='')
            
            #wb_certification_revoked_date
            print(ValDate(line[48:56])+"|",file=fout01,end='')
            
            #wb_certification_denial_date
            print(ValDate(line[56:64])+"|",file=fout01,end='')
            
            #wb_denial_reason_flag
            print(line[64:65]+"|",file=fout01,end='')
            
            #wb_error_api_assign_code
            print(line[65:66]+"|",file=fout01,end='')
            
            #wb_refer_correct_api_nbr
            print(line[66:74]+"|",file=fout01,end='')
            
            #wb_dummy_api_number
            print(line[74:82]+"|",file=fout01,end='')
            
            #wb_date_dummy_replaced
            print(line[82:90]+"|",file=fout01,end='')
            
            #wb_newest_drl_pmt_nbr
            print(line[90:96]+"|",file=fout01,end='')
            
            #wb_cancel_expire_code
            print(line[96:97]+"|",file=fout01,end='')
            
            #wb_except_13_a
            print(line[98:99]+"|",file=fout01,end='')
            
            #wb_fresh_water_flag
            print(line[99:100]+"|",file=fout01,end='')
            
            #wb_plug_flag
            print(line[100:101]+"|",file=fout01,end='') 
            
            #wb_previous_api_nbr
            print(line[101:109]+"|",file=fout01,end='')
            
            #wb_completion_data_ind
            print(line[109:110]+"|",file=fout01,end='') 
            
            #wb_hist_date_source_flg
            print(line[110:111]+"|",file=fout01,end='')
            
            #wb_ex14b2_count
            print(line[112:114]+"|",file=fout01,end='') 
            
            #wb_designation_hb_1975_flag
            print(line[114:115]+"|",file=fout01,end='') 
            
            #wb_designation_effective_date
            print(ValDate(line[115:121]+"00")+"|",file=fout01,end='')
            
            #wb_designation_revised_date
            print(ValDate(line[121:127]+"00")+"|",file=fout01,end='')
            
            #wb_designation_letter_date
            print(ValDate(line[127:135])+"|",file=fout01,end='')
            
            #wb_certication_effect_date
            print(ValDate(line[135:141]+"00")+"|",file=fout01,end='')
            
            #wb_water_land_code
            print(line[141:142]+"|",file=fout01,end='') 
            
            #wb_total_bonded_depth
            print(line[142:148]+"|",file=fout01,end='') 
            
            #wb_override_est_plug_cost
            print(line[148:155]+"|",file=fout01,end='') 
            
            #wb_shut_in_date
            print(ValDate(line[155:161]+"00")+"|",file=fout01,end='')
            
            #wb_override_bonded_depth
            print(line[161:167]+"|",file=fout01,end='') 
            
            #wb_sub_to_14b2_flag
            print(line[167:168]+"|",file=fout01,end='') 
            
            #wb_pend_removal_14b2_flag
            print(line[168:169]+"|",file=fout01,end='') 
            
            #wb_orphan_well_hold_flag
            print(line[169:170]+"|",file=fout01,end='')
            
            #wb_w3x_well_flag
            print(line[170:171],file=fout01,end='') 
            
            # end of line
            print ("\n",file=fout01,end='')
            
        # wellbore record type 02 - Completion
        if (rec_id == '02') :
            #wellid
            print(well_id+"|",file=fout02,end='')
            
            #wb_og_code
            og_code = line[12:13]
            print(og_code+"|",file=fout02,end='')
            
            if (og_code == 'O'):
                #wb_oil_dist
                print(line[13:15].strip()+"|",file=fout02,end='')
                #wb_oil_lse_nbr
                print(line[15:20].strip()+"|",file=fout02,end='')
                #wb_oil_well_nbr
                print(line[20:26].strip()+"|",file=fout02,end='')
                #wb_gas_rrc_id
                print("|",file=fout02,end='')
            elif (og_code == 'G'):
                #wb_oil_dist
                print("|",file=fout02,end='')
                #wb_oil_lse_nbr
                print("|",file=fout02,end='')
                #wb_oil_well_nbr
                print("|",file=fout02,end='')
                #wb_gas_rrc_id
                print(line[13:19].strip()+"|",file=fout02,end='')
            else:
                print("||||",file=fout02,end='')
                
            #wb_gas_dist
            print(line[26:28].strip()+"|",file=fout02,end='')
            
            #wb_gas_well_no                
            print(line[28:34].strip()+"|",file=fout02,end='')
            
            #wb_multi_well_rec_nbr             
            print(line[34:35].strip()+"|",file=fout02,end='')
            
            #wb_api_suffix             
            print(line[35:37].strip()+"|",file=fout02,end='')
            
            #wb_active_inactive_code          
            print(line[55:56].strip()+"|",file=fout02,end='')
            
            #wb_dwn_hole_commingle_code            
            print(line[96:97].strip()+"|",file=fout02,end='')
            
            #wb_created_from_pi_flag        
            print(line[131:132].strip()+"|",file=fout02,end='')
            
            #wb_rule_37_nbr        
            print(line[132:139].strip()+"|",file=fout02,end='')
            
            #wb_p_15       
            print(line[165:166].strip()+"|",file=fout02,end='')
            
            #wb_p_12    
            print(line[166:167].strip()+"|",file=fout02,end='')
            
            #wb_plug_date_ptr
            print(ValDate(line[167:175]),file=fout02,end='')
            
            
            # end of line
            print ("\n",file=fout02,end='')
            
        # wellbore record type 03 - Well Bore Technical Data Forms File Date
        if (rec_id == '03') :
            #wellid
            print(well_id+"|",file=fout03,end='')
            
            #wb_file_key
            print(line[12:20]+"|",file=fout03,end='')
            
            #wb_file_date
            print(ValDate(line[20:28])+"|",file=fout03,end='')
            
            #wb_except_rule
            print(line[36:37].strip()+"|",file=fout03,end='')
            
            #wb_cement_affidavit
            print(line[37:38].strip()+"|",file=fout03,end='')
            
            #wb_g_5
            print(line[20:28].strip()+"|",file=fout03,end='')
            
            #wb_w_12
            print(line[39:40].strip()+"|",file=fout03,end='')
            
            #wb_dir_survey
            print(line[40:41].strip()+"|",file=fout03,end='')
            
            #wb_w2_g1_date
            print(ValDate(line[41:49])+"|",file=fout03,end='')
            
            #wb_compl_date
            print(ValDate(line[49:57])+"|",file=fout03,end='')
            
            #wb_drl_compl_date
            print(ValDate(line[57:65])+"|",file=fout03,end='')
            
            #wb_plugb_depth1
            print(line[65:70].strip()+"|",file=fout03,end='')
            
            #wb_plugb_depth2
            print(line[70:75].strip()+"|",file=fout03,end='')
            
            #wb_water_injection_nbr
            print(line[75:81].strip()+"|",file=fout03,end='')
            
            #wb_salt_wtr_nbr
            print(line[81:86].strip()+"|",file=fout03,end='')
            
            #wb_remarks_ind
            print(line[94:95].strip()+"|",file=fout03,end='')
            
            #wb_elevation
            print(line[95:99].strip()+"|",file=fout03,end='')
            
            #wb_elevation_code
            print(line[99:101].strip()+"|",file=fout03,end='')
            
            #wb_log_file_rba
            print(line[101:109].strip()+"|",file=fout03,end='')
            
            #wb_docket_nbr
            print(line[109:119].strip()+"|",file=fout03,end='')
            
            #wb_psa_well_flag
            print(line[119:120].strip()+"|",file=fout03,end='')
            
            #wb_allocation_well_flag
            print(line[120:121].strip(),file=fout03,end='')
            
            # end of line
            print ("\n",file=fout03,end='')
            
        # wellbore record type 03 - Well Bore Remarks Segment
        if (rec_id == '04') :
            #wellid
            print(well_id+"|",file=fout04,end='')
      
            #wb_rmk_line_cnt
            print(line[12:15].strip()+"|",file=fout04,end='')
      
            #wb_rmk_type_code
            print(line[15:16].strip()+"|",file=fout04,end='')
      
            #wb_remarks
            remarks = str.replace(line[16:86],'"','')
            print(remarks.strip()+"|",file=fout04,end='')
      
            # end of line
            print ("\n",file=fout04,end='')
            
        # wellbore record type 05 - Well Bore Tubing Segment
        if (rec_id == '05') :
            #wellid
            print(well_id+"|",file=fout05,end='')
            
            #wb_segment_counter
            print(line[12:15].strip()+"|",file=fout05,end='')
            
            #wb_tubing_inches
            print(line[15:17].strip()+"|",file=fout05,end='')
            
            #wb_tubing_numerator
            print(line[17:19].strip()+"|",file=fout05,end='')
            
            #wb_tubing_denominator
            print(line[19:21].strip()+"|",file=fout05,end='')
            
            #wb_depth_set
            print(line[21:26].strip()+"|",file=fout05,end='')
            
            #wb_packer_set
            print(line[26:31].strip(),file=fout05,end='')
            
            # end of line
            print ("\n",file=fout05,end='')
            
        # wellbore record type 06 - Well Bore Casing Segment
        if rec_id == '06' :
            #wellid
            print(well_id+'|',file=fout06,end='')

            #wb_casing_count
            print(line[12:15].strip()+'|',file=fout06,end='')

            #wb_cas_inch
            print(line[15:17].strip()+'|',file=fout06,end='')

            #wb_cas_fracNum
            print(line[17:19].strip()+'|',file=fout06,end='')

            #wb_case_fracDenom
            print(line[19:21].strip()+'|',file=fout06,end='')

            #wb_cas_wt_table
            print(line[21:29].strip()+'|',file=fout06,end='')

            #wb_casing_depth_set
            print(line[29:34].strip()+'|',file=fout06,end='')

            #wb_mlti_stg_tool_dpth
            print(line[34:39].strip()+'|',file=fout06,end='')

            #wb_amount_of_cement
            print(line[39:44].strip()+'|',file=fout06,end='')

            #wb_cement_measurement
            print(line[44:45].strip()+'|',file=fout06,end='')

            #wb_hole_inch
            print(line[45:47].strip()+'|',file=fout06,end='')

            #wb_hole_frac_num
            print(line[47:49].strip()+'|',file=fout06,end='')

            #wb_hole_frac_denom
            print(line[49:51].strip()+'|',file=fout06,end='')

            #wb_top_of_cement_casing
            print(line[52:59].strip()+'|',file=fout06,end='')

            #wb_amount_casing_left
            print(line[59:64].strip(),file=fout06,end='')

            #end of line
            print("\n",file=fout06,end='')  
            
        # wellbore record type '07' - Well bore perfs segment
        if rec_id == '07' :
            #wellid
            print(well_id+'|',file=fout07,end='')

            #wb_perf_count
            print(line[12:15].strip()+'|',file=fout07,end='')

            #wb_from_perf
            print(line[15:20].strip()+'|',file=fout07,end='')

            #wb_to_perf
            print(line[20:25].strip()+'|',file=fout07,end='')

            #wb_open_hole_code
            print(line[25:27].strip(),file=fout07,end='')

            #end of line
            print("\n",file=fout07,end='')
        
        #wellbore record type '08' - Well bore liners segment
        if rec_id == '08' :
            #wellid
            print(well_id+'|',file=fout08,end='')

            #wb_line_count
            print(line[12:15].strip()+'|',file=fout08,end='')

            #wb_lin_inch
            print(line[15:17].strip()+'|',file=fout08,end='')

            #wb_lin_frac_num
            print(line[17:19].strip()+'|',file=fout08,end='')

            #wb_lin_frac_denom
            print(line[19:21].strip()+'|',file=fout08,end='')

            #wb_sacks_of_cement
            print(line[21:26].strip()+'|',file=fout08,end='')

            #wb_top_of_liner
            print(line[26:31].strip()+'|',file=fout08,end='')

            #wb_bottom_of_liner
            print(line[31:36].strip(),file=fout08,end='')

            #end of line
            print("\n",file=fout08,end='')
       
        #wellbore record type '09' - Well formation segment
        if rec_id == '09' :
            #wellid
            print(well_id+'|',file=fout09,end='')

            #wb_formation_cntr
            print(line[12:15].strip()+'|',file=fout09,end='')

            #wb_formation_name
            print(line[15:47].strip()+'|',file=fout09,end='')

            #wb_formation_depth
            print(line[47:52].strip(),file=fout09,end='')

            #end of line
            print("\n",file=fout09,end='')
            
        #wellbore record type '10' - Well squeeze segment
        if rec_id == '10' :
            #wellid
            print(well_id+'|',file=fout10,end='')

            #wb_squeeze_cntr
            print(line[12:15].strip()+'|',file=fout10,end='')

            #wb_squeeze_upper_depth
            print(line[15:20].strip()+'|',file=fout10,end='')

            #wb_squeeze_lower_depth
            print(line[20:25].strip()+'|',file=fout10,end='')

            #wb_squeeze_kind_amount
            print(line[25:75].strip(),file=fout10,end='')

            #end of line
            print("\n",file=fout10,end='')
        
        #wellbore record type '11' - Fresh Water segment
        if rec_id == '11' :
            #wellid
            print(well_id+'|',file=fout11,end='')

            #wb_fresh_water_cntr
            print(line[12:15].strip()+'|',file=fout11,end='')

            #wb_twdb_date
            print(ValDate(line[15:23])+'|',file=fout11,end='')

            #wb_surace_casing_deter_code
            print(line[23:24].strip()+'|',file=fout11,end='')

            #wb_uqwp_from
            print(line[24:28].strip()+'|',file=fout11,end='')

            #wb_uqwp_to
            print(line[28:32].strip(),file=fout11,end='')
            
            #end of line
            print("\n",file=fout11,end='')
            
        #wellbore record type '12' - Wellbore old Location segment
        if rec_id == '12' :
            #wellid
            print(well_id+'|',file=fout12,end='')

            #wb_lease_name
            print(line[12:44].strip()+'|',file=fout12,end='')

            #wb_sec_blk_survey_loc
            print(line[44:96].strip()+'|',file=fout12,end='')

            #wb_well_loc_miles
            print(line[96:100].strip()+'|',file=fout12,end='')

            #wb_well_loc_direction
            print(line[100:106].strip()+'|',file=fout12,end='')

            #wb_well_loc_nearest_town
            print(line[106:119].strip()+'|',file=fout12,end='')

            #wb_dist_from_survey_lines
            print(line[147:175].strip()+'|',file=fout12,end='')

            #wb_dist_direct_near_well
            print(line[175:203].strip(),file=fout12,end='')

            #end of line
            print("\n",file=fout12,end='')
            
        #wellbore record type '13' - Wellbore new location segment
        if rec_id == '13' :
            #wellid
            print(well_id+'|',file=fout13,end='')

            #wb_loc_county
            print(line[12:15].strip()+'|',file=fout13,end='')

            #wb_abstract
            print(line[15:21].strip()+'|',file=fout13,end='')

            #wb_survey
            print(line[21:76].strip()+'|',file=fout13,end='')

            #wb_block_number
            print(line[76:86].strip()+'|',file=fout13,end='')

            #wb_section
            print(line[86:94].strip()+'|',file=fout13,end='')

            #wb_alt_section
            print(line[94:98].strip()+'|',file=fout13,end='')

            #wb_alt_abstract
            print(line[98:104].strip()+'|',file=fout13,end='')

            #wb_feet_from_sur_sect_1
            print(line[104:110].strip()+'|',file=fout13,end='')

            #wb_direc_from_ur_ect_1
            print(line[110:123].strip()+'|',file=fout13,end='')

            #wb_feet_from_sur_sect_2
            print(line[123:129].strip()+'|',file=fout13,end='')

            #wb_direc_from_sur_sect_2
            print(line[129:142].strip()+'|',file=fout13,end='')

            #wb_wgs84_latitude
            lat = int(line[142:151].strip())
            if (isinstance(lat,int)) :
                flat = lat / 1000000.0
                print(str(flat)+'|',file=fout13,end='')
            else :
                print ('|',file=fout13,end='')

            #wb_wgs84_longitude
            lng = int(line[152:161].strip())
            if (isinstance(lng,int)) :
                flng = lng / -1000000.0
                print(str(flng)+'|',file=fout13,end='')
            else :
                print('0.0|',file=fout13,end='')

            #wb_plane_zone
            print(line[167:169].strip()+'|',file=fout13,end='')

            #wb_plane_coordinate_east
            xx = line[169:177].strip()
            if xx.isdigit() :
                fxx = int(xx) / 10.0
            else :
                fxx = 0.0
            print(str(fxx)+'|',file=fout13,end='')
            
            #wb_plane_coordinate_north
            yy = line[179:188].strip()
            if (yy.isdigit()) :
                fyy = int(yy) / 1.0
            else :
                fyy = 0.0
            print(str(fyy)+'|',file=fout13,end='')
                
            #wb_verification_flag
            print(line[187:188].strip(),file=fout13,end='')

            #end of line
            print("\n",file=fout13,end='')
            
        #Wellbore record type '14' Plug Record Segment
        if rec_id == '14' :
            #wellid
            print(well_id+'|',file=fout14,end='')

            #wb_date_w3_filed
            print(ValDate(line[12:20])+'|',file=fout14,end='')

            #wb_date_well_bore_plugged
            print(ValDate(line[20:28])+'|',file=fout14,end='')

            #wb_plug_total_depth
            print(line[28:33].strip()+'|',file=fout14,end='')

            #wb_plug_cement_comp
            print(line[33:65].strip()+'|',file=fout14,end='')

            #wb_plug_mud_filled
            print(line[65:66].strip()+'|',file=fout14,end='')

            #wb_plug_mud_applied
            print(line[66:78].strip()+'|',file=fout14,end='')

            #wb_plug_mud_weight
            print(line[78:81].strip()+'|',file=fout14,end='')

            #wb_plug_dril_perm_date
            print(ValDate(line[85:93])+'|',file=fout14,end='')

            #wb_plug_dril_perm_no
            print(line[93:99].strip()+'|',file=fout14,end='')

            #wb_plug_dril_comp_date
            print(ValDate(line[99:107])+'|',file=fout14,end='')

            #wb_plug_log_attached
            print(line[107:108].strip()+'|',file=fout14,end='')

            #wb_plug_log_released_to
            print(line[108:140].strip()+'|',file=fout14,end='')

            #wb_plug_type_log
            print(line[140:141].strip()+'|',file=fout14,end='')

            #wb_plug_fresh_water_depth
            print(line[141:146].strip()+'|',file=fout14,end='')

            #wb_plug_from_uwqp1
            print(line[146:151].strip()+'|',file=fout14,end='')

            #wb_plug_to_uwqp1
            print(line[151:156].strip()+'|',file=fout14,end='')

            #wb_plug_from_uwqp2
            print(line[156:161].strip()+'|',file=fout14,end='')

            #wb_plug_to_uwqp2
            print(line[161:166].strip()+'|',file=fout14,end='')

            #wb_plug_from_uwqp3
            print(line[166:171].strip()+'|',file=fout14,end='')

            #wb_plug_to_uwqp3
            print(line[171:176].strip()+'|',file=fout14,end='')

            #wb_plug_from_uwqp4
            print(line[176:181].strip()+'|',file=fout14,end='')

            #wb_plug_to_uwqp4
            print(line[181:186].strip()+'|',file=fout14,end='')

            #wb_plug_material_left
            print(line[186:187].strip()+'|',file=fout14,end='')

            #wb_plug_code
            code = line[187:188].strip()
            print(code+'|',file=fout14,end='')
            
            if (code == 'O') :
                #wb_plug_oil_dist
                print(line[188:190].strip()+'|',file=fout14,end='')

                #wb_plug_oil_lse_nbr
                print(line[190:195].strip()+'|',file=fout14,end='')

                #wb_plug_oil_well_nbr
                print(line[195:201].strip()+'||',file=fout14,end='')
                
            #otherwise it's assumed to be a gas well.
            else :
                print('|||',file=fout14,end='')
                #wb_plug_gas_rrc_id
                print(line[188:194].strip()+'|',file=fout14,end='')

            #wb_plug_gas_dist
            print(line[201:203].strip()+'|',file=fout14,end='')

            #wb_plug_gas_well_no
            print(line[203:209].strip()+'|',file=fout14,end='')

            #wb_plug_type_well
            print(line[209:210].strip()+'|',file=fout14,end='')

            #wb_plug_multi_compl_flag
            print(line[210:211].strip()+'|',file=fout14,end='')

            #wb_plug_cem_aff
            print(line[211:212].strip()+'|',file=fout14,end='')

            #wb_plug_13a
            print(line[212:213].strip()+'|',file=fout14,end='')

            #wb_plug_log_released_date
            print(ValDate(line[213:221])+'|',file=fout14,end='')

            #wb_plug_log_file_rba
            print(line[221:229].strip()+'|',file=fout14,end='')

            #wb_state_funded_plug_number
            print(line[229:236].strip(),file=fout14,end='')

            #end of line
            print("\n",file=fout14,end='')
            
        #Wellbore record type '15' Wellbore plugging remarks segment
        if rec_id == '15' :
            #wellid
            print(well_id+'|',file=fout15,end='')

            #wb_plug_rmk_line_cnt
            print(line[12:15].strip()+'|',file=fout15,end='')

            #wb_plug_rmk_type_code
            print(line[15:16].strip()+'|',file=fout15,end='')

            #wb_plug_remarks
            print(line[16:86].strip(),file=fout15,end='')

            #end of line
            print("\n",file=fout15,end='')
            
        #Wellbore record type '16' Wellbore plugging record segment
        if rec_id == '16' :
            #wellid
            print(well_id+'|',file=fout16,end='')

            #wb_plug_number
            print(line[12:15].strip()+'|',file=fout16,end='')

            #wb_nbr_of_cement_sacks
            print(line[15:20].strip()+'|',file=fout16,end='')

            #wb_meas_top_of_plug
            print(line[20:25].strip()+'|',file=fout16,end='')

            #wb_bottom_tube_pipe_depth
            print(line[25:30].strip()+'|',file=fout16,end='')

            #wb_plug_calc_top
            print(line[30:35].strip()+'|',file=fout16,end='')

            #wb_plug_type_cement
            print(line[35:41].strip(),file=fout16,end='')

            #end of line
            print("\n",file=fout16,end='')
        
        #Wellbore record type '17' Wellbore Plugging Casing-Tubing Record
        if rec_id == '17' :
            #wellid
            print(well_id+'|',file=fout17,end='')

            #wb_plg_cas_counter
            print(line[12:18].strip()+'|',file=fout17,end='')

            #wb_plug_cas_inch
            print(line[18:20].strip()+'|',file=fout17,end='')

            #wb_plug_cas_frac_num
            print(line[20:22].strip()+'|',file=fout17,end='')

            #wb_plug_cas_frac_denom
            print(line[22:24].strip()+'|',file=fout17,end='')

            #wb_plug_wgt_wgt_whole
            print(line[24:27].strip()+'|',file=fout17,end='')

            #wb_plug_wgt_tenths
            print(line[27:28].strip()+'|',file=fout17,end='')

            #wb_plug_amt_put
            print(line[28:33].strip()+'|',file=fout17,end='')

            #wb_plug_amt_left
            print(line[33:38].strip()+'|',file=fout17,end='')

            #wb_plug_hole_inch
            print(line[38:40].strip()+'|',file=fout17,end='')

            #wb_plug_hole_frac_num
            print(line[40:42].strip()+'|',file=fout17,end='')

            #wb_plug_hole_frac_denom
            print(line[42:44].strip(),file=fout17,end='')

            #end of line
            print("\n",file=fout17,end='')
        
        #Wellbore record type '18' - Wellbore plugging perfs segment
        if rec_id == '18' :
            #wellid
            print(well_id+'|',file=fout18,end='')

            #wb_plug_perf_counter
            print(line[12:15].strip()+'|',file=fout18,end='')

            #wb_plug_from_perf
            print(line[15:20].strip()+'|',file=fout18,end='')

            #wb_plug_to_perf
            print(line[20:25].strip()+'|',file=fout18,end='')

            #wb_plug_open_hole_indicator
            print(line[25:26].strip(),file=fout18,end='')

            #end of line
            print("\n",file=fout18,end='')
        
        #wellbore record type '19' - Wellbore plugging data casing-tubing record
        if rec_id == '19' :
            #wellid
            print(well_id+'|',file=fout19,end='')

            #wb_plug_field_no
            print(line[12:20].strip()+'|',file=fout19,end='')

            #wb_plug_field_name
            print(line[20:52].strip()+'|',file=fout19,end='')

            #wb_plug_oper_no
            print(line[52:58].strip()+'|',file=fout19,end='')

            #wb_plug_per_name
            print(line[58:90].strip()+'|',file=fout19,end='')

            #wb_plug_leae_name
            print(line[90:122].strip(),file=fout19,end='')

            #end of line
            print("\n",file=fout19,end='')
            
        #wellbore record type '20' - Wellbore drilling permit number
        if rec_id == '20' :
            #wellid
            print(well_id+'|',file=fout20,end='')

            #wb_permit_number
            print(line[12:18].strip(),file=fout20,end='')

            #end of line
            print("\n",file=fout20,end='')
        
        #wellbore record type '21' - Wellbore Well-ID Segment
        if rec_id == '21' :
            
            #wellid
            print(well_id+'|',file=fout21,end='')
            
            #wb_og_code
            og_code = line[12:13]
            print(og_code+"|",file=fout21,end='')
            
            if (og_code == 'O'):
                #wb_oil_dist
                print(line[13:15].strip()+"|",file=fout21,end='')
                #wb_oil_lse_nbr
                print(line[15:20].strip()+"|",file=fout21,end='')
                #wb_oil_well_nbr
                print(line[20:26].strip()+"|",file=fout21,end='')
                #wb_gas_rrc_id
                print("|",file=fout21,end='')
            elif (og_code == 'G'):
                #wb_oil_dist
                print("|",file=fout21,end='')
                #wb_oil_lse_nbr
                print("|",file=fout21,end='')
                #wb_oil_well_nbr
                print("|",file=fout21,end='')
                #wb_gas_rrc_id
                print(line[13:19].strip()+"|",file=fout21,end='')
            else:
                print("||||",file=fout21,end='')
                
            #end of line
            print("\n",file=fout21,end='')
            
        #wellbore record type '22 - 14(B)(2) Extension / Plug system'
        if rec_id == '22' :
            #wellid
            print(well_id+'|',file=fout22,end='')
            
            #wb_og_code
            og_code = line[12:13]
            print(og_code+"|",file=fout22,end='')
            
            if (og_code == 'O'):
                #wb_oil_dist
                print(line[13:15].strip()+"|",file=fout22,end='')
                #wb_oil_lse_nbr
                print(line[15:20].strip()+"|",file=fout22,end='')
                #wb_oil_well_nbr
                print(line[20:26].strip()+"|",file=fout22,end='')
                #wb_gas_rrc_id
                print("|",file=fout22,end='')
            elif (og_code == 'G'):
                #wb_oil_dist
                print("|",file=fout22,end='')
                #wb_oil_lse_nbr
                print("|",file=fout22,end='')
                #wb_oil_well_nbr
                print("|",file=fout22,end='')
                #wb_gas_rrc_id
                print(line[13:19].strip()+"|",file=fout22,end='')
            else:
                print("||||",file=fout22,end='')

            #wb_14b2_application_number
            print(line[26:32].strip()+'|',file=fout22,end='')

            #wb_14b2_gas_district
            print(line[32:34].strip()+'|',file=fout22,end='')

            #wb_14b2_ext_status_flag
            print(line[34:35].strip()+'|',file=fout22,end='')

            #wb_14b2_ext_cancelled_reason
            print(line[35:36].strip()+'|',file=fout22,end='')

            #wb_14b2_ext_approved_date
            print(ValDate(line[36:44])+'|',file=fout22,end='')

            #wb_14b2_ext_exp_date
            print(ValDate(line[44:52])+'|',file=fout22,end='')

            #wb_14b2_ext_denied_date
            print(ValDate(line[52:60])+'|',file=fout22,end='')

            #wb_14b2_ext_hist_date
            print(ValDate(line[60:68])+'|',file=fout22,end='')

            #wb_14b2_mech_integ_viol_flag
            print(line[68:69].strip()+'|',file=fout22,end='')

            #wb_14b2_plug_order_sf_hold_flag
            print(line[69:70].strip()+'|',file=fout22,end='')

            #wb_14b2_pollution_viol_flag
            print(line[70:71].strip()+'|',file=fout22,end='')

            #wb_14b2_field_ops_hold
            print(line[71:72].strip()+'|',file=fout22,end='')

            #wb_14b2_h15_problem_flag
            print(line[72:73].strip()+'|',file=fout22,end='')
            
            #wb_14b2_h15_not_filed_flag
            print(line[73:74].strip()+'|',file=fout22,end='')
            
            #wb_14b2_oper_delq_flag
            print(line[74:75].strip()+'|',file=fout22,end='')
            
            #wb_district_hold_sfp_flag
            print(line[75:76].strip()+'|',file=fout22,end='')

            #wb_14b2_dist_sf_clean_up_flag
            print(line[76:77].strip()+'|',file=fout22,end='')

            #wb_14b2_dist_state_plug_flag
            print(line[77:78].strip()+'|',file=fout22,end='')

            #wb_14b2_good_faith_viol_flag
            print(line[78:79].strip()+'|',file=fout22,end='')

            #wb_14b2_well_other_viol_flag
            print(line[79:80].strip()+'|',file=fout22,end='')

            #wb_14b2_w3c_surf_eqp_viol_flag
            print(line[80:81].strip()+'|',file=fout22,end='')

            #wb_14b2_w3x_viol_flag
            print(line[81:82].strip()+'|',file=fout22,end='')

            #wb_14b2_hb2259_wex_pub_ent
            print(line[89:90].strip()+'|',file=fout22,end='')

            #wb_14b2_hb2259_w3x_10pct
            print(line[90:91].strip()+'|',file=fout22,end='')

            #wb_14b2_hb2259_w3x_bonding
            print(line[91:92].strip()+'|',file=fout22,end='')

            #wb_14b2_hb2259_w3x_h13_eor
            print(line[92:93].strip()+'|',file=fout22,end='')

            #wb_14b2_hb2259_w3x_aop
            print(line[93:94].strip()+'|',file=fout22,end='')

            #wb_14b2_hb2259_w3x_mit
            print(line[94:95].strip()+'|',file=fout22,end='')

            #wb_14b2_hb2259_w3x_escrow
            print(line[95:96].strip()+'|',file=fout22,end='')

            #wb_14b2_w3x_filing_key
            print(line[96:104].strip()+'|',file=fout22,end='')

            #wb_14b2_w3x_aop_received_date
            print(ValDate(line[104:112])+'|',file=fout22,end='')

            #wb_14b2_w3x_aop_fee_rcvd_date
            print(ValDate(line[112:120])+'|',file=fout22,end='')

            #wb_14b2_w3x_h15_fee_rcvd_date
            print(ValDate(line[120:128])+'|',file=fout22,end='')

            #wb_14b2_w3x_escrow_funds
            print(line[128:135].strip()+'|',file=fout22,end='')

            #wb_14b2_60_day_letter_sent_flag
            print(line[135:136].strip()+'|',file=fout22,end='')

            #wb_14b2_w1x_36_needs_bond_flag
            print(line[136:137].strip()+'|',file=fout22,end='')

            #wb_14b2_w1x_36_type_coverage
            print(line[137:138].strip()+'|',file=fout22,end='')

            #wb_14b2_w1x_36_amt_filed
            print(line[138:147].strip()+'|',file=fout22,end='')

            #wb_14b2_w1x_36_surety
            print(line[147:152].strip()+'|',file=fout22,end='')

            #wb_14b2_w1x_36_exp_date
            print(ValDate(line[152:160])+'|',file=fout22,end='')

            #wb_14b2_12x_36_bond_number
            print(line[160:180].strip(),file=fout22,end='')

            #end of line
            print("\n",file=fout22,end='')
            
        #wb record type '23' Wellbore H-15 segment
        if rec_id == '23' :
            #wellid
            print(well_id+'|',file=fout23,end='')

           #wb_h15_date_key
            print(ValDate(line[12:8])+'|',file=fout23,end='')

            #wb_h15_status
            print(line[20:21].strip()+'|',file=fout23,end='')

            #wb_h15_operator
            print(line[21:27].strip()+'|',file=fout23,end='')

            #wb_h15_next_test_due_date
            print(ValDate(line[27:33])+'|',file=fout23,end='')

            #wb_h15_district
            print(line[33:35].strip()+'|',file=fout23,end='')

            #wb_h15_field
            print(line[35:43].strip()+'|',file=fout23,end='')

            #wb_h15_hist_wellbore_flag
            print(line[43:44].strip()+'|',file=fout23,end='')

            #wb_h15_hist_well_ccyymmdd
            print(ValDate(line[44:52])+'|',file=fout23,end='')

            #wb_h15_w1x_well
            print(line[52:53].strip()+'|',file=fout23,end='')

            #wb_15_oil_gas_code
            print(line[53:54].strip()+'|',file=fout23,end='')

            #wb_h15_lease_nbr
            print(line[54:59].strip()+'|',file=fout23,end='')

            #wb_h15_well_nbr
            print(line[59:65].strip()+'|',file=fout23,end='')

            #wb_h15_gasid_nbr
            print(line[65:71].strip()+'|',file=fout23,end='')

            #wb_h15_test_date
            print(ValDate(line[71:79])+'|',file=fout23,end='')

            #wb_h15_base_usable_water
            print(line[79:85].strip()+'|',file=fout23,end='')

            #wb_h15_type_test_flag
            print(line[85:86].strip()+'|',file=fout23,end='')

            #wb_h15_top_of_fluid
            print(line[86:92].strip()+'|',file=fout23,end='')

            #wb_h15_fluid_test_flag
            print(line[92:93].strip()+'|',file=fout23,end='')

            #wb_h15_mech_integ_test_flag
            print(line[93:94].strip()+'|',file=fout23,end='')

            #wb_h15_mech_test_reason_flag
            print(line[94:95].strip()+'|',file=fout23,end='')

            #wb_h15_alternate_test_period
            print(line[95:97].strip()+'|',file=fout23,end='')

            #wb_h15_other_mit_test_type
            print(line[97:117].strip()+'|',file=fout23,end='')

            #wb_h15_status_date
            print(ValDate(line[117:125])+'|',file=fout23,end='')

            #wb_h15_no_date_well_flag
            print(line[125:126].strip()+'|',file=fout23,end='')

            #wb_h15_record_from_edi_flag
            print(line[126:127].strip()+'|',file=fout23,end='')

            #wb_h15_keyed_date
            print(ValDate(line[127:135])+'|',file=fout23,end='')

            #wb_h15_changed_date
            print(ValDate(line[135:143])+'|',file=fout23,end='')

            #wb_h15_previous_status
            print(line[143:144].strip()+'|',file=fout23,end='')

            #wb_h15_uic_test_flag
            print(line[144:145].strip()+'|',file=fout23,end='')

            #wb_h15_2yrs_approved_flag
            print(line[145:146].strip()+'|',file=fout23,end='')

            #wb_h15_mail_hold_flag
            print(line[146:147].strip()+'|',file=fout23,end='')

            #wb_h15_10yr_inactive_flag
            print(line[147:148].strip()+'|',file=fout23,end='')

            #wb_h15_w3x_well_flag
            print(line[148:149].strip(),file=fout23,end='')

            #end of line
            print("\n",file=fout23,end='')
        
        #wb record type = '24' wbh15 remarks
        if rec_id == '24' :
            #wellid
            print(well_id+'|',file=fout24,end='')

            #wb_h15_remark_key
            print(line[12:15].strip()+'|',file=fout24,end='')

            #wb_h15_remark_text
            print(line[15:85].strip(),file=fout24,end='')
            #end of line
            print("\n",file=fout24,end='')
            
        #wb record type = '25' wb senate bill 126 segment
        if rec_id == '25' :
            #wellid
            print(well_id+'|',file=fout25,end='')

            #wb_sb126_designation_flag
            print(line[12:13].strip()+'|',file=fout25,end='')

            #wb_sb126_desig_effective_date
            print(ValDate(line[13:19])+'|',file=fout25,end='')

            #wb_sb126_desig_revised_date
            print(ValDate(line[19:25])+'|',file=fout25,end='')

            #wb_sb126_desig_letter_date
            print(ValDate(line[25:33])+'|',file=fout25,end='')

            #wb_sb126_cert_effect_date
            print(ValDate(line[33:39])+'|',file=fout25,end='')

            #wb_sb126_cert_revoked_date
            print(ValDate(line[39:47])+'|',file=fout25,end='')

            #wb_sb126_cert_denial_date
            print(ValDate(line[47:55])+'|',file=fout25,end='')

            #wb_sb126_denial_reason_flag
            print(line[55:56].strip(),file=fout25,end='')

            #end of line
            print("\n",file=fout25,end='')
        
        #wb record type = '26' wb Drilling Permit Status Number
        if rec_id == '26' :
            #wellid
            print(well_id+'|',file=fout26,end='')

            #wb_dastat_stat_num
            print(line[12:19].strip()+'|',file=fout26,end='')

            #wb_dastat_uniq_num
            print(line[19:21].strip()+'|',file=fout26,end='')

            #wb_dastat_deleted_flag
            print(line[21:22].strip(),file=fout26,end='')

            #end of line
            print("\n",file=fout26,end='')
            
        #wb record type = '27' wb form w3c segment
        if rec_id == '27' :
            #wellid
            print(well_id+'|',file=fout27,end='')

            #wb_w3c_1yr_flag
            print(line[12:13].strip()+'|',file=fout27,end='')

            #wb_w3c_1yr_filed_date
            print(ValDate(line[13:21])+'|',file=fout27,end='')

            #wb_w3c_1yr_filing_oper
            print(line[21:27].strip()+'|',file=fout27,end='')

            #wb_w3c_5yr_flag
            print(line[27:28].strip()+'|',file=fout27,end='')

            #wb_w3c_5yr_filed_date
            print(ValDate(line[28:36])+'|',file=fout27,end='')

            #wb_w3c_5yr_filing_oper
            print(line[36:42].strip()+'|',file=fout27,end='')

            #wb_w3c_10yr_flag
            print(line[42:43].strip()+'|',file=fout27,end='')

            #wb_w3c_10yr_filed_date
            print(ValDate(line[43:51])+'|',file=fout27,end='')

            #wb_w3c_10yr_filing_oper
            print(line[51:57].strip()+'|',file=fout27,end='')

            #wb_w3c_14b2_removal_date
            print(ValDate(line[57:65])+'|',file=fout27,end='')

            #wb_w3c_extension_flag
            print(line[65:66].strip()+'|',file=fout27,end='')

            #wb_w3c_extension_date
            print(ValDate(line[66:74])+'|',file=fout27,end='')

            #wb_w3c_5yr_flag_previous
            print(line[74:75].strip()+'|',file=fout27,end='')

            #wb_w3c_10yr_flag_previous
            print(line[75:76].strip(),file=fout27,end='')

            #end of line
            print("\n",file=fout27,end='')
            
        #wb record type = '28' wellbore remarks segment
        if rec_id == '28' :
            #wellid
            print(well_id+'|',file=fout28,end='')

            #wb_14b2_rmk_line_cnt
            print(line[12:15].strip()+'|',file=fout28,end='')

            #wb_14b2_rmk_date
            print(ValDate(line[15:23])+'|',file=fout28,end='')

            #wb_14b2_rmk_userid
            print(line[23:31].strip()+'|',file=fout28,end='')

            #wb_14b2_remarks
            print(line[31:97].strip(),file=fout28,end='')

            #end of line
            print("\n",file=fout28,end='')
        
        
        
        
        
fout01.close()
fout02.close()
fout03.close()
fout04.close()
fout05.close()
fout06.close()
fout07.close()
fout08.close()
fout09.close()
fout10.close()
fout11.close()
fout12.close()
fout13.close()
fout14.close()
fout15.close()
fout16.close()
fout17.close()
fout18.close()
fout19.close()
fout20.close()
fout21.close()
fout22.close()
fout23.close()
fout24.close()
fout25.close()
fout26.close()
fout27.close()
fout28.close()

#Clean up output files

base = r"D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore"
printable = set(string.printable)
for ii in range (1,29) :
    fname_junk = base+"\wb"+"{:02d}".format(ii)+"_junk.csv"
    fname = base+"\wb"+"{:02d}".format(ii)+".csv"
      
    #Get rid of junk characters in the wb files
    
    print("Processing removal of junk from file: "+fname+" (phase 1)\n")
    
    with open(fname_junk,'r') as infile, \
        open(fname, 'w') as outfile:
        for line in infile:
            data = ''.join(filter(lambda x: x in printable, line))
            outfile.write(data)
    os.remove(fname_junk)

    
    
                       
