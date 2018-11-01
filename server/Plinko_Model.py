def insuranceFunc(planDict, scenDict): #Function which returns a dictionary, mapping each treatment scenario to every insurance plan,
    #and the associated out-of-pocket maximums, deductibles, and drug deductibles after each claim in that scenario. Once the OOPM
    #hits 0 or below 0, or the treatment program ends, the function also returns the final number of claims that occurred under that
    #insurance plan.
    retdict = {}
    for planId,numTup in planDict.items(): #For-loop which loops through every single insurance plan (planDict) in the study.
        #numTup is a tuple which includes a list of the plan specifications, and successive list of the (oopm, deduc, drug deduc)
        planSpecs = numTup[0] #List of all the specifications of the insurance plan in the current loop.
        planIdInfo = planSpecs[5]
        #print "Plan ID Number = " + planIdInfo
        print(planSpecs)
        for scenario,values in scenDict.items(): #For-loop that loops through every single treatment scenario (scenDict) in the study.
            #This dictionary contains each scenario number, linked to a list of the type of visit, the total cost of the visit, and the number of inpatient days.
            print ("Scenario " + str(scenario))
            scen = str(scenario)
            if scen not in retdict:
                retdict[scen] = []
            for value in values: #Third for-loop which loops through every single insurance claim that occurs during treatment
                #for the current scenario in question.
                oopm = numTup[-1][-1][0]
                deduc = numTup[-1][-1][1]
                drugDeduc = numTup[-1][-1][2]
                category = value[0]
                TC = float(value[1])
                inpatientDays = int(value[3]) #Setting up variable names for relevant values in each loop
                metalLevel = planSpecs[3]
                claimlength = len(numTup[-1])
                print ("CLAIMLEN" + str(claimlength))
                visit = value[4]
                print (category)
                print ("visit is " + visit)
                #print inpatientDays
                #print TC
                #print oopm
                #print deduc
                #print drugDeduc
                if category == "PCP": #Each of these 'category' statements tells the program where to pull insurance-specific
                    #values from, based on the type of claim that is being made
                    copay = float(planSpecs[10]) #Value of the copay for PCP visit
                    coinsurance = float(planSpecs[11]) #Value of coinsurance for PCP visit
                    deducBool = planSpecs[12] #Whether deductible applies for this claim ("1") or not ("0")
                    copayBef = planSpecs[13] #Whether the copay applies before the deductible ("1") or not ("0")
                    coinsAft = planSpecs[14] #Whether the coinsurance applies after the deductible ("1") or not ("0")
                    
                elif category == "Specialist":
                    copay = float(planSpecs[15])
                    coinsurance = float(planSpecs[16])
                    deducBool = planSpecs[17]
                    copayBef = planSpecs[18]
                    coinsAft = planSpecs[19]
                    
                elif category == "ER":
                    copay = float(planSpecs[20])
                    coinsurance = float(planSpecs[21])
                    deducBool = planSpecs[22]
                    copayBef = planSpecs[23]
                    coinsAft = planSpecs[24]
    
                elif category == "Inpatient Physician":
                    copay = float(planSpecs[25])
                    coinsurance = float(planSpecs[26])
                    deducBool = planSpecs[27]
                    copayBef = planSpecs[28]
                    coinsAft = planSpecs[29]
    
                elif category == "Inpatient Facility":
                    copay = float(planSpecs[30])
                    coinsurance = float(planSpecs[31])
                    deducBool = planSpecs[32]
                    copayBef = planSpecs[33]
                    coinsAft = planSpecs[34]
                    copayPerStay = planSpecs[35]
                    copayPerDay = planSpecs[36]
        
                elif category == "Rx Generic":
                    copay = float(planSpecs[37])
                    coinsurance = float(planSpecs[38])
                    deducBool = planSpecs[39]
                    copayBef = planSpecs[40]
                    coinsAft = planSpecs[41]
    
                elif category == "Rx Preferred Brand":
                    copay = float(planSpecs[42])
                    coinsurance = float(planSpecs[43])
                    deducBool = planSpecs[44]
                    copayBef = planSpecs[45]
                    coinsAft = planSpecs[46]
        
                elif category == "Rx Non Preferred Brand":
                    copay = float(planSpecs[47])
                    coinsurance = float(planSpecs[48])
                    deducBool = planSpecs[49]
                    copayBef = planSpecs[50]
                    coinsAft = planSpecs[51]
        
                elif category == "Rx Specialty":
                    copay = float(planSpecs[52])
                    coinsurance = float(planSpecs[53])
                    deducBool = planSpecs[54]
                    copayBef = planSpecs[55]
                    coinsAft = planSpecs[56]
                
                elif category == "Advanced Imaging":
                    copay = float(planSpecs[57])
                    coinsurance = float(planSpecs[58])
                    deducBool = planSpecs[59]
                    copayBef = planSpecs[60]
                    coinsAft = planSpecs[61]
                    
                elif category == "Lab":
                    copay = float(planSpecs[62])
                    coinsurance = float(planSpecs[63])
                    deducBool = planSpecs[64]
                    copayBef = planSpecs[65]
                    coinsAft = planSpecs[66]
                    
                elif category == "Xray":
                    copay = float(planSpecs[67])
                    coinsurance = float(planSpecs[68])
                    deducBool = planSpecs[69]
                    copayBef = planSpecs[70]
                    coinsAft = planSpecs[71]
                #print copay
                #print coinsurance
                #print deducBool
                #print copayBef
                #print coinsAft
            
                if deducBool == "1" and ((planSpecs[7] == "0") or (planSpecs[7] != "0" and "Rx" not in category)) and ((planSpecs[36] == "0") or (planSpecs[36] != "0" and "Inpatient Facility" not in category)):
                    #Watch for the space after the "$0.00"..how to fix?
                    #Accounts for situation when the medical deductible applies, the drug deductible doesn't apply, and the number
                    #of inpatient days does not affect how the oopm, deductible or drug deductible change
                    if copay > 0 and coinsurance == 0:
                        if copayBef == "1": #What to do when copay > 0 and the copay applies before the deductible
                            TCRem = TC - copay
                            num = TCRem - deduc
                            if TCRem > 0:
                                if num <= 0: #Deductible not exhausted
                                    oopm -= copay + TCRem
                                    deduc -= TCRem
                                    if deduc <= 0:
                                        deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category)) #Adds a new tuple to numTup with the updated (OOPM, deduc, drug deduc)
                                    print (numTup)
                                    print ("1")
                                    if oopm <= 0: #Tells the program to terminate the smallest loop (claim within a given scenario)
                                    #when the OOPM hits 0 or goes below zero.
                                        break
                                if num > 0: #Deductible exhausted
                                    oopm -= copay + deduc
                                    deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("2")
                                    if oopm <= 0:
                                        break
                            elif TCRem <= 0:
                                if num <= 0: #Deductible not exhausted
                                    oopm -= TC
                                    deduc -= TC
                                    if deduc <= 0:
                                        deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category)) #Adds a new tuple to numTup with the updated (OOPM, deduc, drug deduc)
                                    print (numTup)
                                    print ("1")
                                    if oopm <= 0: #Tells the program to terminate the smallest loop (claim within a given scenario)
                                    #when the OOPM hits 0 or goes below zero.
                                        break
                                if num > 0: #Deductible exhausted
                                    oopm -= TC
                                    deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("2")
                                    if oopm <= 0:
                                        break
                        elif copayBef == "0": #What do do when copay > 0, copay applies after deductible
                            num = TC - deduc #Total Cost minus Deductible
                            if num <= 0: #Deductible is not exhausted
                                deduc -= TC
                                oopm -= TC
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("3")
                                if oopm <= 0:
                                    break
                            if num > 0: #Deductible is exhausted
                                oopm -= deduc + min(copay,abs(TC))
                                deduc = 0
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("4")
                                if oopm <= 0:
                                    break
                    elif coinsurance > 0 and copay == 0: 
                        if coinsAft == "1": #Coinsurance > 0, coinsurance applies after deductible
                            num = TC - deduc
                            if num <= 0: #Deductible is not exhausted
                                deduc -= TC
                                oopm -= TC
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("5")
                                if oopm <= 0:
                                    break
                            if num > 0: #Deductible is exhausted
                                oopm -= deduc + (coinsurance*num)
                                deduc = 0
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("6")
                                if oopm <= 0:
                                    break
                        if coinsAft == "0": #Coinsurance > 0, applies before deductible
                            TCRem = TC - coinsurance*TC
                            num = TCRem - deduc
                            if num <= 0: #Deductible not exhausted
                                oopm -= (TC*coinsurance) + TCRem
                                deduc -= TCRem
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("7")
                                if oopm <= 0:
                                    break
                            if num > 0: #Deductible exhausted
                                oopm -= (coinsurance*TC) + deduc
                                deduc = 0
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("8")
                                if oopm <= 0:
                                    break
                                
                    elif copay > 0 and coinsurance > 0:
                        if copayBef == "1" and coinsAft == "0": #copay before deductible and coinsurance before deductible also.
                            TCRem = TC - copay
                            TCRem = TCRem - coinsurance*TCRem
                            num = TCRem - deduc
                            if TCRem > 0:   
                                if num <= 0: #Deductible not exhausted
                                    oopm -= copay + (TC*coinsurance) + TCRem
                                    deduc -= TCRem
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("9")
                                    if oopm <= 0:
                                        break    
                                if num > 0: #Deductible exhausted
                                    oopm -= copay + (coinsurance*TC) + deduc
                                    deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("10")
                                    if oopm <= 0:
                                        break
                            elif TCRem <= 0:
                                if (TC - deduc) <= 0: #Deductible not exhausted
                                    oopm -= TC
                                    deduc -= TC
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("9.5")
                                    if oopm <= 0:
                                        break  
                                elif (TC - deduc) > 0: #Deductible exhausted
                                    oopm -= TC
                                    deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("10.5")
                                    if oopm <= 0:
                                        break
            
                        elif copayBef == "1" and coinsAft == "1":
                            TCRem = TC - copay
                            num = TCRem - deduc
                            if TCRem > 0:
                                if num <= 0: #Deductible is not exhausted
                                    deduc -= TCRem
                                    oopm -= copay + TCRem
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("11")
                                    if oopm <= 0:
                                        break
                                elif num > 0: #Deductible is exhausted
                                    oopm -= copay + deduc + (coinsurance*num)
                                    deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("12")
                                    if oopm <= 0:
                                        break
                            elif TCRem <= 0:
                                if (TC - deduc) <= 0:
                                    deduc -= TC
                                    oopm -= TC
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("11.5")
                                    if oopm <= 0:
                                        break
                                elif (TC - deduc) > 0: #Deductible is exhausted
                                    oopm -= TC
                                    deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("12.5")
                                    if oopm <= 0:
                                        break
                                    
                        elif copayBef == "0" and coinsAft == "1":
                            num = TC - deduc #Total Cost minus Deductible
                            if num <= 0: #Deductible is not exhausted
                                deduc -= TC
                                oopm -= TC
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("13")
                                if oopm <= 0:
                                    break   
                            if num > 0: #Deductible is exhausted
                                TCRem = TC - deduc - copay
                                if TCRem > 0:
                                    oopm -= deduc + copay + coinsurance*TCRem
                                    deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("14")
                                    if oopm <= 0:
                                        break
                                elif TCRem <= 0:
                                    oopm -= deduc + TC
                                    deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("14.5")
                                    if oopm <= 0:
                                        break
                    
                    elif copay == 0 and coinsurance == 0: #Copay and coinsurance both apply, but no deductible
                        num = TC - deduc
                        if num <= 0: 
                            deduc -= TC
                            oopm -= TC
                            if drugDeduc >= deduc:
                                drugDeduc = deduc
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("15")
                            if oopm <= 0:
                                break
                        if num > 0:
                            oopm -= deduc
                            deduc = 0
                            if drugDeduc >= deduc:
                                drugDeduc = deduc
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("16")
                            if oopm <= 0:
                                break
                            
                elif deducBool == "1" and planSpecs[7] != "0" and (category == "Rx Generic" or category == "Rx Preferred Brand" or category == "Rx Non Preferred Brand" or category == "Rx Specialty"):
                    #Situation where deductible applies, and drug deductible exists/applies to claim
                    if copay > 0 and coinsurance == 0:
                        if copayBef == "1": #Copay > 0 and applies before deductible
                            TCRem = TC - copay
                            num = TCRem - drugDeduc
                            if TCRem > 0:   
                                if num <= 0: # Drug Deductible not exhausted
                                    oopm -= copay + TCRem
                                    drugDeduc -= TCRem
                                    deduc -= TCRem
                                    if deduc <= 0:
                                        deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("17")
                                    if oopm <= 0:
                                        break
                                if num > 0: #Drug Deductible exhausted
                                    oopm -= copay + drugDeduc
                                    deduc -= drugDeduc
                                    drugDeduc = 0 
                                    if deduc <= 0:
                                        deduc = 0
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("18")
                                    if oopm <= 0:
                                        break
                            elif TCRem <= 0:
                                oopm -= TC
                                if deduc <= 0:
                                    deduc = 0
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("17.5")
                                if oopm <= 0:
                                    break
                                
                        if copayBef == "0": #Copay > 0 and applies after deductible
                            num = TC - drugDeduc
                            TCRem = num - copay
                            if num <= 0: #Drug Deductible is not exhausted
                                drugDeduc -= TC
                                if drugDeduc >= 0:
                                    drugDeduc = 0
                                deduc -= TC
                                oopm -= TC
                                if deduc <= 0:
                                    deduc = 0
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("19")
                                if oopm <= 0:
                                    break
                            if num > 0: #Drug Deductible is exhausted
                                deduc -= drugDeduc
                                if deduc <= 0:
                                    deduc = 0
                                oopm -= (drugDeduc + min(copay,abs(TCRem)))
                                drugDeduc = 0
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("20")
                                if oopm <= 0:
                                    break
                                
                    elif coinsurance > 0 and copay == 0: 
                        if coinsAft == "1": #Coinsurance > 0 and applies after deductible
                            num = TC - drugDeduc
                            if num <= 0: #Drug Deductible is not exhausted
                                deduc -= TC
                                drugDeduc -= TC
                                oopm -= TC
                                if deduc <= 0:
                                    deduc = 0
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("21")
                                if oopm <= 0:
                                    break
                            if num > 0: #Drug Deductible is exhausted
                                deduc -= drugDeduc
                                oopm -= drugDeduc + (coinsurance*num)
                                drugDeduc = 0
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("22")
                                if oopm <= 0:
                                    break
                                
                        if coinsAft == "0": #Coinsurance > 0 and applies before deductible
                            TCRem = TC - coinsurance*TC
                            num = TCRem - drugDeduc
                            if num <= 0: #Drug Deductible not exhausted
                                oopm -= (TC*coinsurance) + TCRem
                                deduc -= TCRem
                                drugDeduc -= TCRem
                                if deduc <= 0:
                                    deduc = 0
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("23")
                                if oopm <= 0:
                                    break
                            if num > 0: #Drug Deductible exhausted
                                oopm -= (coinsurance*TC) + drugDeduc
                                deduc -= drugDeduc
                                drugDeduc = 0
                                if deduc <= 0:
                                    deduc = 0
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("24")
                                if oopm <= 0:
                                    break
                                
                    elif copay > 0 and coinsurance > 0:
                        if copayBef == "1" and coinsAft == "0":
                            TCRem = TC - copay
                            TCRem = TCRem - coinsurance*TCRem
                            num = TCRem - drugDeduc
                            if (TC - copay) > 0:
                                if num <= 0: #Drug Deductible not exhausted
                                    oopm -= copay + (TCRem*coinsurance) + TCRem
                                    drugDeduc -= TCRem
                                    deduc -= TCRem
                                    if deduc <= 0:
                                        deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("25")
                                    if oopm <= 0:
                                        break   
                                elif num > 0: #Drug Deductible is exhausted
                                    oopm -= copay + (TCRem*coinsurance) + drugDeduc
                                    deduc -= drugDeduc
                                    drugDeduc = 0
                                    if deduc <= 0:
                                        deduc = 0
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("26")
                                    if oopm <= 0:
                                        break  
                            elif (TC - copay) <= 0:
                                oopm -= TC
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("25.5")
                                if oopm <= 0:
                                    break   

                        elif copayBef == "1" and coinsAft == "1":
                            TCRem = TC - copay
                            num = TCRem - drugDeduc
                            if (TC - copay) > 0:
                                if num <= 0: #Drug Deductible is not exhausted
                                    oopm -= copay + TCRem
                                    drugDeduc -= TCRem
                                    deduc -= TCRem
                                    if deduc <= 0:
                                        deduc = 0
                                    if drugDeduc >= deduc:
                                        drugDeduc = deduc
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("27")
                                    if oopm <= 0:
                                        break
                                elif num > 0: #Deductible is exhausted
                                    oopm -= copay + drugDeduc + (coinsurance*num)
                                    deduc -= drugDeduc
                                    drugDeduc = 0
                                    if deduc <= 0:
                                        deduc = 0
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("28")
                                    if oopm <= 0:
                                        break
                            elif (TC - copay) <= 0:
                                oopm -= TC
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("27.5")
                                if oopm <= 0:
                                    break   
                                
                            
                        elif copayBef == "0" and coinsAft == "1":
                            num = TC - drugDeduc #Total Cost minus Drug Deductible
                            if num <= 0: #Drug Deductible is not exhausted
                                drugDeduc -= TC
                                oopm -= TC
                                deduc -= TC
                                if deduc <= 0:
                                    deduc = 0
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("29")
                                if oopm <= 0:
                                    break   
                            elif num > 0: #Deductible is exhausted
                                if num > copay:
                                    TCRem = TC - drugDeduc - copay
                                    oopm -= drugDeduc + copay + coinsurance*TCRem
                                    deduc -= drugDeduc
                                    drugDeduc = 0
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("29.5")
                                    if oopm <= 0:
                                        break
                                elif num <= copay:
                                    oopm -= drugDeduc + num
                                    deduc -= drugDeduc
                                    drugDeduc = 0
                                    numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                    print (numTup)
                                    print ("29.7")
                                    if oopm <= 0:
                                        break
                                     
                    elif copay == 0 and coinsurance == 0: #Deductible applies but copay and coinsurance = 0
                        num = TC - drugDeduc
                        if num <= 0: #Drug Deductible not exhausted
                            oopm -= TC
                            deduc -= TC
                            drugDeduc -= TC
                            if deduc <= 0:
                                deduc = 0
                            if drugDeduc >= deduc:
                                drugDeduc = deduc
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("30")
                            if oopm <= 0:
                                break
                        elif num > 0: #Drug Deductible exhausted
                            oopm -= drugDeduc
                            deduc -= drugDeduc
                            drugDeduc = 0
                            if deduc <= 0:
                                deduc = 0
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("31")
                            if oopm <= 0:
                                break
                elif deducBool == "0" and planSpecs[36] == "1" and category == "Inpatient Facility": #The claim is an inpatient visit, and 
                    #the plan requires us to pay copay for every day spent in clinic
                    if copay > 0: 
                        oopm -= copay*inpatientDays
                        numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                        print (numTup)
                        print ("32")
                        if oopm <= 0:
                            break
                    elif coinsurance > 0:
                        oopm -= coinsurance*TC
                        numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                        print (numTup)
                        print ("33")
                        if oopm <= 0:
                            break
                elif deducBool == "1" and planSpecs[36] == "1" and category == "Inpatient Facility": #Inpatient days matters (again),
                    #but deductible also applies
                    if copay > 0:
                        if copayBef == "1":
                            oopm -= copay*inpatientDays + (TC - copay*inpatientDays)
                            deduc -= (TC - copay*inpatientDays)
                            if deduc <= 0:
                                deduc = 0
                            if drugDeduc >= deduc:
                                drugDeduc = deduc
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("34")
                            if oopm <= 0:
                                break
                        if copayBef == "0":
                            num = TC - deduc
                            if num <= 0: #Deductible is not exhausted)
                                deduc -= TC
                                oopm -= TC
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("35")
                                if oopm <= 0:
                                    break
                            elif num > 0: #Deductible is exhausted
                                oopm -= (deduc + copay*inpatientDays)
                                deduc = 0
                                if drugDeduc >= deduc:
                                    drugDeduc = deduc
                                numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                                print (numTup)
                                print ("36")
                                if oopm <= 0:
                                    break
                elif deducBool == "0" and ((planSpecs[36] == "0") or (planSpecs[36] != "0" and category != "Inpatient Facility")):
                    #Simplest scenario, where no deductible applies, and drug deductible/number of inpatient days do not affect costs
                    if copay > 0 and coinsurance == 0:
                        num = TC - copay
                        if num > 0:
                            oopm -= copay
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("37")
                            if oopm <= 0:
                                break
                        elif num <= 0:
                            oopm -= TC
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("37.5")
                            if oopm <= 0:
                                break         
                    elif coinsurance > 0 and copay == 0:
                        oopm -= coinsurance*TC
                        numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                        print (numTup)
                        print ("38")
                        if oopm <= 0:
                            break
                    elif copay > 0 and coinsurance > 0:
                        TCRem = TC - copay
                        if TCRem > 0:
                            oopm -= copay + coinsurance*TCRem
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("39")
                            if oopm <= 0:
                                break
                        elif TCRem <= 0:
                            oopm -= TC
                            numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                            print (numTup)
                            print ("40")
                            if oopm <= 0:
                                break
                    elif copay == 0 and coinsurance == 0:
                        numTup[-1].append((oopm,deduc,drugDeduc,claimlength,visit,metalLevel,category))
                        print (numTup)
                        print ("41")
                        if oopm <= 0:
                            break
                        
            if oopm <= 0:
                #Once OOPM hits 0 for a particular insurance plan, tells program to create a list with the Plan ID, the updated OOPM,
                #deductible and drug deductible, and the number of claims that have been passed through the plan. This list gets appended
                #to the dictionary 'retdict', which eventually gets returned by this function, mapping each scenario to the cost
                #information associated with each claim.
                finallist = [str(scenario),numTup[0][5],numTup[-1]]
                print (finallist)
                print (numTup)
                #claimlen = len(finallist[2])-1
                print ("claimlength = " + str(claimlength))
                #finallist.append(claimlength)
                templist = []
                for ele in finallist[2]:
                    templist.append([finallist[1], ele[5], ele[0], ele[1], ele[2], ele[3], ele[4], ele[6]])
                retdict[scen].append(templist)
                del numTup[-1][1:]
                #break
            
            else:
                
                finallist = [str(scenario),numTup[0][5],numTup[-1]]
                print (finallist)
                print (numTup)
                print (numTup[-1])
                #claimlen = len(finallist[2])-1
                print ("claimlen = " + str(claimlength))
                #finallist.append(claimlen)
                templist = []
                for ele in finallist[2]:
                    templist.append([finallist[1], ele[5], ele[0], ele[1], ele[2], ele[3], ele[4], ele[6]])
                retdict[scen].append(templist)
                del numTup[-1][1:]
                #break
                
    return retdict
