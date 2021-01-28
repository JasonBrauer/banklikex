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

    