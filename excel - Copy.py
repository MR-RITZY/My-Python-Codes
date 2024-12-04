import openpyxl, pprint
workbook = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = workbook.active
states = list(list(sheet.columns)[1])
del states[0]
counties = list(list(sheet.columns)[2])
del counties[0]
popu = list(list(sheet.columns)[3])
del popu[0]
census_data = {}
county = {}
for i, j in enumerate(counties):
    if j.value != counties[i-1].value:
        county[j.value] = [popu[i].value, 1]
    else:
        county[j.value] = [county[j.value][0] + popu[i].value, county[j.value][1]+1]
for i, j in enumerate(states):
    if j.value != states[i-1]:
        census_data[j.value] = {counties[i].value: {'pop' : county[counties[i].value][0], 'tract':county[counties[i].value][1]}}
    else:
        pass
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(census_data))
resultFile.close()







