import getpass
import replit


class ui:
    """
    Handle user interaction.
    
    Ensure valid user input, unify header / footer,
    call core functions and format their results.
    """

    def __init__(self, caesarshift):
        """Connect to core functions."""
        self.cs = caesarshift


    def input_encrypt(self):
        """
        Encrypt user input.

        Enquire cryptokey and message,
        call encrypt method,
        show encrypted message.
        """
        self.header()
        print("Encrypting")

        self.cs.cryptokey = self.input_cryptokey()
        if not self.cs.cryptokey:
            print("\nCancelled")
            self.footer()
            return

        message_in = input("\nMessage:   ")
        message_out = self.cs.encrypt(message_in)
        print("\nEncrypted:", message_out)
        self.footer()


    def input_decrypt(self):
        """
        Decrypt user input.

        Enquire cryptokey and encrypted message,
        call decrypt method,
        show decrypted message.
        """
        self.header()
        print("Decrypting")

        self.cs.cryptokey = self.input_cryptokey()
        if not self.cs.cryptokey:
            print("\nCancelled")
            self.footer()
            return

        message_in = input("\nMessage:   ")
        message_out = self.cs.decrypt(message_in)
        print("\nDecrypted:", message_out)
        self.footer()


    def input_brute_force(self):
        """Show numbered list of all possible shiftings."""
        self.header()
        print("Brute Force Decrypting")

        message_in = input("\nEncrypted Message: ")
        
        shiftings = self.cs.brute_force_decrypt(message_in)
        for i, shifted in enumerate(shiftings):
            print("{:2}: {}".format(i+1, shifted))
        
        print("\nThe number of the line with legit text")
        print("is the cryptokey used for encryption.")
        self.footer()


    def input_cryptokey(self):
        print("\nCryptokey between 1 and 26 (0 to cancel).")
        print("Note that this entry shows no output on screen.")

        return self.get_int(
            "Your secret Cryptokey: ",
            min=0, max=26,
            secret = True
        )


    @staticmethod
    def header():
        replit.clear()
        print("CAESAR CIPHER\n")


    @staticmethod
    def get_int(msg, min, max, secret=False):
        """
        Acquire integer safely.

        Repeat until input is valid.

        Parameters:
        msg (str): A message to show before input
        min (int): Minimum number allowed
        max (int): Maximum number allowed
        secret (bool): Hide input if True
                       Defaults to False
        Returns:
        int: min <= number <= max
        """
        while True:
            if secret:
                num = getpass.getpass(msg)
            else:
                num = input(msg)

            try:
                num = int(num)
            except ValueError:
                pass
            else:
                if min <= num <= max:
                    break
            
            print(f"Numbers between {min} and {max} only. Try again")

        return num


    @staticmethod
    def footer():
        input("\nENTER to continue")


    @staticmethod
    def quit():
        print("\nkeep fit and well\n")
