#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            <This class inherits from Mail and represents the confidential emails. It enforces the 'conf' tag and encrypts the email body.>     ###
### Partner A:                                                                                ###
###            <Jayvyn Johansen Bedeau>, SID<001491581>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FA.5.a
class Confidential(Mail):
    """This is a confidential email, inherited from Mail, and it enforces the 'conf' tag and encrypts the body."""
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec

    def __init__(self, m_id,frm,to,date,subject,tag,body):    # DO NOT MODIFY Attributes
        super().__init__(m_id,frm,to,date,subject,tag,body)   # Inherits attributes from parent class DO NOT MODIFY
        self.tag = 'conf'
        self._body = self.encrypt()

    # FA.5.b
    #
    def encrypt(self):
        """Encrypts the email body based on the word count."""
        encrypted_message = []
        word_count = len(self._body.split())

        if word_count == 0:
            return self._body

        for ch in self.body:
            if ch == '.':
                encrypted_message.append(ch)
            elif ch.isdigit():
                num = int(ch)
                # Digit encryption: 1->'a', 2->'b', ..., 9->'i'. 0 remains '0' or is handled outside this range.
                if 1 <= num <= 9:
                    ch = chr(ord('a') + num - 1)
                    encrypted_message.append(ch)
                else:
                    encrypted_message.append(ch)

            elif ch.isalpha():
                position = ord(ch.lower()) - ord('a') + 1
                encrypted_message.append(str(position * word_count))
            else:
                encrypted_message.append(ch)

        return "".join(encrypted_message)