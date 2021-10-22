# Caesar Pypher
This is the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) encryption implemented in Python.
# Motivation
I did this before in JS to help a friend. Now took it to Python and poshed it up a bit to give beginners easy examples of how to
- import own modules
- define, init and use own classes
- implement a very basic menu

and whatever you may find useful.
# Usage
From Wikipedia: [...] _each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet_ [...]
This fixed number is what I call cryptokey in both interface and code.

Applying the Caesar Cipher with pen & paper entails different signs of the cryptokey for encoding and decoding.
This program avoids confusion. You use the same number for both.
By the way: If you were allowed to enter a number `-26 < n < 0` it would yield `n modulo 26 = 26 - n`.
## User
Menu and functions are somewhat self explanatory and answer bad input with a hint.

The entry of the cryptokey is kept secret. It shows no output.

Brute force mode lists 25 of 26 possible shiftings, excluding of course the one that was fed in. It's up to the user to decide which one is correct.
The output lines are numbered. The line number with legit text is the cryptokey used for encryption.
### Warning
An encrypted message can only be decrypted with the proper cryptokey. Otherwise no information will be accessible.
## Developer
(This chapter needs completion, but the code has a bit of documentation.)
Example
```
from caesarshift import CaesarShift
import app
cs = CaesarShift(cryptokey=13)
ui = app.ui(cs)
ui.input_encrypt()  # Front end for cs.encrypt()
ui.input_decrypt()  # Front end for cs.decrypt()
ui.input_brute_force()  # Front end for cs.brute_force_decrypt()
```
## class caesarshift.CaesarShift()
Core functions for encoding and decoding.
## class app.ui()
Ensure valid user input, unify header / footer, call core functions and display the results.
# Known bug
At one point I pasted a longer message. The soft line break was considered a regular one and messed up the output.
Unfortunately I am not able to reproduce this behavior.
In the settings I switched "Wrapping" from <soft> to <none> and back. Perhaps that did the trick.
# Changelog
2020/03/31
- switch direction of letter shifting to match with description at Wikipedia
- split ui and logic into separate modules
- split demo and test into separate modules
- add brute force decryption (including demo and test)
- minor improvements of the interface
- add some docstrings
- add this changelog
