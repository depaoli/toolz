#!/usr/bin/env python
#
# Rough script (or module) to find duplicated files
# as fast as possible.
#
# The tradeoff is to use a fast non-cryptographic
# hash function (no need to prevent attacks/malicious input)
# applied only to a small part of the file, and then
# cross-checking this hash with the file size (reducing
# chances of collision).
#
# MurmurHash3 has excellent performance and Python module
# is optimised for x86 (both 32 and 64 bit) CPU.
#
#############################################################


import os
from smhasher import murmur3_x64_64 as murmur3


def hash_file(path, blocksize=65536):
    """
    Return an Hash of the file passed as parameter.
    For performance reasons (mem & speed), by default, only the initial part of the file
    up to 'blocksize' is read and hashed (it's mandatory to check the file size in the
    duplicate search).
    If a negative "blocksize" (eg. -1) is passed, the entire contents of the file
    will be read.
    """
    
    # NOTE:
    # - from the Help of Python built-in function read(): "Notice that when in
    #   non-blocking mode, less data than what was requested may be returned"
    # - read() Linux system call on file descriptors is, by default, blocking.
    # Because we need consistent data from files for hashing comparison, we should ensure
    # that no weird different logic exist between the 2 functions above (or force the flag
    # through fcntl).
    with open(path, 'rb') as f:
        data = f.read(blocksize)
        hash = murmur3(data)
        f.close()
    
    return hash

def find_dup_fast(root_path, verbose=False):
    """
    Given a root path from which the search starts, it returns a dictionary with the
    hash of part of the files as key, with a nested dictionary with the size of the file
    as key and with an array containing path/s to the file names as value.
    """
    
    dups = {}
    for root, dirs, files in os.walk(root_path):
        if verbose: print('Scanning {}...'.format(root))
        for filename in files:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            file_hash = hash_file(file_path)
            
            if not file_hash in dups:
                dups[file_hash] = {}
            if not file_size in dups[file_hash]:
                dups[file_hash][file_size] = []
            
            dups[file_hash][file_size].append(file_path)
    
    return dups


if __name__ == '__main__':
    root_path = raw_input('Enter the root path: ')
    dups = find_dup_fast(root_path, verbose = True)
    for digest in dups:
        for size in dups[digest]:
            if len(dups[digest][size]) > 1:
                print '\nFollowing files seem equal (hash digest {}, size {}):'.format(digest, size)
                print dups[digest][size], '\n'
