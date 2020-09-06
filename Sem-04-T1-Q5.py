def indice_massa(p, a):
  imc = p / (a**2)
  return imc
def tabela(a):
  if a < 18.5:
    return 'Abaixo do peso'
  elif a >= 18.5 and a < 25:
    return 'Peso normal'
  elif a >= 25 and a < 30:
    return 'Sobrepeso'
  elif a >= 30 and a < 35:
    return 'Obeso leve'
  elif a >= 35 and a < 40:
    return 'Obeso moderado'
  else:
    return 'Obeso mórbido'

def main():
  peso = float(input('Qual é o seu peso? (Kg)'))
  altura = float(input('Qual é a sua altura? (m)'))
  imc = indice_massa(peso, altura)
  frase = tabela(imc)
  print(f'O IMC dessa pessoa é de {imc:.0f}')
  print(f'{frase}')
  
if __name__== '__main__':
  main()
