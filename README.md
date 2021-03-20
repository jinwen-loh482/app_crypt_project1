# app_crypt_project1

dependencies:
- python3
- library: random
- library: numpy
- library: argparse
- library: statistics
- library: difflib

extra work dependencies:
- library: time

Program takes an input string that is the ciphertext. The program can be run as follows:
```
python zavoral_zhou_loh-decrypt-binary.py
# then enter a ciphertext when prompted
```
OR it can be run as follows:
```
python zavoral_zhou_loh-decrypt-binary.py --ciphertext <ciphertext>
```

The program demonstrated success for test 1 and minimal success for test 2.

Successes:
- cyclic and random encryption with t between 1 and 24 without insertion
- random insertion in test 1

Problems:
- random insertion in test 2 (good sometimes for all insertions in the same relative location)
- t greater than 20 with all unique key shifts and random insertion greater than 10 in test 1


Contributors: Zavoral, Zhou, Loh