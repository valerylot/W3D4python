str1 = "Y(3(p)p(3)r)s"
expected1 = True

str2 = "N(0(p)3"
expected2 = False
# // Explanation: not every parenthesis is closed.


str3 = "N(0)t ) 0(k"
expected3 = False
# // Explanation: because the second ")" is premature: there is nothing open for it to close.

str4 = "a(b))(c"
expected4 = False
# // Explanation: same number of opens and closes but the 2nd closing closes nothing.

str5 = "(y)l(jjkjk)jjkfjd)"

str6 = "()hg(hj:),.(kj)"

def parens_valid(str):
    split_str = str.split()
    # return split_str
    count1 = 0
    count2 = 0
    for i in range (0, len(split_str)):
        if split_str[i] == '(':
            count1+=1


print(parens_valid(str1))
print(parens_valid(str2))
print(parens_valid(str3))
print(parens_valid(str4))