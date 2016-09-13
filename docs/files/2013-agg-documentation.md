Medicare Physician and Other Supplier National Provider Identifier (NPI) Aggregate Report, Calendar Year 2013|
Documentation|
Variable Name|Description
NPI|National Provider Identifier (NPI) for the performing provider on the claim.
NPPES Provider Last Name / Organization Name|When the provider is registered in NPPES as an individual (entity type code=’I’), this is the provider’s last name. When the provider is registered as an organization (entity type code = ‘O’), this is the organization name.
NPPES Provider First Name|When the provider is registered in NPPES as an individual (entity type code=’I’), this is the provider’s first name. When the provider is registered as an organization (entity type code = ‘O’), this will be blank.
NPPES Provider Middle Initial|When the provider is registered in NPPES as an individual (entity type code=’I’), this is the provider’s middle initial. When the provider is registered as an organization (entity type code = ‘O’), this will be blank.
NPPES Credentials|When the provider is registered in NPPES as an individual (entity type code=’I’), these are the provider’s credentials. When the provider is registered as an organization (entity type code = ‘O’), this will be blank. 
NPPES Provider Gender|When the provider is registered in NPPES as an individual (entity type code=’I’), this is the provider’s gender. When the provider is registered as an organization (entity type code = ‘O’), this will be blank.
NPPES Entity Code|Type of entity reported in NPPES. An entity code of ‘I’ identifies providers registered as individuals and an entity type code of ‘O’ identifies providers registered as organizations.
NPPES Provider Street Address 1|The first line of the provider’s street address, as reported in NPPES.
NPPES Provider Street Address 2|The second line of the provider’s street address, as reported in NPPES.
NPPES Provider City|The city where the provider is located, as reported in NPPES.
NPPES Provider Zip Code|The provider’s zip code, as reported in NPPES.
NPPES Provider State|"The state where the provider is located, as reported in NPPES. The fifty U.S. states and the District of Columbia are reported by the state postal abbreviation.  The following values are used for other areas:
'XX' = 'Unknown'
'AA' = 'Armed Forces Central/South America'
'AE' = 'Armed Forces Europe'
'AP' = 'Armed Forces Pacific'
'AS' = 'American Samoa'
'GU' = 'Guam'
'MP' = 'North Mariana Islands'
'PR' = 'Puerto Rico'
'VI' = 'Virgin Islands'
'ZZ' = 'Foreign Country'
"
NPPES Provider Country |"The country where the provider is located, as reported in NPPES. The country code will be ‘US’ for any state or U.S. possession. For foreign countries (i.e., state values of ‘ZZ’), the provider country values include the following:
‘AE’ = ‘United Arab Emirates’; 'AG'='Antigua'; ‘AR’= ‘Argentina’; ‘AU’= ‘Australia’; 'BO'='Bolivia'; ‘BR’= ‘Brazil’;  ‘CA’= ‘Canada’;  ‘CH’= Switzerland’; ‘CN’= China’; ‘CO’= Colombia’;  ‘DE’= ‘Germany’; ‘ES’= ‘Spain’; ‘FR’= France’;  ‘GB’= Great Britain’; ‘HU’= Hungary’; ‘IL’= Israel’; ‘IN’= India’; ‘IS’= Iceland;  ‘IT’= Italy’;  ‘JP’= Japan’; ‘KR’= ‘Korea’; 'KW'='Kuwait'; 'KY'='Cayman Islands'; 'LB'='Lebanon'; 'MX'='Mexico'; ‘NL’= ‘Netherlands’;  'NO'='Norway'; 'NZ'='New Zealand'; 'PA'='Panama'; ‘PK’= ‘Pakistan’;  'RW'='Rwanda'; ‘SA’= ‘Saudi Arabia’; ‘SY’= ‘Syria’;  ‘TR’= ‘Turkey’; ' TH'='Thailand'; ‘VE’= ‘Venezuela’ ."
Provider Type|Derived from the provider specialty code reported on the claim.  For providers that reported more than one specialty code on their claims, this is the specialty code associated with the largest number of services.
Medicare Participation Indicator|Identifies whether the provider participates in Medicare and/or accepts assignment of Medicare allowed amounts.  The value will be ‘Y’ for any provider that had at least one claim identifying the provider as participating in Medicare or accepting assignment of Medicare allowed amounts.
Number of HCPCS|Total number of unique HCPCS codes.
Number of Services|Total provider services.
Number of Unique Beneficiaries|Total Medicare beneficiaries receiving the provider services. The beneficiary counts reported in the demographic sub-groups (i.e., age, sex, race and entitlement) may not aggregate to the ‘Number of Unique Beneficiaries’ due to the suppression of beneficiaries fewer than 11 within the demographic sub-groups.  In addition, a small percentage of beneficiaries are reflected in the “Number of Unique Beneficiaries” but are not reflected in the beneficiary demographic information due to the lack of demographic information available at the time of reporting.
Total Submitted Charges|The total charges that the provider submitted for all services.
Total Medicare Allowed Amount|The Medicare allowed amount for all provider services. This figure is the sum of the amount Medicare pays, the deductible and coinsurance amounts that the beneficiary is responsible for paying, and any amounts that a third party is responsible for paying.
Total Medicare Payment Amount|Amount that Medicare paid after deductible and coinsurance amounts have been deducted for all the provider's line item services.
Drug Suppress Indicator1|Identifies whether the utilization, cost and payment information associated with HCPCS codes for drug services as listed on the Medicare Part B Drug Average Sales Price (ASP) list have been suppressed.  An '*' identifies that the suppressed information is based on fewer than 11 beneficiaries and a '#' identifies that the information has been counter suppressed  to prevent the re-calculation of  information suppressed due to fewer than 11 beneficiaries.  For example, if the information associated with Drug  services has been suppressed because fewer than 11 beneficiaries received these services from a provider, then the information associated with Medical services must also be suppressed so that the information associated with Drug services can not be recalculated by subtracting the Medical values from the provider's overall values.
Number of HCPCS Associated With Drug Services1|Total number of HCPCS codes for drug services, as defined from the Medicare Part B Drug ASP File. 
Number of Drug Services1|Total drug services, as defined from the Medicare Part B Drug ASP File.
Number of Unique Beneficiaries With Drug Services1|Total Medicare beneficiaries receiving drug services, as defined from the Medicare Part B Drug ASP File.
Total Drug Submitted Charges1|The total charges that the provider submitted for drug services, as defined from the Medicare Part B Drug ASP File.
Total Drug Medicare Allowed Amount1|The Medicare allowed amount for drug services, as defined from the Medicare Part B Drug ASP File. This figure is the sum of the amount Medicare pays, the deductible and coinsurance amounts that the beneficiary is responsible for paying, and any amounts that a third party is responsible for paying.
Total Drug Medicare Payment Amount1|Amount that Medicare paid after deductible and coinsurance amounts have been deducted for all the provider's line item drug services, as defined from the Medicare Part B Drug ASP File.
Medical Suppress Indicator|Identifies whether the utilization, cost and payment information associated with HCPCS codes for Medical (non-ASP) services have been suppressed.  An '*' identifies that the suppressed information is based on fewer than 11 beneficiaries and a '#' identifies that the information has been counter suppressed  to prevent the re-calculation of  information suppressed due to fewer than 11 beneficiaries.  For example, if the information associated with Medical (non-ASP) services has been suppressed because fewer than 11 beneficiaries received these services from a provider, then the information associated with Drug services must also be suppressed so that the information associated with Medical services can not be recalculated by subtracting the Drug values from the provider's overall values.
Number of HCPCS Associated With Medical Services|Total number of HCPCS codes associated with medical (non-ASP) services. 
Number of Medical Services|Total medical (non-ASP) services.
Number of Unique Beneficiaries With Medical Services|Total Medicare beneficiaries receiving medical (non-ASP) services.
Total Medical Submitted Charges|The total charges that the provider submitted for medical services (non-ASP).
Total Medical Medicare Allowed Amount|The Medicare allowed amount for medical (non-ASP) services. This figure is the sum of the amount Medicare pays, the deductible and coinsurance amounts that the beneficiary is responsible for paying, and any amounts that a third party is responsible for paying.
Total Medical Medicare Payment Amount|Amount that Medicare paid after deductible and coinsurance amounts have been deducted for all the provider's line item medical (non-ASP) services.
Average Age of Beneficiaries2|Average age of beneficiaries. Beneficiary age is calculated at the end of the calendar year or at the time of death.
Number of Beneficiaries Age Less 652|Number of beneficiaries under the age of 65. Beneficiary age is calculated at the end of the calendar year or at the time of death.
Number of Beneficiaries Age 65 to 742|Number of beneficiaries between the ages of 65 and 74. Beneficiary age is calculated at the end of the calendar year or at the time of death.
Number of Beneficiaries Age 75 to 842|Number of beneficiaries between the ages of 75 and 84. Beneficiary age is calculated at the end of the calendar year or at the time of death.
Number of Beneficiaries Age Greater 842|Number of beneficiaries over the age of 84. Beneficiary age is calculated at the end of the calendar year or at the time of death.
Number of Female Beneficiaries2|Number of female beneficiaries. 
Number of Male Beneficiaries2|Number of male beneficiaries. 
Number of Non-Hispanic White Beneficiaries2 3|Number of non-Hispanic white beneficiaries. 
Number of Black or African American Beneficiaries2 3|Number of non-Hispanic black or African American beneficiaries. 
Number of Asian Pacific Islander Beneficiaries2 3|Number of Asian Pacific Islander beneficiaries. 
Number of Hispanic Beneficiaries2 3|Number of Hispanic beneficiaries. 
Number of American Indian/Alaska Native Beneficiaries2 3|Number of American Indian or Alaska Native beneficiaries. 
Number of Beneficiaries With Race Not Elsewhere Classified2 3|Number of beneficiaries with race not elsewhere classified. 
Number of Beneficiaries With Medicare Only Entitlement2|Number of Medicare beneficiaries qualified to receive Medicare only benefits. Beneficiaries are classified as Medicare only entitlement if they received zero months of any Medicaid benefits (full or partial) in the given calendar year.
Number of Beneficiaries With Medicare & Medicaid Entitlement2|Number of Medicare beneficiaries qualified to receive Medicare and Medicaid benefits. Beneficiaries are classified as Medicare and Medicaid entitlement if in any month in the given calendar year they were receiving full or partial Medicaid benefits.
Percent (%) of Beneficiaries Identified With Alzheimer’s Disease or Dementia2|Percent of beneficiaries meeting the CCW chronic condition algorithm for Alzheimer’s, related disorders, or dementia.  
Percent (%) of Beneficiaries Identified With Asthma2|Percent of beneficiaries meeting the CCW chronic condition algorithm for Asthma. 
Percent (%) of Beneficiaries Identified With Atrial Fibrillation2|Percent of beneficiaries meeting the CCW chronic condition algorithm for atrial fibrillation. 
Percent (%) of Beneficiaries Identified With Cancer2|Percent of beneficiaries meeting the CCW chronic condition algorithms for cancer. Includes breast cancer, colorectal cancer, lung cancer and prostate cancer. 
Percent (%) of Beneficiaries Identified With Chronic Kidney Disease2|Percent of beneficiaries meeting the CCW chronic condition algorithm for chronic kidney disease. 
Percent (%) of Beneficiaries Identified With Chronic Obstructive Pulmonary Disease2|Percent of beneficiaries meeting the CCW chronic condition algorithm for chronic obstructive pulmonary disease. 
Percent (%) of Beneficiaries Identified With Depression2|Percent of beneficiaries meeting the CCW chronic condition algorithm for depression. 
Percent (%) of Beneficiaries Identified With Diabetes2|Percent of beneficiaries meeting the CCW chronic condition algorithm for diabetes. 
Percent (%) of Beneficiaries Identified With Heart Failure2|Percent of beneficiaries meeting the CCW chronic condition algorithm for heart failure. 
Percent (%) of Beneficiaries Identified With Hyperlipidemia2|Percent of beneficiaries meeting the CCW chronic condition algorithm for hyperlipidemia. 
Percent (%) of Beneficiaries Identified With Hypertension2|Percent of beneficiaries meeting the CCW chronic condition algorithm for hypertension. 
Percent (%) of Beneficiaries Identified With Ischemic Heart Disease2|Percent of beneficiaries meeting the CCW chronic condition algorithm for ischemic heart disease. 
Percent (%) of Beneficiaries Identified With Osteoporosis2|Percent of beneficiaries meeting the CCW chronic condition algorithm for osteoporosis. 
Percent (%) of Beneficiaries Identified With Rheumatoid Arthritis / Osteoarthritis2|Percent of beneficiaries meeting the CCW chronic condition algorithm for rheumatoid arthritis/osteoarthritis. 
Percent (%) of Beneficiaries Identified With Schizophrenia / Other Psychotic Disorders2|Percent of beneficiaries meeting the CCW chronic condition algorithm for  schizophrenia and other psychotic disorders. 
Percent (%) of Beneficiaries Identified With Stroke2|Percent of beneficiaries meeting the CCW chronic condition algorithm for  stroke. 
Average HCC Risk Score of Beneficiaries4|Average Hierarchical Condition Category (HCC) risk score of beneficiaries. 
|
1For additional information on the ASP drug pricing, visit:|
http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Part-B-Drugs/McrPartBDrugAvgSalesPrice/index.html.|
|
2To protect the privacy of Medicare beneficiaries, the number of beneficiaries fewer than 11 have been suppressed and the percent of |
beneficiaries between 75% and 100% have been top-coded at 75% . Source of data is available from the CMS Chronic Conditions |
Warehouse (CCW) which contains 100 percent of Medicare enrollment and eligibility data. For complete information regarding |
data in the CCW, visit http://ccwdata.org/index.php.|
|
3Race is based on the RTI_RACE_CD  from the CMS CCW enrollment database. The RTI_RACE_CD variable is based upon a validated |
algorithm that uses Census surname lists and geography to improve the accuracy of race/ethnicity classification, particularly for those |
who are Hispanic or Asian/Pacific Islanders.|
|
4CMS developed a risk-adjustment model that uses HCCs (hierarchical condition categories) to assign risk scores. Those scores estimate |
how beneficiaries’ FFS spending will compare to the overall average for the entire Medicare population. The average risk score |
is set at 1.08; beneficiaries with scores greater than that are expected to have above-average spending, and vice versa. |
Risk scores are based on a beneficiary’s age and sex; whether the beneficiary is eligible for Medicaid, first qualified for Medicare|
 on the basis of disability, or lives in an institution (usually a nursing home); and the beneficiary’s diagnoses from the previous year.|
 The HCC model was designed for risk adjustment on larger populations, such as the enrollees in an MA plan, and generates more |
accurate results when used to compare groups of beneficiaries rather than individuals. |
|
CMS uses HCCs to determine the diagnosis-related portion of the risk score. For example, the HCC system for 2010 included a total |
of 189 conditions, with related conditions grouped into 70 disease hierarchies. One hierarchy had three different diseases that affect |
the liver: end-stage liver disease, cirrhosis, and chronic hepatitis. Each condition had a weight that reflects its marginal contribution|
 to a beneficiary’s total expected Medicare costs. |
|
Under the HCC system, CMS calculates the diagnosis-related portion of a beneficiary’s risk score by adding up the weights for |
the most severe diagnosis that the beneficiary has in each disease hierarchy. Continuing the example above, a beneficiary |
with both cirrhosis (weight = 0.406) and chronic hepatitis (weight = 0.406) would receive credit only for the cirrhosis diagnosis. |
The researchers who developed the HCC system adopted this approach after finding that having multiple conditions within a hierarchy |
did not increase overall patient spending substantially. |
