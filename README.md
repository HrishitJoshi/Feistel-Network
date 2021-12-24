# Feistel-Network-
2 round Feistel network Implementation 


Consider a two-round Feistel network. Assume that the block length is 6-bit. Thus, each block is divided into two 3-bit sub-blocks.

Let the message M= 111 111 (in binary),

the key of round 1 is k1 = (1, 0, 1),

the key of round 2 is k2 = (0, 1, 1).

The PRF function f(x , y) is defined below. Note that x and y are both 3-bit numbers. f returns a 3-bit output.

"^" denotes the XOR.

f(x, y)= f(x0, x1, x2; y0, y1, y2) = (x0x1y0y1,  x1x2y2y0,  (x0 ^ x1)y0y2)

 Find ciphertext of the above input message M?
 
 Feel free to use any values you may choose.
