def fibonacci(n: int) -> int:
    if n < 2: return n
    def mult(A,B):
        return (A[0]*B[0] + A[1]*B[2],
                A[0]*B[1] + A[1]*B[3],
                A[2]*B[0] + A[3]*B[2],
                A[2]*B[1] + A[3]*B[3])
    def power(M,p):
        if p == 1: return M
        X = power (M, p // 2)
        X = mult(X,X)
        return X if p % 2 == 0 else mult(M,X)
    return power((1, 1, 1, 0), n)[1]


if __name__== '__main__':
    print([fibonacci(i) for i in range(15)])