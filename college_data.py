import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

hd = pd.read_csv('data/hd/hd2018.csv', encoding='latin_1')
hd = hd[['UNITID', 'INSTNM', 'ADDR', 'CITY', 'STABBR', 'ZIP', 'HLOFFER', 'HBCU', 'LOCALE', 'INSTCAT', 'COUNTYNM', 'LONGITUDE', 'LATITUDE']]

#hd.set_index('UNITID', inplace=True)
rename = {
    'INSTNM': 'name',
    'ADDR': 'address',
    'CITY': 'city',
    'STABBR': 'state',
    'ZIP': 'zipcode',
    'HLOFFER': 'highest_level_offered',
    'LOCALE': 'locale',
    'INSTCAT': 'category',
    'COUNTYNM': 'county',
    'LONGITUDE': 'longitude',
    'LATITUDE': 'latitude'
}
replace = {
    'category_desc': {
        1: 'Degree-granting, graduate with no undergraduate degrees',
        2: 'Degree-granting, primarily baccalaureate or above',
        3: 'Degree-granting, not primarily baccalaureate or above',
        4: 'Degree-granting, Associates and certificates',
        5: 'Nondegree-granting, above the baccalaureate',
        6: 'Nondegree-granting, sub-baccalaureate'
    },
    
    'locale': {
        11: 'City: Large',
        12: 'City: Midsize',
        13: 'City: Small',
        21: 'Suburb: Large',
        22: ' Suburb: Midsize',
        23: 'Suburb: Small',
        31: 'Town: Fringe',
        32: 'Town: Distant',
        33: 'Town: Remote',
        41: 'Rural: Fringe',
        42: 'Rural: Distant',
        43: 'Rural: Remote'
    }
}
hd.rename(rename, axis=1, inplace=True)
hd['category_desc'] = hd['category'].copy()
hd.replace(replace, inplace=True)
#hd[hd['category'] == 3]

ic = pd.read_csv('data/ic/ic2018.csv', encoding='latin_1')
ic = ic[['UNITID', 'ROOMAMT', 'BOARDAMT', 'APPLFEEU']]
#ic.set_index('UNITID', inplace=True)
rename = {
    'ROOMAMT': 'room_cost',
    'BOARDAMT': 'board_cost',
    'APPLFEEU': 'application_fee'
}
replace = {
    '.': 0
}
ic.rename(rename, axis=1, inplace=True)
ic.replace(replace, inplace=True)

icay = pd.read_csv('data/ic_ay/ic2018_ay.csv', encoding='latin_1')
icay = icay[['UNITID','TUITION2','FEE2','TUITION3','FEE3',]]
#icay.set_index('UNITID', inplace=True)
rename = {
    'TUITION2': 'in_tuition',
    'TUITION3': 'out_tuition',
    'FEE2': 'in_fees',
    'FEE3': 'out_fees',
}
replace = {
    '.': 0
}
icay.rename(rename, axis=1, inplace=True)
icay.replace(replace, inplace=True)

effy = pd.read_csv('data\eefy\effy2018.csv', encoding='latin_1')
effy = effy[['UNITID', 'EFFYLEV','EFYTOTLT', 'EFYTOTLM', 'EFYTOTLW']]
effy = effy[effy['EFFYLEV'] == 2]
#effy.set_index('UNITID', inplace=True)
rename = {
    'EFYTOTLT': 'total_students',
    'EFYTOTLM': 'total_men',
    'EFYTOTLW': 'total_women'
}
effy.rename(rename, axis=1, inplace=True)

efd = pd.read_csv("data\EF2018D\ef2018d.csv", encoding = 'latin_1')
efd = efd[['UNITID','RET_PCF', 'STUFACR']]
#efd.set_index('UNITID', inplace=True)
rename = {
    'STUFACR': 'student_faculty_ratio',
    'RET_PCF': 'retention',
}
efd.rename(rename, axis=1, inplace=True)

sfa = pd.read_csv("data\SFA1718\sfa1718.csv", encoding = 'latin_1')
sfa = sfa[['UNITID', 'SCUGRAD', 'UFLOANN', 'UFLOANT', 'UAGRNTT', 'UPGRNTN', 'UPGRNTT', 'SGRNT_N', 'SGRNT_T', 'IGRNT_N', 'IGRNT_T', 'LOAN_N', 
           'LOAN_T', 'GISTT2']]
#sfa.set_index('UNITID', inplace = True)
rename = {
    'SCUGRAD': 'num_students_financial_aid',
    'UFLOANN': "num_students_receiving_aid_federal",
    'UFLOANT': 'total_federal_aid_awarded',
    'UAGRNTT': "total_aid_awarded",
    'UPGRNTN': 'num_pell_grants',
    'UPGRNTT': 'total_pell_grants',
    'SGRNT_N': 'num_students_receiving_aid_state_local',
    'SGRNT_T': 'total_state_local_aid_awarded',
    'IGRNT_N': 'num_students_receiving_institutional_aid',
    'IGRNT_T': 'total_institutional_aid_awarded',
    'LOAN_N': 'num_students_loans',
    'LOAN_T': 'total_loans_awarded',
    'GISTT2': 'total_scholarships_awarded'
    
}
sfa.rename(rename, axis=1, inplace=True)

#sfa['retention'] = sfa['retention']/100

#f = pd.read_csv('data/f1718/f1718.csv', encoding = 'latin_1')

dfs = [hd, ic, icay, effy, efd, sfa]

for df in dfs:
    df.set_index('UNITID', inplace=True)

college = hd.join(ic, on='UNITID', how='left')
college = college.join(icay, on='UNITID', how='left')
college = college.join(effy, on='UNITID', how='left')
college = college.join(efd, on='UNITID', how='left')
college = college.join(sfa, on='UNITID', how='left')
#college = college.join(f, on='UNITID', how='right')

#college.to_csv('data/college.csv')