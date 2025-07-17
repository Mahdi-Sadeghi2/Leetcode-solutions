# Time complexity O(n) | Space complexity O(n)
def fibo(n):
    if n <= 0:
        return n
    # Initialize firs two Fibonacci numbers
    fib = [0, 1]
    # Generate subsequent numbers form F2 to Fn
    for i in range(2, n+1):
        # Each Fibonacci number is the sum of the two preceding ones
        next_num = fib[i-1] + fib[i-2]
        fib.append(next_num)
    return fib[-1] 
