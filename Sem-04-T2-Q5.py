def crecentes(a,b,c):
  num1 = a
  num2 = b
  num3 = c
  return num1, num2, num3
def main():
  n1 = int(input('1° Número: '))
  n2 = int(input('2° Número: '))
  n3 = int(input('3° Número: '))
  ordem = crecentes(n1, n2, n3)
  if n1 < n2 < n3:
    print(ordem[0])
    print(ordem[1])
    print(ordem[2])
  elif n1 < n3 < n2:
    print(ordem[0])
    print(ordem[2])
    print(ordem[1])
  elif n2 < n1 < n3:
    print(ordem[1])
    print(ordem[0])
    print(ordem[2])
  elif n2 < n3 < n1:
    print(ordem[1])
    print(ordem[2])
    print(ordem[0])
  elif n3 < n2 < n1:
    print(ordem[2])
    print(ordem[1])
    print(ordem[0])
  elif n3 < n1 < n2:
    print(ordem[2])
    print(ordem[0])
    print(ordem[1])
  else:
    print('Todos são iguais')


if __name__== '__main__':
  main()
