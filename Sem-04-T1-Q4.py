def media_cinco(a,b,c,d,e):
  media = (a + b + c + d + e) / 5
  return media

def main():
 num1 = int(input('Digite o 1° número: '))
 num2 = int(input('Digite o 2° número: '))
 num3 = int(input('Digite o 3° número: '))
 num4 = int(input('Digite o 4° número: '))
 num5 = int(input('Digite o 5° número: '))
 media = media_cinco(num1, num2, num3, num4, num5)
 print(f'A média é {media:0.2f}')
 if num1 > media:
   print(f'O número {num1:0.2f} é maior que a média')
 if num2 > media:
   print(f'O número {num2:0.2f} é maior que a média')
 if num3 > media:
   print(f'O número {num3:0.2f} é maior que a média')
 if num4 > media:
   print(f'O número {num4:0.2f} é maior que a média')
 if num5 > media:
   print(f'O número {num5:0.2f} é maior que a média')

if __name__== '__main__':
  main()
  
