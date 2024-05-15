# String partition example 
cad = "Hola, ¿cómo estás?"
part = cad.partition(",")
print(part)

# String partition from end example
cad = "www.ejemplo.com/documentos"
part = cad.rpartition("/")
print(part)

# Is identifier function example
cad1 = "variable1"
cad2 = "1variable"
print(cad1.isidentifier())  # Output: True
print(cad2.isidentifier())  # Output: False

# String decode and encode example
cadena = "Hola mundo"
cadena_codificada = cadena.encode("utf-8")
print(cadena_codificada)
cadena_decodificada = cadena_codificada.decode("utf-8")
print(cadena_decodificada)

# Printable verification example
cad1 = "Hola mundo"
cad2 = "Hola\nmundo"
print(cad1.isprintable())
print(cad2.isprintable()) 