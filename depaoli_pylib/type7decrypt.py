#!/usr/bin/env python
#
# Rough script (or module) to decrypt Cisco Type 7 passwords.
#
#############################################################


def type7decrypt(type7_string):
    """
    Function to decrypt Cisco Type 7 passwords.
    """
    
    type0_string = ''

    cipher_key = ( 0x64, 0x73, 0x66, 0x64, 0x3b, 0x6b, 0x66, 0x6f, 0x41,
                   0x2c, 0x2e, 0x69, 0x79, 0x65, 0x77, 0x72, 0x6b, 0x6c,
                   0x64, 0x4a, 0x4b, 0x44, 0x48, 0x53, 0x55, 0x42 )

    cipher_index = int(type7_string[:2])
    encrypted_password = [int('0x' + type7_string[i:i+2], 16) for i in range(2, len(type7_string), 2)]

    for i in range(len(encrypted_password)):
        type0_string += (chr(cipher_key[(i + cipher_index) % len(cipher_key)] ^ encrypted_password[i]))

    return type0_string



if __name__ == '__main__':
    type7_string = raw_input('Enter Type7 string: ')
    type0_string = type7decrypt(type7_string)
    print 'The password is: {0}'.format(type0_string)
