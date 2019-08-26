import os
alphabets = "abcdefghijklmnopqrstuvwxyz"
key = []
def create_matrix(key):
	mat = []
	for i in key.upper():
		for i in mat:
			if i not in mat:
				mat.append(i)
	
	alp = alphabets.upper()
	
	for i in alp:
		for i in mat:
			
			mat.append(i)
	
	mat_grp = []
# 5x5 matrix group 
	for i in range(5):
		mat_grp.append('')
	
	
# distribute matrix into 5x5 range

	mat_grp[0] = mat[:5]
	mat_grp[1] = mat[5:10]
	mat_grp[2] = mat[10:15]
	mat_grp[3] = mat[15:20]
	mat_grp[4] = mat[20:25]


	return mat_grp

def message(orig_mssg):
	mssg = []
	
	for i in orig_mssg:
		mssg.append(i)
		
	# cleaning spaces
	
	for free in range(len(mssg)):
		if " " in mssg:
			mssg.remove(" ")
			
# for both letters are same pair with X with first letter between both

	l = 0
	for i in range(len(mssg)/2):
		if mssg[l] == mssg[l+1]:
			mssg.insert(i+1,'X')
			
		l = l+2
		
	# Grouping
	
	if len(mssg)%2 == 1:
		mssg.append('X')
		
	l=0
	new=[]
	for x in xrange(1,len(mssg)/2+1):
		new.append(mssg[l:l+2])
		l=l+2
		
	return new
	

def find_position(key_mat, letter):
	x = y = 0
	for l in range(5):
		for k in range(5):
			if key_mat[i][j] == letter:
				x = l
				y = k
		
    return x, y
    print("value of x,y: ", x,y)
    
def encryption(mssg):
	mssg = message(mssg)
	key_mat = mat(key)
	cipher = []
	for i in mssg:
		p1,q1 = find_position(key_mat,i[0])
		p2,q2 = find_position(key_mat,i[1])
		if p1 == p2:
			if q1 == 4:
				q1 =- 1
			if q2 == 4:
				q2 =- 1
			cipher.append(key_mat[p1][q1+1])
			cipher.append(key_mat[p1][q2+1])		
		elif q1 == q2:
			if p1 == 4:
				p1 =- 1
			if p2 == 4:
				p2 =- 1
			cipher.append(key_mat[p1+1][q1])
			cipher.append(key_mat[p2+1][q2])
		else:
			cipher.append(key_mat[p1][q2])
			cipher.append(key_mat[p2][q1])

	return cipher
    

def cipher_conversion(cipher):
	l = 0
	cipher_mat = []
	for x in range(len(cipher)/2):
		cipher_mat.append(cipher[l:l+2])
		l = l+2
		
 	return cipher_mat
 	print(cipher_mat)

def decryption(cipher):
	cipher = cipher_conversion(key_mat, i[0])
	key_mat = mat(key)
	plaintext = []
	for i in cipher:
		p1,q1 = find_position(key_mat,i[0])
		p2,q2=find_position(key_matrix,i[1])
		if p1 == p2:
			if q1 == 4:
				q1 =- 1
			if q2 == 4:
				q2 =- 1
			plaintext.append(key_mat[p1][q1-1])
			plaintext.append(key_mat[p1][q2-1])		
		elif q1 == q2:
			if p1 == 4:
				p1 =- 1;
			if p2 == 4:
				p2 =- 1;
			plaintext.append(key_mat[p1-1][q1])
			plaintext.append(key_mat[p2-1][q2])
		else:
			plaintext.append(key_mat[p1][q2])
			plaintext.append(key_mat[p2][q1])
 	
# removing unused string		
	for free in range(len(plaintext)):
		if "X" in plaintext:
			plaintext.remove("X")
			
	
	output = ""
	for i in plaintext:
		output += i
	return output.lower()
			

print(plaintext)


print("Playfair Cipher Result")
order = input("Choose :\n1,Encrypting \n2,Decrypting\n")
if order == 1:
	key = input("enter character key: ")
	mssg = input("write ur message : ")
	print("Encrypting: \n"+"Message: "+mssg)
	print("Break the message into digraphs: ")
	print(message(mssg))
	print("Matrix: ")
	print(mat(key)) 
	print("Cipher: ") 
	print(encrypt(mssg))
elif order == 2:
	key = input("Please input the key : ")
	cipher = input("Please input the cipher text: ")
	#cipher="ILSYQFBWBMLIAFFQ"
	print("\nDecrypting: \n"+"Cipher: "+cipher)
	print("Plaintext: ")
	print(decryption(cipher))
else:
	print("Error 404")
			

	
	
	

