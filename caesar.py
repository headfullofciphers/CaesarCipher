import string
import base64

alphabet = string.ascii_lowercase

def shift_cipher(text, shift, mode):
    plain = text.lower()
    shift %= len(alphabet)
    ciphertext = ''
    
    for letter in plain:
        position = alphabet.find(letter)
        
        if position == -1:
            ciphertext += letter
            continue
        
        if mode == 'enc':
            ciphertext += alphabet[(position+shift)%len(alphabet)]
        elif mode == 'dec':
            ciphertext += alphabet[(position-shift)%len(alphabet)]
             
    return ciphertext 

egg = 'L2d1ci9xcmlmL25lci9mYi9zaGFhbC9ndX\
JsL3V2cS9uYS9ybmZncmUvcnR0L2p2Z3V2YS9ndXIvcm5mZ3JlL3J0dA==' #step1
egg_decoded = base64.b64decode(egg) #step 2
egg_decoded = egg_decoded.decode("utf-8") #step 3
print(f'step 1 - egg = {egg}')
print(f'step 2+3 - egg base64 decoded = {egg_decoded}')

for i in range(1,26):#step4
    print(f'#{i} - {shift_cipher(egg_decoded,i,"dec")}')