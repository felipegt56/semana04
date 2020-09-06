def data(a, b, c, d, e):
  if b >= d :
    if b == d:
      if a >= c:
        idade = e
      else:
        idade = e - 1
    elif b > d:
      idade = e
  else:
    idade = e - 1
  return idade

def main():
  dia1 = int(input('Digite o dia atual: '))
  mes1 = int(input('Digite o mês atual: '))
  anos = int(input('Digite o ano atual: '))
  dia2 = int(input('Digite o dia que você nasceu: '))
  mes2 = int(input('Digite o mês que você nasceu: '))
  ano = int(input('Digite o ano que você nasceu: '))
  calculo = anos - ano
  variavel = data(dia1, mes1, dia2, mes2, calculo)
  print(f'Você tem {variavel} anos')

if __name__== '__main__':
  main()

