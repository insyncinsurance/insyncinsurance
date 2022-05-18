def getEndorsements(dictionary, policyfield, giofield):
    tempList = []
    endorsements = []

    for part in parts:
        if ge(part['partname'].find('GenericInsuredObject'), 0):
            tempList.append(part[giofield])

    tempList.append(policyfield)

    for i in tempList:
        if i in dictionary:
            endorsements.append(dictionary[i])

    return list(set(endorsements))