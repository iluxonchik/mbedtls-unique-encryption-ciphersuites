# mbedTLS Unique Encryption Ciphersuites Extractor

Extract the minimum set of mbedTLS ciphersuites with unique encryption
algorithms Assumes that the input files use the mbedTLS ciphersuite naming.
Each line in the ciphersuite files is assumed to have the following format:
`[ciphersuite_id] [ciphersuite_name]` Check the example text files within this
repository.

## Usage

```
uec.py [-h] ciphers ordered output

Extract the minimum set of mbedTLS ciphersuites with unique encryption
algorithms Assumes that the input files use the mbedTLS ciphersuite naming.
Each line in the ciphersuite files is assumed to have the following format:
[ciphersuite_id] [ciphersuite_name] Check the example text files within this
repository.

positional arguments:
  ciphers     file containing the complete list of ciphersuites
  ordered     file containing the ciphersuites ordered by preferrence.This
              file can be the same as the <ciphers> file.
  output      output file name

optional arguments:
  -h, --help  show this help message and exit
```

## About

Part of the toolkit used in profiling and analyzing the TLS implementation
by the mbedTLS library.

