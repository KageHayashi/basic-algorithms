### Returns the first N terms of the fibonacci sequence
def fibonacciNumbers(n):
    fibonacci_num = [1, 2]
    for i in range(n + 1):
        fibonacci_num.append(fibonacci_num[i] + fibonacci_num[i+1])
    return fibonacci_num

### Returns the first N terms of the even fibonacci numbers
def evenFibonacciNumbers(n):
    if n < 2:
        return(0)
    
    even_fibonacci_num = [2]

    ef1 = 0
    ef2 = 2

    while ef2 <= n:
        ef3 = 4 * ef2 + ef1

        if ef3 > n:
            break

        # update to next even values and update list
        ef1 = ef2
        ef2 = ef3
        even_fibonacci_num.append(ef2)
    return even_fibonacci_num


