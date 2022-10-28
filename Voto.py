def voto(ano):
   import datetime
   a=datetime.datetime.today().year
   idade=a-ano
   if idade<16:
       return f" com {idade} ANOS NÃO VOTA"
   elif 16<=idade <18 or idade>65:
       return f"com {idade} ANOS VOTO OPCIONAL"
   else:
       return f"com {idade} ANOS VOTO OBRIGATÓRIO"


i=int(input("em que ano você nasceu?"))
print(voto(i))





