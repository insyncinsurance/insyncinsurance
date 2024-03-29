import re
import NLP

refer = lambda code, *message: info('Refer', [code, ' '.join(map(str, message))])
decline = lambda code, *message: info('Decline', [code, ' '.join(map(str, message))])


def create_message(code):
    def returned_function(*message):
        info('Refer', [code, ' '.join(map(str, message))])

    return returned_function


debug = create_message('Debug')


def get_list(level, field):
    temp_list = []
    for part in parts:
        if ge(part['partname'].find(level), 0):
            temp_list.append(part[field])
    return temp_list


class Policy:
    policies = {}

    def __init__(self, name):
        self.premium = 0
        self.endorsements = []
        self.excess = {}
        self.name = name
        Policy.policies[name] = self.premium

    def add(self, number):
        self.premium += number
        Policy.policies[self.name] = self.premium

    def rate(self, rate):
        self.premium = round(self.premium * rate, 2)
        Policy.policies[self.name] = self.premium

    def override(self, amount):
        self.premium = amount
        Policy.policies[self.name] = self.premium

    def add_endorsement(self, endorsement):
        if endorsement not in self.endorsements:
            self.endorsements.append(endorsement)
        else:
            pass

    def remove_endorsement(self, endorsement):
        self.endorsements.remove(endorsement)

    def get_endorsements(self):
        return self.endorsements

    def discount(self, amount):
        self.premium -= amount
        Policy.policies[self.name] = self.premium

    def get_premium(self):
        return self.premium

    @staticmethod
    def combine(*lists):
        return [i for sub in lists for i in sub]

    def add_excess(self, excess_type, amount):
        if excess_type in self.excess:
            self.excess[excess_type] += amount
        else:
            self.excess[excess_type] = amount

    def remove_excess(self, excess_type, amount=None):
        if amount is None:
            self.excess.pop(excess_type)
        elif excess_type in self.excess:
            self.excess[excess_type] -= amount
        else:
            pass

    def rate_excess(self, excess_type, rate):
        self.excess[excess_type] = round(self.excess[excess_type] * rate, 2)

    def discount_excess(self, excess_type, amount):
        self.excess[excess_type] -= amount

    def get_excess(self, excess_type):
        return self.excess[excess_type]

    def total_excess(self):
        return sum(self.excess.values())

    @staticmethod
    def total():
        return sum(Policy.policies.values())

    @staticmethod
    def stringify_total():
        return str('{0:,.2f}'.format(float(sum(Policy.policies.values()))))


class debugging:
    def __init__(self):
        pass

    debug_mode = False

    @staticmethod
    def toggle():
        debugging.debug_mode = not debugging.debug_mode

    @staticmethod
    def send(*message):
        if debugging.debug_mode:
            debug(*message)

    @staticmethod
    def breakdown():
        if debugging.debug_mode:
            for k, v in Policy.policies.items():
                debug(k, 'has a premium of', v)


class Postcodes():
    def __init__(self, Postcode):
        self.Postcode = Postcode
        self.matches = re.findall(r'^(([A-Z][A-Z]{0,1})([0-9][A-Z0-9]{0,1})) {0,}(([0-9])([A-Z]{2}))$', self.Postcode)

    def area(self):
        return self.matches[0][1]

    def district(self):
        return self.matches[0][0]

    def sector(self):
        return self.matches[0][0] + self.matches[0][4]

    def unit(self):
        return self.matches[0][0] + self.matches[0][3]

    def contains(self, comparative):
        postcode_unit = self.matches[0][0] + self.matches[0][3]
        if isinstance(comparative, list):
            for i in comparative:
                if i in postcode_unit:
                    return True
            return False
        else:
            if comparative in postcode_unit:
                return True
            else:
                return False

    def validate(self):
        pattern = 'not matched'
        pc = self.replace(" ", "")
        # e.g. W27XX
        if len(pc.replace(" ", "")) == 5:
            pattern = re.compile("^[a-zA-Z]{1}[0-9]{2}[a-zA-Z]{2}")
        # e.g. TW27XX
        elif len(pc.replace(" ", "")) == 6:
            pattern = re.compile("^[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}")
        # e.g. TW218FF
        elif len(pc.replace(" ", "")) == 7:
            pattern = re.compile("^[a-zA-Z]{2}[0-9]{3}[a-zA-Z]{2}")

        if pattern != 'not matched':
            if pattern.match(pc):
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return self.Postcode


def try_all(array):
    errors = 0
    count = 0
    error_list = []
    debug_mode = debugging.debug_mode
    while lt(count, len(array)):
        variable = array[count]
        try:
            exec ("%s = %s" % (variable + "Dft", variable))
        except NameError:
            errors += 1
            error_list.append(variable)
        count += 1
    if debug_mode:
        debug('All variables have been tested with', errors, 'errors out of', len(array), 'variables.')
        debug('The following variables have errors:', error_list)

    if gt(errors, 0) and debug_mode == False:
        refer('Error', errors, 'errors occurred obtaining Workbench fields. Enable debug mode to see the error.')


def createDocValueDict(array, docValueType, blank='Nil'):
    variableList = []
    i = 1
    while lt(len(array), 10):
        array.append(blank)
        while le(i, 10):
            variableList.append('DocValue_' + docValueType + str(i))
            i += 1

    docValueDict = dict(zip(variableList, array))

    return docValueDict


def addCover(coverCodeList, coverDescList, coverPriceList, coverLimitList, coverCode, coverDesc, coverPrice,
             coverLimit):
    coverCodeList.append(coverCode)
    coverDescList.append(coverDesc)
    coverPriceList.append(coverPrice)
    coverLimitList.append(coverLimit)
    return


def addAddon(addOnCodesList, addOnDescsList, addOnPricesList, addOnCodes, addOnDescs, addOnPrices):
    addOnCodesList.append(addOnCodes)
    addOnDescsList.append(addOnDescs)
    addOnPricesList.append(addOnPrices)
    return


def addFee(feeCodeList, feePriceList, feeCode, feePrice):
    feeCodeList.append(feeCode)
    feePriceList.append(feePrice)
    return


coverCodes = []
coverDescs = []
coverPrices = []
coverLimits = []

addOnCodes = []
addOnDescs = []
addOnPrices = []

feeCodes = []
feePrices = []
