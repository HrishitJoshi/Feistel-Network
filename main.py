# Solution is 0b100110
left_m = [1,1,1]
right_m = [1,1,1]
key_1 = [1,0,1]
key_2 = [0,1,1]
def prf(x, key):
    arr = [0] *3
    arr[0] = x[0] & x[1] & key[0] & key[1]
    arr[1] = x[1] & x[2] & key[2] & key[0]
    arr[2] = (x[0]^x[1]) & key[0] & key[2]
    return arr

def feistel(left,right, key):
    temp = right
    right = (prf(right, key))
    for i in range(0,2,1):
        right[i] = right[i] ^ left[i]
    left = temp
    print(left,right)
    return left,right

left,right=feistel(left_m,right_m,key_1)
feistel(left,right,key_2)

# Here we have a helper function for PRF - that function replicates the logical equality for  PRF given in the Question
# Then we have variables declared as left_m, right_m, key_1, key_2. We also have the main function called Feistel.
# Feistel returns two values left and right. after the first iteration
# we have the output as 0b111100 and two more variables are declared.
# Those variables are used in the second iteration as input with key_2 to give the final result which is 0b100110

