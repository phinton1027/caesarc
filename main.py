from caesarshift import CaesarShift
import app
import demo
import test


cs = CaesarShift()
ui = app.ui(cs)

while True:
    ui.header()
    print("Encrypt a message     1")
    print("Decrypt a message     2")
    print("Brute Force Decrypt   3")
    print("Demo                  4")
    print("Test                  5")
    print("Quit                  0")

    try:
        order = int(input("      Execute Order # "))
    except ValueError:
        print("Numbers between 0 and 5 only. Try again")
        ui.footer()
        continue

    if order == 1:
        ui.input_encrypt()
    elif order == 2:
        ui.input_decrypt()
    elif order == 3:
        ui.input_brute_force()
    elif order == 4:
        demo.demo()
    elif order == 5:
        test.test()
    elif order == 0:
        ui.quit()
        break
    









































    elif order == 66:
        demo.order66()
    else:
        print("Numbers between 0 and 5 only. Try again")
        ui.footer()
