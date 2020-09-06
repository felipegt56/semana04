def calendario(a,b,c,d,e,f):
  if c > f:
    return f'{a}/{b}/{c}'
  elif c == f:
    if b > e:
      return f'{a}/{b}/{c}'
    elif b < e:
      return f'{d}/{e}/{f}'
    else:
      if a > d:
        return f'{a}/{b}/{c}'
      elif a < d:
        return f'{d}/{e}/{f}'
      else:
        return f'{a}/{b}/{c}'
  else:
    return f'{d}/{e}/{f}'

def main():
  dia1 = int(input('Dia: '))
  mes1 = int(input('Mês: '))
  ano1 = int(input('Ano: '))
  dia2 = int(input('Dia: '))
  mes2 = int(input('Mês: '))
  ano2 = int(input('Ano: '))
  data = calendario(dia1, mes1, ano1, dia2, mes2, ano2)
  print(data)

if __name__== '__main__':
  main()
