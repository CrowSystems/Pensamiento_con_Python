def fibonnacci(n):
    if n == 0 or n == 1:
        return 1
    #print(n)
    return fibonnacci(n-1) + fibonnacci(n-2)
n = int(input('Escribe un numero entero: '))
print(f'El número fibonnaci para {n} es {fibonnacci(n)}')