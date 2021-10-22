from caesarshift import CaesarShift
import app
import random


def test():
    """Run all tests."""
    test_caesarshift()
    test_brute_force()


def test_caesarshift():
    """
    Test encryption / decryption.
    
    Decrypt an enrypted message and
    compare it to the original.
    cryptokey = 1 makes it easier to spot
    an error in the encryption step.
    """
    cs = CaesarShift(cryptokey=1)
    ui = app.ui(cs)

    ui.header()
    print("Testing Encryption / Decryption")
    print("with cryptokey", cs.cryptokey)

    print("\nEnter test message,")
    message_in = input("leave empty for default: ")
    if not message_in:
        message_in = "Only the true Messiah denies his divinity!"

    message_encrypted = cs.encrypt(message_in)
    message_decrypted = cs.decrypt(message_encrypted)

    print("\nEncrypt original:\n" + message_encrypted)
    print("\nDecrypt encrypted:\n" + message_decrypted)

    if message_in == message_decrypted:
        print("\nSuccess: Messages match")
    else:
        print("\nFail: Messages don't match")

    ui.footer()


def test_brute_force():
    """
    Test brute force decryption.

    The line number of the only legit decryption
    is the cryptokey used for encryption.
    """

    cs = CaesarShift()
    ui = app.ui(cs)

    cs.cryptokey = random.randint(1, 25)
    secret_key = cs.cryptokey

    message_in = "People called Romanes, they go the house."
    message_encrypted = cs.encrypt(message_in)

    ui.header()
    print("Testing Brute Force Decryption")
    print("with random cryptokey\n")

    shiftings = cs.brute_force_decrypt(message_encrypted)
    for i, line in enumerate(shiftings):
        print("{:2}: {}".format(i+1, line))

    legit_line = ui.get_int("\nEnter line number of legit text: ", 1, 25)

    if legit_line == secret_key:
        print("\nSuccess: cryptokey and line number match")
    else:
        print("Fail: cryptokey and line number don't match")

    ui.footer()
