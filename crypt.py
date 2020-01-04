import string, pyfiglet

welcome_txt = pyfiglet.figlet_format("%$__CRYPT__*&", font='doom')
print(welcome_txt)

print("\n"+85*"*"+"\n")
print("\n[01] Encrypter")
print("\n[02] Decrypter")
print("\n[03] Quit")

while True:
    while True:
        try:
            print("\n"+85*"*"+"\n")
            choice = int(input("\nEnter your choice: "))
            break
        except ValueError:
            print("\nOnly Integers Allowed!!!\n")

    alpha = " " + string.printable
    # print(alpha)
    if choice == 1 or choice ==0o1:
        print("\n"+85*"*"+"\n")
        while True:
            try:
                key = int(input("\nEnter a key [to be in range 35-51]: "))
                if key in range(35,51):
                    break
                else:
                    print("\nRange Limit Error!")
            except ValueError:
                print("\nOnly Integers Allowed!!!")

        print("\n"+85*"*"+"\n")
        msg = input("\nEnter your Message: ")
        msg = msg.strip()
        new_msg = ""

        for char in msg:
            """ Loop Through the msg variable
            and then using the alpha variable to find the chars 
            in msg. Appending those chars at different postn in the
            new_msg var (which is actually the encrypted msg)"""
            postn = alpha.find(char)
            new_posn = (postn+key)%94   # We can use any logic for the Encryption process.
            # print(new_posn)
            new_char=alpha[new_posn]   # These New chars are chosen from alpha variable
            new_msg+=new_char  # Appending those new_chars in the new_msg 

        print(f"\nYour Encrypted Message is '{new_msg}'")

    elif choice==2 or choice==0o2:
        print("\n"+85*"*"+"\n")
        while True:
            try:
                key = int(input("\nEnter your Key: "))
                if key in range(35,51):
                    break
                else:
                    print("\nRange Limit Error!")
            except ValueError:
                print("\nOnly Integers Allowed!!!")
            
        print("\n"+85*"*"+"\n")
        dmsg = input("Enter the Encrypted Message: ")
        decoded = ""

        for d_char in dmsg:
            """ Just Subtract the key from the position to decode the message"""
            d_postn = alpha.find(d_char)
            d_new_posn = (d_postn-key)%94
            # print(new_posn)
            d_new_char = alpha[d_new_posn]
            decoded+=d_new_char
            # decoded = decoded.strip()
        
        print(f"\nYour Decrypted Message is '{decoded}'")  # The special symbols would be displayed as normal alphabets :(
        print("\n"+85*"*"+"\n")
     
    elif choice==3 or choice==0o3:
        exit()
    else:
        print("\nNot an Option!!!\n")
