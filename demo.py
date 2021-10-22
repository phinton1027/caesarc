
from caesarshift import CaesarShift
import app


def demo():
    """Show examples of encryption, decryption and brute force."""
    demo_shift()
    demo_brute()


def demo_shift():
    """Show examples of encryption and decryption."""
    
    encrypt_this = "Your mother was a hamster"
    decrypt_this = "F cxoq fk vlro dbkboxi afobzqflk"  


    cs = CaesarShift(cryptokey=3)
    ui = app.ui(cs)

    encrypted = cs.encrypt(encrypt_this)
    decrypted = cs.decrypt(decrypt_this)


    ui.header()
    print("Demo with cryptokey", cs.cryptokey)

    print("\nEncrypting")
    print("In: ", encrypt_this)
    print("Out:", encrypted)

    print("\nDecrypting")
    print("In: ", decrypt_this)
    print("Out:", decrypted)

    ui.footer()


def demo_brute():
    """Show example of brute force decryption."""

    encrypted = "Erznexnoyr oveq, gur Abejrtvna Oyhr. Ornhgvshy cyhzntr!"


    cs = CaesarShift(cryptokey=13)
    ui = app.ui(cs)


    ui.header()
    print("Demo of Brute Force Decryption")
    print("Showing all shiftings for")
    print("    " + encrypted + "\n")


    shiftings = cs.brute_force_decrypt(encrypted)
    
    for i, line in enumerate(shiftings):
        print("{:2}: {}".format(i+1, line))


    print("\nResult of Brute Force Attack:")
    print("Cryptokey was 13, as line 13 contains legit text.")
    ui.footer()























































def order66():
    print("\n\nOrder 66  [imperial march blaring]")
    print("\nYou could not resist the temptation of the Dark Side.")
    print("So you're rewarded with an Easter Egg:")
    print("\n1: Determine the cryptokey corresponding to 66.")
    print("2: With it decrypt the line")
    print("Oabk tffbe://iii.kagfgnq.oay/imfot?h=gH7OpcVcjvY uzfa ftq mppdqee nmd ar kagd ndaieqd mzp tuf Qzfqd")
    print("3: Follow directions to get your reward!")
    print("\nNote that there may be a bug concerning copy & paste on the repl.it console. See readme.md for details.")
    app.ui.footer()
