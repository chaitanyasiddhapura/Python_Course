# 1. String and Numeric value can operate together with '*'and
A1,B1 = 2, 3
txt1 = "$"
print("Output 1 ->")
# Evaluate = 2 * 3 = 6 ->  $ * 6 = $$$$$$
print(2 * txt1 * 3) 

# 2. String & String can operate with +
A2,B2 = "2", 3
txt2 = "$"
# One string can be connected with another string using the '+' operator it is called concatenation.
print("Output 2 ->")
# Evaluate = "2" + "$" = "2$" ->  "2$" * 3 = 2$2$2$
print((A2 + txt2 ) * B2)

# 3. Numeric value can operate with all arithmetic operators
A3, B3 = 2, 3
C3 = 4
print("Output 3 -> ")
print(A3 + B3 * C3)

# 4. Arithmetic expression with integer and float will result in float 
A4, B4 = 10, 5.0
C4 = A4 * B4 
print("Output 4 -> ")
print(C4)

# 5. Result of division operator with two integers will be float 
A5, B5 = 1, 2
print("Output 5 -> ")
print(A5 / B5)


# 6. Integer division with float and int will give int display as float 
A6, B6 = 1.5, 3
#Evaluate 1/10 = 0.1. However, the result is always an integer, so it is 0. But display the result as a floating-point number, so the final result is 0.0.  
C6 = A6 // B6
print("Output 6 -> ")
print(C6)

# 7. About Floor Function
# floor give closest integer which is lesser than or equal to the float value result of (A//B) is smae as floor(A/B)
# case 1
A71, B71 = 12, 5
C71 = A71 // B71
print("Output 7")
print("case: 1 -> ")
print(C71)

#case 2
A72, B72 = -12, 5
C72 = A72 // B72
print("case: 2 -> ")
print(C72)

# 8. Remainder is Negative  when denominator is Negative  
# for example 5/-2 in that case return '-' Negative  value 

# case 1
A81, B81 = -5, 2
C81 = A81 % B81
print("Output 8")
print("case: 1 -> ")
print(C81)

# case 2
A82, B82 = 5, 2
C82 = A82 % B82
print("case: 2 -> ")
print(C82)

# case 3
A83, B83 = 5, -2
C83 = A83 % B83
print("case: 3 -> ")
print(C83)
