def c(n, k):
    
    if n == k or k == 0:
        print(str(n)+"C"+str(k), "=", 1)
        return 1
    else:
        print(str(n)+"C"+str(k), "=", str(n-1)+"C"+str(k-1), "+", str(n-1)+"C"+str(k))
        re = c(n-1, k-1) + c(n-1, k)
        print(str(n)+"C"+str(k), "=", re)
        return re
    

def main():
    a = int(input())
    b = int(input())
    c(a, b)
    
main()