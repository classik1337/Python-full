a=int(input())

def reverse (a):
    b=list(str(a))                      
    c=len(b)                            
    a=int(c/2)                          
    if c % 2 == 0:                      
        one_b=(b[:a])                   
        two_b=(b[a:])                   
        one_rev=list(reversed(one_b))   
        two_rev=list(reversed(two_b))   
        sum_b=one_rev + two_rev         
        sss=' '.join(map(str, sum_b))   
        print(sss)
    else:
        min_b=min(b)                    
        b.remove(min_b)                 
        one_b=(b[:a])                   
        two_b=(b[a:])
        one_revv=list(reversed(one_b))
        two_revv=list(reversed(two_b))
        sum_b=one_revv + two_revv 
        sss=' '.join(map(str, sum_b))
        print(sss, min_b)               
reverse(a)
        


    