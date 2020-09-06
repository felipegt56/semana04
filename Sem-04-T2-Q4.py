def signos(dia, mes):
  if mes == 3:
    return 'Peixes' if dia < 21 else 'Áries'
  if mes == 4:
    return 'Áries' if dia < 20 else 'Touro'
  if mes == 5:
    return 'Touro' if dia < 21 else 'Gêmeos'
  if mes == 6:
    return 'Gêmeos' if dia < 22 else 'Câncer'
  if mes == 7:
    return 'Câncer' if dia < 23 else 'Leão'
  if mes == 8:
    return 'Leão' if dia < 23 else 'Virgem'
  if mes == 9:
    return 'Virgem' if dia < 23 else 'Libra'
  if mes == 10:
    return 'Libra' if dia < 23 else 'Escorpião'
  if mes == 11:
    return 'Escorpião' if dia < 22 else 'Sagitário'
  if mes == 12:
    return 'Sagitário' if dia < 22 else 'Capricórnio'
  if mes == 1:
    return 'Capricórnio' if dia < 20 else 'Aquário'
  if mes == 2:
    return 'Aquário' if dia < 19 else 'Peixes'
  

def main():
  d = int(input('Dia que você nasceu: '))
  m = int(input('mês que você nasceu: '))
  signo = signos(d, m)
  print(signo)

if __name__== '__main__':
  main()
