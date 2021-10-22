
class CaesarShift:
    """Core functions of the Caesar Cipher."""

    def __init__(self, cryptokey=3):
        self.cryptokey = cryptokey


    def encrypt(self, message):
        """
        Encrypt a message.

        Parameters:
        message (str): message to encrypt

        Returns:
        str: encrypted message
        """
        self.cryptokey = -abs(self.cryptokey)
        # key negative: Shift down to encode
        return self.shift_message(message)


    def decrypt(self, message):
        """
        Decrypt a message.

        Parameters:
        message (str): encrypted message to decrypt

        Returns:
        str: decrypted message
        """
        self.cryptokey = abs(self.cryptokey)
        # key positive: Shift up to decode
        return self.shift_message(message)


    def brute_force_decrypt(self, message):
        """
        Show the first 25 possible shiftings.

        One of them must be correct
        and it can't be #26:
        26 % 26 == 0 ergo input == output
        
        Parameters:
        message (str): message to decrypt

        Returns:
        list: list of strings containing all shiftings
        """
        shiftings = list()
        for ck in range(1, 26):
            self.cryptokey = ck
            shiftings.append(self.decrypt(message))
            
        return shiftings


    def shift_message(self, message):
        """
        Shift every character of a message.

        Parameters:
        message (str): message to process

        Returns:
        str: message with shifted letters
        """
        message_out = ""
        for character in message:
            message_out += self.shift_letter(character)
        return message_out


    def shift_letter(self, letter):
        """
        Shift a single letter.
        
        Characters other than letters are ignored.
        
        Parameters:
        letter (str): len(letter) == 1  # a single character

        Returns:
        str: a single character, shifted if it's a letter
        """
        if letter.isalpha():
            # distinguish upper and lower case letters,
            # consider that ascii codes of "a" and "A" are not 0
            if letter.islower():
                chr_offset = 97
            else:
                chr_offset = 65

            ascii_in = ord(letter) - chr_offset
            ascii_out = (ascii_in + self.cryptokey) % 26 + chr_offset
            
            shifted_letter = chr(ascii_out)

        elif letter.isprintable():
            # whitespace, numbers, punctuation, ...
            shifted_letter = letter
        else:
            # non-printables
            shifted_letter = " "

        return shifted_letter 
