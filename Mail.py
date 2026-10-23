#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Mail Class                                                             ###
###            <This is the base class for all email objects in the Outlook Simulator. All email attributes are hold here. It manages the read and flag status. It provides properties for read access to all the attributes and setters.>     ###
### Partner A:                                                                                ###
###            <Jayvyn Johansen Bedeau>, SID<001491581>                              ###
### Partner B:                                                                                ###
###            <Manjish Prajapati>, SID<001490165>                              ###
#################################################################################################
import pprint
# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

class Mail:
    """This is a standard email object in the Outlook Simulator, and it provides properties and setters for core email attributes."""
    # DO NOT CHANGE CLASS OR METHOD NAMES
    def  __init__(self,m_id,frm,to,date,subject,tag,body):
        self._m_id = m_id
        self._frm = frm
        self._to = to
        self._subject = subject
        self._date = date
        self._tag = tag      # reference to Outlook mail folder email is stored in
                             # e.g. tag0 = inbox, tag1 = bin, tag2 = private, tag3 = bank_acct, tag4 = COMP1811, etc.
        self._body = body
        self._flag = False   # Boolean indicating whether email is important
        self._read = False   # Boolean indicating whether the email is read or not.

    # Format should be done from pretty print.
    def __str__(self):
        return f"m_id:{self.m_id}\tfrom:{self.frm}\t|{self.to}\t|{self.date}|{self.subject}|{self.tag}|{self.read}|{self.flag}"

    @property
    def m_id(self):
        return self._m_id

    @property
    def frm(self):
        return self._frm

    @property
    def to(self):
        return self._to

    @property
    def date(self):
        return self._date

    @property
    def body(self):
        return self._body

    @property
    def subject(self):
        return self._subject

    @property
    def tag(self):
        return self._tag

    @property
    def read(self):
        return self._read

    @property
    def flag(self):
        return self._flag

    @tag.setter
    # Pre: value in tags.
    def tag(self, value):
        self._tag = value

    @read.setter
    def read(self,value):
        self._read = value

    @flag.setter
    def flag(self,value):
        self._flag = value

# FEATURES A (Partner A)
    # FA.2
    #
    def show_email(self):
        """Display the email contents using pretty print (pprint) for formatted output."""
        email = {'m_id': self.m_id,
                 'frm': self.frm,
                 'to': self.to,
                 'date': self.date,
                 'subject': self.subject,
                 'tag': self.tag,
                 'body': self.body,
                 'flag': self.flag,
                 'read': self.read}
        pprint.pp(email)
