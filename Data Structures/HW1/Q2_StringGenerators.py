"""
Assignment 1 question 2 String Generator

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""
import copy


def string_generator():
    """
    :return: an iterator that would yield all possible strings formed by
             using the characters ‘c’ , ‘a’ , ‘t’ , ‘d’ , ‘o’ , and ‘g’ exactly once.
    """
    # To do
    res=['c']
    source=['a','t','d','o','g']
    for depth in range(5):
        k=len(res)
        for i in range(k):
            pre= res.pop(0)
            for idx in range(len(pre)+1):
                new=pre[:idx]+source[depth]+pre[idx:]
                res.append(new)
    return iter(res)
        
            
            
            
                
                
            
            
            
            
    


def main():
    catdog_it = string_generator()
    print(next(catdog_it))  # Expect: a permutation of 'catdog'
    for i in range(719):
        next(catdog_it)     # should br executed without an error

    # next(catdog_it)        # Should raise a StopIteration error

    catdog_it = string_generator()
    L = list(catdog_it)
    print('tadcgo' in L)    # Expect: True
    print(len(L))           # Expect: 720


# if __name__ == '__main__':
#     main()
