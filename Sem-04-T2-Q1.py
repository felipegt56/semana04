def main():
  nome = str(input('Qual é o seu nome: '))
  relacao = int(input('estado civil 1 casado, 2 solteiro:  '))
  if relacao == 1:
    conjuge = str(input('nome do cônjuge: '))
    print(f'{len(nome) + len(conjuge)} caracteres no total')
  elif relacao == 2:
    print(f'{len(nome)} caracteres no total')
if __name__== '__main__':
  main()
