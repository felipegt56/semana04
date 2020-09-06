def main():
  cont = 0
  n = int(input('Digite um número entre 100 e 999: '))
  if n >= 100 and n <= 999:
      c = n // 100
      r_c = n % 100
      d = r_c // 10
      r_d = n % 10
      u = r_d // 1
      if c % 2 == 0:
        cont += 1
      if d % 2 == 0:
        cont += 1
      if u % 2 == 0:
        cont += 1
      soma = cont
      print(f'Tem {soma} digito pare(s)')
if __name__== '__main__':
  main()
