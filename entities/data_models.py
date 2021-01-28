from datetime import date

class CallData():
    """
    Structure to hold data from FFEIC call data summaries
    """

    def __init__(self):
        self.period = None
        self.idrssd = None
        self.fdic = None
        self.bank_name = None
        self.address = None
        self.field_dict = None

    @property
    def period(self):
        return self.__period
    @period.setter
    def period(self, period):
        if type(period) == date or period == None:
            self.__period = period
        else:
            try:
                self.__period = date.strptime(period, "%m/%d/%Y")
            except:
                raise (
                TypeError("period type must be either date, string in format 'mm/dd/YYYY' or None"))

    @property
    def idrssd(self):
        return self.__idrssd
    @idrssd.setter
    def idrssd(self, idrssd):
        if type(idrssd) == int or idrssd == None:
            self.__idrssd = idrssd
        else:
            try:
                self.__idrssd = int(idrssd)
            except:
                raise TypeError("idrssd type must be convertible int or None")

    @property
    def fdic(self):
        return self.__fdic
    @fdic.setter
    def fdic(self, fdic):
        if type(fdic) == int or fdic == None:
            self.__fdic = fdic
        else:
            try:
                self.__fdic = int(fdic)
            except:
                raise TypeError("fdic type must be convertible int or None")

    @property
    def bank_name(self):
        return self.__bank_name
    @bank_name.setter
    def bank_name(self, bank_name):
        if type(bank_name) == str or bank_name == None: 
            self.__bank_name = bank_name
        else:
            raise TypeError("bank_name type must be string or None")

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        if type(address) == str or address == None: 
            self.__address = address
        else:
            raise TypeError("address type must be string or None")

    @property
    def field_dict(self):
        return self.__field_dict
    @field_dict.setter
    def field_dict(self, field_dict):
        if type(field_dict) == dict or field_dict == None: 
            self.__field_dict = field_dict
        else:
            raise TypeError("field_dict type must be dict or None")

class AggregateData():
    """
    Structure to hold aggregated data from FFEIC call data summaries
    """

    def __init__(self):
        self.aggregation = None
        self.idrssd = None
        self.field_dict = None
        self.intersection_dict = None

    @property
    def aggregation(self):
        return self.__aggregation
    @aggregation.setter
    def aggregation(self, aggregation):
        if type(aggregation) == str or aggregation == None: 
            self.__aggregation = aggregation
        else:
            raise TypeError("aggregation type must be string or None")

    @property
    def idrssd(self):
        return self.__idrssd
    @idrssd.setter
    def idrssd(self, idrssd):
        if type(idrssd) == int or idrssd == None:
            self.__idrssd = idrssd
        else:
            try:
                self.__idrssd = int(idrssd)
            except:
                raise TypeError("idrssd type must be convertible int or None")

    @property
    def field_dict(self):
        return self.__field_dict
    @field_dict.setter
    def field_dict(self, field_dict):
        if type(field_dict) == dict or field_dict == None: 
            self.__field_dict = field_dict
        else:
            raise TypeError("field_dict type must be dict or None")

    @property
    def intersection_dict(self):
        return self.__intersection_dict
    @intersection_dict.setter
    def intersection_dict(self, intersection_dict):
        if type(intersection_dict) == dict or intersection_dict == None: 
            self.__intersection_dict = intersection_dict
        else:
            raise TypeError("intersection_dict type must be dict or None")