# write function "readme"
'''
Going to take some TLC to get this function going. 
'''

def readme(
        undergradlist = [], trainingset = None, testset = None, 
        formula = None, features = None, n_subset = None, 
        prob_wt = None, boot_se = None, nboot = None, 
        printit = None):
    '''
    Parameters call in data from a master table and functions
    from VA, the R library. Currently will not run until
    functions from this library are completed.
    '''
    if testset == None:
        testset = undergradlist[:testset]
    
    if trainingset == None:
        trainingset = undergradlist[:trainingset]

    hospital = trainingset[,1]
    community = testset[,1]
    
    if formula == None:
        formula = undergradlist[:formula]
        
    if features == None:
        features = undergradlist[:features]

    if n_subset == None:
        n_subset = undergradlist[:n_subset]

    if prob_wt == None:
        prob_wt = undergradlist[:prob_wt]

    if boot_se == None:
        boot_se = undergradlist[:boot_se]

    if printit == None:
        printit = undergradlist[:printit]

    if nboot == None:
        nboot = undergradlist[:nboot]

    return va.va_function(
        formula = va.formula, data = [hospital = va.hospital,
                                   community = va.community],
        nsymp = va.features, n_subset = va.n_subset,
        prob_wt = va.prob_wt, boot_se = va.boot_se,
        nboot = va.nboot, printit = va.printit)






    
    

