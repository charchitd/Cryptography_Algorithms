from __future__ import print_function
 
sharedPrime = int(input("Enter Shared prime variablepublicly: "))  
sharedBase = int(input("Enter Shared base variable publicly: ")) 
aliceSecret = int(input("Enter Alice;s private message: "))     
bobSecret = int(input("Enter bob;s private message: "))     
 
print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime: " , sharedPrime )
print( "    Publicly Shared Base:  " , sharedBase )
 
# A = (g^a)modp
A = (sharedBase**aliceSecret) % sharedPrime
print( "\n  Alice Sends Over Public Chanel: " , A )
 
# B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print("Bob Sends Over Public Chanel: ",B )
 
print( "\n------------\n" )
print( "Privately Calculated Shared Secret:" )
# Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print( "    Alice Shared Secret: ", aliceSharedSecret )
 
# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = (A**bobSecret) % sharedPrime
print( "    Bob Shared Secret: ", bobSharedSecret )
