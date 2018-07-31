#!/usr/bin/env python3
import argparse
import re

def parse_encryption_algorithms_list_from_file(file_path):
    """Parses a list of ciphersuites from a file.

    Format of file:
    CIPHERSUITE_ID[:id] CIPHERSUITE_NAME[:str] TAG[:str]
    """
    with open(file_path, 'r') as sc_file:
        ciphersuites = [line.strip().split(' ') for line in sc_file.readlines()]

    ciphersuites = [ciphersuite[1] for ciphersuite in ciphersuites if len(ciphersuite) > 1]

    print(f'Total Ciphersuites: {len(ciphersuites)}')

    return ciphersuites

def get_encr_alg_from_ciphersuite(ciphersuite):
    ENC_ALG_REGEX = 'WITH-(?P<encr_alg>[^ \n]+)'
    pattern = re.compile(ENC_ALG_REGEX)
    res = pattern.search(ciphersuite)

    return res.group('encr_alg')

def get_unique_encryption_algorithms_from_file(file_path):
    all_ciphers = parse_encryption_algorithms_list_from_file(file_path)

    enc_algs = set()

    for cipher in all_ciphers:
        alg = get_encr_alg_from_ciphersuite(cipher)
        enc_algs.add(alg)

    print(f'Total Unique Encryption Algorithms: {len(enc_algs)}')
    return enc_algs

def get_all_lines_from_file(file_path):
    with open(file_path, 'r') as sc_file:
        ciphersuites = sc_file.readlines()
    return ciphersuites

def filter_ordered_ciphersuites(all_ciphers, encr_algs):
    unique_ciphersuites = set()

    while(encr_algs):
        encr_alg = encr_algs.pop()
        for cipher in all_ciphers:
            cipher_enc_alg = get_encr_alg_from_ciphersuite(cipher)
            if encr_alg == cipher_enc_alg:
                unique_ciphersuites.add(cipher)
                break
    return unique_ciphersuites

def write_lines_to_file(lines, path):
    with open(path, 'w') as out_file:
        out_file.writelines(lines)
    print(f'Total lines written: {len(lines)}')

def run(ciphers_file, ordered_file, output_file):
    unique_enc_algs = get_unique_encryption_algorithms_from_file(ciphers_file)
    ordered_file_lines = get_all_lines_from_file(ordered_file)
    ordered_unique_encr_alg_ciphersuites = filter_ordered_ciphersuites(ordered_file_lines, unique_enc_algs)
    write_lines_to_file(ordered_unique_encr_alg_ciphersuites, output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Extract the minimum set of mbedTLS ciphersuites with unique encryption algorithms\n'
    'Assumes that the input files use the mbedTLS ciphersuite naming. Each line'
    ' in the ciphersuite files is assumed to have the following format:\n'
    '[ciphersuite_id] [ciphersuite_name]\n'
    'Check the example text files within this repository.')
    parser.add_argument('ciphers', type=str, help='file containing the complete list of ciphersuites')
    parser.add_argument('ordered', type=str, help='file containing the ciphersuites ordered by preferrence.'
                        'This file can be the same as the <ciphers> file.')
    parser.add_argument('output', type=str, help='output file name')

    args = parser.parse_args()

    run(args.ciphers, args.ordered, args.output)
