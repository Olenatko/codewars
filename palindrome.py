def check_prime_number(N):
    if N < 1:
        return False
    if N == 2 or N == 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    for x in range(3, int(N**0.5)+1, 2):
        if N % x == 0:
            return False
    return True

N = 0
while N < 1000:
    if str(N) == str(N)[::-1] and check_prime_number(N):
        print N
    N += 1

