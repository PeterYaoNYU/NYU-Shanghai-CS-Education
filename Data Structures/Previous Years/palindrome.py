'''
Problem 3
Palindrome (Recursive version)
Implement function palindrome( ): this function assesses whether an input String is
indeed a palindrome.
Important:
• Check the string letter by letter, no string.reverse( )
• Use recursion to break large problem into smaller problem.
'''

'''
 # Complete the palindrome algorithm --- with recursion
    # Think about how to break a large problem into smaller sub problems.
    What is our base case in this problem?

    # Another way to ask: what is our smallest problem?
    How to get to this smallest problem?

    :param string: String -- the string to check whether it is a palindrome
    :param index: Int -- additional parameter for recursion tracking

    :return: True if @string is palindrome, False otherwise
    """
'''
def palindrome_recursive(s, num=0):
    if len(s)==0 or len(s)==1:
        # this is important: you cannot write len(s)==0 or 1:
        # otherwise it will always return True
        return True
    n=len(s)
    return s[0]==s[n-1] and palindrome_recursive(s[1:n-1], num+1)

def main():
    s1 = "nodevillivedon"
    s2 = "livenoevil!liveonevil"
    s3 = "beliveivileb"
    r1 = palindrome_recursive(s1, 0)
    r2 = palindrome_recursive(s2, 0)
    r3 = palindrome_recursive(s3, 0)
    print("s1 is", r1)  # Should be True
    print("s2 is", r2)  # Should be True
    print("s3 is", r3)  # Should be False

main()