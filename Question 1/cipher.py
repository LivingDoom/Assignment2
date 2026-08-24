"""
Assignment 2

Cipher.py

Group Name: [DAN/EXT12] 
Group Members: 
[Kayla Edwards]                 -           [S396018] 
[Jonathan William McPhail]      -           [S368879] 
[Ibrahim Najjarine]             -           [S407912] 
[Glen Mark Pasigna]             -           [S328808] 


"""


lower_a_n = [chr(c) for c in range(97, 111)]
lower_o_z = [chr(c) for c in range(111, 123)]
capital_AtoM = [chr(c) for c in range(65,78)]
capital_NtoZ = [chr(c) for c in range(78,91)]

#--------------------------------------------------------------------------------------------------------------
# Function to read files and return the text for further processing.
#--------------------------------------------------------------------------------------------------------------

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

#--------------------------------------------------------------------------------------------------------------
# Function to write files to same directory as script. Will print the name of the file being saved.
#--------------------------------------------------------------------------------------------------------------

def write_file(location, out):
    with open(location, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'File saved as: {location}') # Ask if we can keep here for submission or 'have to'/'should' remove before submission. 

#--------------------------------------------------------------------------------------------------------------
# Encryption Function: 
# Takes in 4 parameters, two positive intergers from the user, a text file to encrypt, and an output path to the encrypted file.
# Both input and output paths have a default paths incase no file name entered during function execution.
#--------------------------------------------------------------------------------------------------------------

def encrypt_file(shift1: int, shift2: int, input_path: str = 'raw_text.txt' , output_path: str = 'encrypted_text.txt') -> None:
    output = [] 
    for i in input_path:

        if i.islower():
            if i in lower_a_n:
                offset = 97
                output.append(chr((ord(i) - offset + (shift1 * shift2))%14 + offset))
            elif i in lower_o_z:
                offset = 111
                output.append(chr((ord(i) - offset - (shift1 + shift2))%12 + offset))

        elif i.isupper():
            if i in capital_AtoM:
                offset = 65
                output.append(chr((ord(i) - offset - (shift1))%13 + offset))
            elif i in capital_NtoZ:
                offset = 78
                output.append(chr((ord(i) - offset + (shift2**2))%13 + offset))

        elif i.isdigit():
            output.append(str((int(i)-(shift1 - shift2))%10))

        else:
            output.append(i)
    write_file(output_path, ''.join(output))
    
#--------------------------------------------------------------------------------------------------------------
# Decrytion Function:
# Reverses the encryption applied above.
# Takes 4 inputs, two positive intergers from the user, a text file to decrypt, and an output path to the decrypted file.
# Both input and output paths have a default paths incase no file name entered during function execution.
#--------------------------------------------------------------------------------------------------------------

def decrypt_file(shift1: int, shift2: int, input_path: str = 'encrypted_text.txt', output_path: str = 'decrypted_text.txt') -> None:
    output = [] 
    for i in input_path:
        if i.islower():
            offset = 97
            if i in lower_a_n:
                output.append(chr((ord(i) - offset - (shift1 * shift2))%14 + offset))

            elif i in lower_o_z:
                offset = 111
                output.append(chr((ord(i) - offset + (shift1 + shift2))%12 + offset))

        elif i.isupper():
            if i in capital_AtoM:
                offset = 65
                output.append(chr((ord(i) - offset + (shift1))%13 + offset))
            elif i in capital_NtoZ:
                offset = 78
                output.append(chr((ord(i) - offset - (shift2**2))%13 + offset))
        elif i.isdigit():
            output.append(str((int(i)+(shift1 - shift2))%10))
        else:
            output.append(i)
    write_file(output_path, ''.join(output))
    # pass


#--------------------------------------------------------------------------------------------------------------
# Verification Function:
# Compares the original input_text.txt file against the decrypted_text.txt file.
# Will print success or failure message to user.
#--------------------------------------------------------------------------------------------------------------

def verify_files(original_path: str, decrypted_path: str,) -> bool:
    original = read_file(original_path)
    decrypted = read_file(decrypted_path)
    
    if original == decrypted:
        print( 'Files have been decrypted sucessfully' )
    else:
        print( 'File have NOT been decrypted successfully!!!' ) 

#--------------------------------------------------------------------------------------------------------------
# Input Section:
# Checks input for positive numbers, will stay in the loop until two integers have been entered.
#--------------------------------------------------------------------------------------------------------------

while True:
    try:
        input_shift1 = int(input("Please enter the 1st shift: "))
        if input_shift1 < 0:
            print("Please enter a positive interger")
            continue

        input_shift2 = int(input("Please enter the 2nd shift: "))
        if input_shift2 < 0:
            print("Please enter a positive interger")
            continue
        break

    except:
        print( 'Please enter "Positive Integers" only' )


encrypt_file(input_shift1, input_shift2, read_file('raw_text.txt'),)
decrypt_file(input_shift1, input_shift2, read_file('encrypted_text.txt'),)
verify_files('raw_text.txt', 'decrypted_text.txt')

# for testing purposes, remove before submission.
# encrypt_file(3, 4, read_file('night_sky.txt'))
# decrypt_file(3, 4, read_file('encrypted_text.txt'))
# verify_files('night_sky.txt', 'decrypted_text.txt')
