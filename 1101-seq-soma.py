M, N  = map(int, input().split())

soma = 0

if M != 0 and N != 0:
    while M >= N:
        soma = N + soma
        print(f"{N} ",end="")
        N = N + 1
    print(f"Sum={soma}")