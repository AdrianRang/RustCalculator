# Calculator - Made in rust*, Adrian Rangel
#* rust, germany

expresion = input("Please enter your expresion ")

expresion = expresion.split(" ")

for i in range(1, len(expresion)):
  if expresion[i - 1] == "+":
    total += float(expresion[i])
  elif expresion[i - 1] == "-":
    total -= float(expresion[i])
  elif expresion[i - 1] == "*":
    total *= float(expresion[i])
  elif expresion[i - 1] == "/":
    total /= float(expresion[i])
  elif expresion[i - 1] == "%":
    total %= float(expresion[i])
    
print (total)
