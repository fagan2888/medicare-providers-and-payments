# Convert xls files to CSV


# In agg files, split beneficiary data from the agg data





# Reconcile the field differences in PUFs:

```
csvcut -n -t wrangle/corral/fetched/Medicare_Provider_Util_Payment_PUF_CY2013.txt
  1: NPI
  2: NPPES_PROVIDER_LAST_ORG_NAME
  3: NPPES_PROVIDER_FIRST_NAME
  4: NPPES_PROVIDER_MI
  5: NPPES_CREDENTIALS
  6: NPPES_PROVIDER_GENDER
  7: NPPES_ENTITY_CODE
  8: NPPES_PROVIDER_STREET1
  9: NPPES_PROVIDER_STREET2
 10: NPPES_PROVIDER_CITY
 11: NPPES_PROVIDER_ZIP
 12: NPPES_PROVIDER_STATE
 13: NPPES_PROVIDER_COUNTRY
 14: PROVIDER_TYPE
 15: MEDICARE_PARTICIPATION_INDICATOR
 16: PLACE_OF_SERVICE
 17: HCPCS_CODE
 18: HCPCS_DESCRIPTION
 19: HCPCS_DRUG_INDICATOR
 20: LINE_SRVC_CNT
 21: BENE_UNIQUE_CNT
 22: BENE_DAY_SRVC_CNT
 23: AVERAGE_MEDICARE_ALLOWED_AMT
 24: STDEV_MEDICARE_ALLOWED_AMT
 25: AVERAGE_SUBMITTED_CHRG_AMT
 26: STDEV_SUBMITTED_CHRG_AMT
 27: AVERAGE_MEDICARE_PAYMENT_AMT
 28: STDEV_MEDICARE_PAYMENT_AMT



 csvcut -n -t wrangle/corral/fetched/Medicare_Provider_Util_Payment_PUF_CY2014.txt
  1: npi
  2: nppes_provider_last_org_name
  3: nppes_provider_first_name
  4: nppes_provider_mi
  5: nppes_credentials
  6: nppes_provider_gender
  7: nppes_entity_code
  8: nppes_provider_street1
  9: nppes_provider_street2
 10: nppes_provider_city
 11: nppes_provider_zip
 12: nppes_provider_state
 13: nppes_provider_country
 14: provider_type
 15: medicare_participation_indicator
 16: place_of_service
 17: hcpcs_code
 18: hcpcs_description
 19: hcpcs_drug_indicator
 20: line_srvc_cnt
 21: bene_unique_cnt
 22: bene_day_srvc_cnt
 23: average_Medicare_allowed_amt
 24: average_submitted_chrg_amt
 25: average_Medicare_payment_amt
 26: average_Medicare_standard_amt
 ```



