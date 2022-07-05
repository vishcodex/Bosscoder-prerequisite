
def sum_digits():
    print("Enter a number:")
    n = int(input())
    sum_val = 0
    m = 0      
    while n != 0:
        m=n%10   
        sum_val += m  
        n=n//10        
    return sum_val 

a = sum_digits()

print(a)