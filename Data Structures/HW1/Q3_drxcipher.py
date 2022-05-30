"""
Assignment 1 question 3 Dr X Cipher

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""


def encryptX(plain, key):
    """
    :param plain: String -- a python input string. The plain text.
    :param key: String -- a python input string. The key.

    :return: String -- the cipher python string text.
    """
    # To do
    n=len(key)
    try:
        supple=list(plain[:n])
        supple.reverse()
        supple=''.join(supple)
    except:
        pass
    while len(key)<len(plain):
        key+=supple
    key=key[:len(plain)]
    # print(key)
    n=len(plain)
    lissy=list(plain)
    for i in range(n):
        if ord(lissy[i])+(ord(key[i]))-65<91:
            lissy[i]=chr(ord(lissy[i])+(ord(key[i]))-65)
        else:
            lissy[i]=chr(ord(lissy[i])+(ord(key[i]))-91)
    return ''.join(lissy)
        
        


def decryptX(cipher, key):
    '''
    :param cipher: String -- a python input string. The cipher text.
    :param key: String -- a python input string. The key.

    :return: String -- the plain python string text.
    '''
    # To do
    n=len(key)
    if n<len(cipher):
        top=[]
        for i in range(n):
            k=chr(ord(cipher[i])+65-ord(key[i]))
            # print(k)
            if not 'A'<=k<='Z':
                k=chr(ord(k)+26)
            top.append(k)
        top.reverse()
        top=''.join(top)
        # print(top)
        m=len(cipher)
        while len(key)<m:
            key+=top
        key=key[:m]
        # print(key)
    key=list(key)
    n=len(cipher)
    res=[]
    for i in range(n):
        k=chr(ord(cipher[i])+65-ord(key[i]))
            # print(k)
        if not 'A'<=k<='Z':
            k=chr(ord(k)+26)
        res.append(k)
    return ''.join(res)
            
        
    
            


def main():
    print(encryptX("ATTACKATDAWN", "QUE"))  # QNXTVKTMDTPN

    print(encryptX("DATASTRUCTURE", "NYUSH"))   # QYNSZLRNCWMRX

    print( encryptX("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLJJJJJOOOOOTTTTTYYYYYD

    print( encryptX("CUTE", "NYUSH"))  # PSNW

    print(decryptX("QNXTVKTMDTPN", "QUE"))   # ATTACKATDAWN
    print( decryptX("QYNSZLRNCWMRX", "NYUSH"))   # DATASTRUCTURE
    print( decryptX("NZWVLJJJJJOOOOOTTTTTYYYYYD", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print( decryptX("PSNW", "NYUSH"))  # CUTE


# if __name__ == '__main__':
#     main()
