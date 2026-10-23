#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <This is the central management class for the Outlook Simulator. It holds the _mailbox and contains methods for all mailbox operations.>     ###
### Partner A:                                                                                ###
###            <Jayvyn Johansen Bedeau>, SID<001491581>                              ###
### Partner B:                                                                                ###
###            <Manjish Prajapati>, SID<001490165>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Confidential import *
from Personal import *
from datetime import datetime

class MailboxAgent:
    """<This is the documentation for MailboxAgent. It contains methods for all mail-related operations as defined in the CW spec."""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

# FEATURES A (Partner A)
    # FA.1
    # 
    def get_email(self, m_id):
        """Retrieves an email by its ID, marks it as read, and returns the Mail object."""
        for mail in self._mailbox:
            if str(mail.m_id) == str(m_id):
                mail.read = True
                return mail
        return None

    # FA.3
    # 
    def del_email(self, m_id):
        """'Deletes' an email by changing its tag to 'bin'."""
        for mail in self._mailbox:
            if str(mail.m_id) == str(m_id):
                mail.tag = 'bin'
                return mail
        return None

    # FA.4
    # 
    def filter(self, frm):
        """Filters and returns a list of all emails sent from the specified sender."""
        results = []
        clean_frm = frm.strip().lower()
        for mail in self._mailbox:
            if mail.frm.strip().lower() == clean_frm:
                results.append(mail)

        return results

    # FA.5
    # 
    def sort_date(self):
        """Sorts the internal mailbox list by the email date in ascending order (oldest first) and returns the sorted list."""

        def get_date_key(mail):
            try:
                return datetime.strptime(mail.date.strip(), '%d/%m/%Y')
            except ValueError:
                return datetime.min

        self._mailbox.sort(key=get_date_key)
        return self._mailbox


# FEATURES B (Partner B)
    # FB.1
    # 
    def show_emails(self):
        """Returns the entire list of Mail objects in the mailbox."""
        return self._mailbox

    # FB.2
    # 
    def mv_email(self, m_id, tag):
        """Moves an email by its ID to a new folder by changing its tag."""
        for mail in self._mailbox:
            if str(mail.m_id) == str(m_id):
                mail.tag = tag
                return mail
        return None

    # FB.3
    # 
    def mark(self, m_id, m_type):
        """Marks an email as either 'read' or 'flagged' based on the m_type parameter."""
        for mail in self._mailbox:
            if mail.m_id == m_id:
                if m_type == "read":
                    mail.read = True
                elif m_type == "flag":
                    mail.flag = True
                return mail
        return None

    # FB.4
    # 
    def find(self, date):
        """Finds and returns a list of all emails received on the specified date."""
        results = []
        clean_date = date.strip()
        for mail in self._mailbox:
            if mail.date.strip() == clean_date:
                print(mail)
                results.append(mail)
        return results

    # FB.5
    # 
    def sort_from(self):
        """Sorts the internal mailbox list alphabetically by the sender's email address and returns the sorted list."""

        def get_sender(mail):
            return mail.frm.strip().lower()

        self._mailbox.sort(key=get_sender)
        return self._mailbox


# FEATURE 6 (Partners A and B)
    # 
    def add_email(self, frm, to, date, subject, tag, body):
        """Creates a new email with a unique ID and appends it to the mailbox."""
        if len(self._mailbox) == 0:
            m_id = 1
        else:
            max_id = max([int(mail.m_id) for mail in self._mailbox])
            m_id = max_id + 1

        m_id = str(m_id)
        # code must generate unique m_id

        new_email = None

        match tag.lower():
            # FA.6
            case 'conf':     # executed when tag is 'conf'
                new_email = Confidential(m_id, frm, to, date, subject, tag, body)
            # FB.6
            case 'prsnl':    # executed when tag is 'prsnl'
                new_email = Personal(m_id, frm, to, date, subject, tag, body)
            # FA&B.6
            case _:          # executed when tag is neither 'conf' nor 'prsnl'
                new_email = Mail(m_id, frm, to, date, subject, tag, body)

        self._mailbox.append(new_email)
        return new_email