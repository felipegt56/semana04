def maior_valor(a,b,c,d,e):
  if a > b and a > c and a > d and a > e:
    maior = a
  if b > a and b > c and b > d and b > e:
    maior = b
  if c > a and c > b and c > d and c > e:
    maior = c
  if d > a and d > b and d > c and d > e:
    maior = d
  if e > a and e > b and e > c and e > d:
    maior = e
  return maior
def menor_valor(a,b,c,d,e):
  if a < b and a < c and a < d and a < e:
    menor = a
  if b < a and b < c and b < d and b < e:
    menor = b
  if c < a and c < b and c < d and c < e:
    menor = c
  if d < a and d < b and d < c and d < e:
    menor = d
  if e < a and e < b and e < c and e < d:
    menor = e
  return menor

def main():
 num1 = int(input('Digite o 1° número: '))
 num2 = int(input('Digite o 2° número: '))
 num3 = int(input('Digite o 3° número: '))
 num4 = int(input('Digite o 4° número: '))
 num5 = int(input('Digite o 5° número: '))
 maior = maior_valor(num1, num2, num3, num4, num5)
 menor = menor_valor(num1, num2, num3, num4, num5)
 print(f'O maior valor digitado foi {maior}')
 print(f'O menor valor digitado foi {menor}')

if __name__== '__main__':
  main()
  
