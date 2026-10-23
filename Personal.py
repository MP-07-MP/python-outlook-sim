#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                             ###
###            <This class inherits from Mail and represents the personal email. It enforces the 'prsnl' tag and to modify the email body.>     ###
### Partner B:                                                                                ###
###            <Manjish Prajapati>, SID<001490165>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FB.5.a
class Personal(Mail):
    """This class is Personal email, which modifies the stats and stores in 'prsnl' folder."""
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec
    def __init__(self, m_id, frm, to, date, subject, tag, body):  # DO NOT MODIFY Attributes
        super().__init__(m_id, frm, to, date, subject, tag, body)  # Inherits attributes from parent class DO NOT MODIFY
        self._tag = 'prsnl'
        self._body = self.add_stats()
    # FB.5.b
    #
    def add_stats(self):
        """This class modifies the email body by replacing 'Body' with the sender's UID and appends the word statistics."""
        try:
            uid = self.frm.split("@")[0].strip()
        except IndexError:
            uid = "User"

        msg = self._body.replace("Body", uid)
        words = msg.split()
        count = len(words)

        if count > 0:
            lengths = [len(w.strip(".!?")) for w in words]
            avg_len = sum(lengths) // count
            longest = max(lengths)

        else:
            avg_len = 0
            longest = 0

        msg += f" Stats:Word count:{count}, Average word length:{avg_len}, Longest word length:{longest}."
        return msg
    # FB.5.c - Implementation of the required feature
    #
    def show_email(self):
        """Overrides the parent's method to display ONLY Personal Mail objects, including a 'PERSONAL' header."""
        print("PERSONAL")
        print(f"From:{self.frm}")
        print(f"Date: {self.date}")
        print(f"Subject:{self.subject}")
        # self.body property retrieves the modified body containing stats
        print(f"Body:{self.body}")
        print(f"Read?{self.read}")