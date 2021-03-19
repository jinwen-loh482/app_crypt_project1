import argparse
from ic_attack import ic_attack
from unique_shift_attack import unique_shift_attack

def main():
    parser = argparse.ArgumentParser(description='Given a ciphertext, attempts to decrypt it into the correct plaintext.')
    parser.add_argument('ciphertext', help='The ciphertext to be analyzed.')
    cmdline = parser.parse_args()
    ciphertext = cmdline.ciphertext
    message_pp = ic_attack(ciphertext)
    print(unique_shift_attack(message_pp, ciphertext))

if __name__ == "__main__":
    main()