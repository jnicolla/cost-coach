import os
import csv
from Plinko_Model import insuranceFunc
# If you wan to change the input files to obtain different output files, run the main_script.py
# Make sure you change the file name (pathname) in the process_data to the one you want to be runing 
def getPath(rel_path):
    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]
    return os.path.join(script_dir, rel_path)

def readfile(filename):
    retlist = []
    fname = open(filename)
    tempread = csv.reader(fname, delimiter = ",")
    for line in tempread:
        retlist.append(line)
    return retlist

def planDict(filelist):
    planDict = {}
    for ele in filelist:
        iden = ele[5]
        tempoopm = ele[8].strip("$")
        newoopm = int(round(float(tempoopm.replace(',',''))))
        tempdeduc = ele[6].strip("$")
        newdeduc = int(round(float(tempdeduc.replace(',',''))))
        tempdrugDeduc = ele[7].strip("$")
        newdrugDeduc = int(round(float(tempdrugDeduc.replace(',',''))))
        metalLevel = ele[3]
        if iden not in planDict:
            planDict[iden] = (ele, [(newoopm, newdeduc, newdrugDeduc, 0, '1',metalLevel,'')]) #tuple: (plan, [(oopm, deduc, drug deduc, first claim, first visit)])
    return planDict

def writeGenericFile(infodict):
    for k,v in infodict.items():
        rel_path = "csvfiles/Step-by-Step Changes in OOPM and Deductibles for " + k + ".csv"
        filename = getPath(rel_path)
        header  = ["Plan", 'Metal Level', 'OOPM', 'Deductible', 'Drug Deductible', 'Number of Claims', 'Visits', 'Category']
        with open(filename, 'w') as newFile:
            tempWrite = csv.writer(newFile)
            tempWrite.writerow(header)
            for ele in v:
                tempWrite.writerows(ele)
    return

def writeFinalFile(infodict):
    for k,v in infodict.items():
        rel_path = "csvfiles/Final Plans for Scenario " + k + ".csv"
        filename = getPath(rel_path)
        header  = ["Plan", 'Metal Level', 'OOPM', 'Deductible', 'Drug Deductible', 'Number of Claims', 'Visits', 'Category']
        with open(filename, 'w') as newFile:
            tempWrite = csv.writer(newFile)
            tempWrite.writerow(header)
            for ele in v:
                tempWrite.writerow(ele[-1])
    return

def scenarioDict(filelist):
    dict = {}
    for ele in filelist:
        scenario = ele[0]
        if scenario not in dict:
            dict[scenario] = [(ele[3], ele[4], ele[6], ele[8], ele[1])] # value = (category, cost, inpatient stay, inpatient days, visit)
        elif scenario in dict:
            dict[scenario].append((ele[3], ele[4], ele[6], ele[8], ele[1]))
    return dict

    

if __name__ == '__main__':
    insuranceFile_rel_path = "csvfiles/Copy QHP.csv"
    insuranceFile = getPath(insuranceFile_rel_path)

    pathwaysFile_rel_path = "csvfiles/Prostate IV Oral 150 - Full Year Regimens with Categories.csv"
    pathwaysFile = getPath(pathwaysFile_rel_path)

    tempInsuranceFileList = readfile(insuranceFile)
    insuranceFileList = tempInsuranceFileList[1:]
    tempPathwaysFileList = readfile(pathwaysFile)
    pathwaysFileList = tempPathwaysFileList[1:]
    planDict = planDict(insuranceFileList)
    scenDict = scenarioDict(pathwaysFileList)
       #print (planDict)
    #print planDict.items()
       #print (scenDict)
    #print scenDict.items()
    #for plan,numTup in planDict.items():
        #print numTup[1]
    #for scenario,values in scenDict.items():
        #for value in values:
            #print value[1]
    #for ele in planDict.items():
        #print ele
    dict = insuranceFunc(planDict, scenDict)
     #print (dict)
    writeGenericFile(dict)
    writeFinalFile(dict)
