def par(n):
  return n % 2 == 0
def impar(n):
  return n % 2 != 0
def condicoes(a, b):
  if par(a) and par(b):
    return 'Nenhum dígito é ímpar.'
  elif par(a) and impar(b) or impar(a) and par(b):
    return 'Apenas um dígito é ímpar.'
  elif impar(a) and impar(b):
    return 'Os dois dígitos são ímpares.'

def main():
  cont = 0
  n = int(input('Digite um número entre 10 e 99: '))
  if n >= 10 and n <= 99:
    d = n // 10
    r_d = n % 10
    u = r_d // 1
    texto = condicoes(d, u)
    print(texto)


if __name__== '__main__':
  main()
