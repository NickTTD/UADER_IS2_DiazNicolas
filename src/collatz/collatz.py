import matplotlib.pyplot as plt

def collatz_sequence(n):
    """
    Función para calcular la secuencia de Collatz para un número n.
    Devuelve el número de pasos necesarios para llegar a 1.
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Si n es par, dividir entre 2
        else:
            n = 3 * n + 1  # Si n es impar, aplicar la fórmula 3n + 1
        steps += 1
    return steps

def generate_collatz_data(start, end):
    """
    Genera los datos de los números de inicio y sus pasos de Collatz.
    """
    numbers = []
    steps_list = []
    
    for number in range(start, end + 1):
        steps = collatz_sequence(number)
        numbers.append(number)
        steps_list.append(steps)
    
    return numbers, steps_list

# Solicitar al usuario el rango de números (inicio y fin)
start = int(input("Introduce el número de inicio para la secuencia de Collatz: "))
end = int(input("Introduce el número final para la secuencia de Collatz: "))

# Generar los datos de Collatz para el rango dado
numbers, steps_list = generate_collatz_data(start, end)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(steps_list, numbers, s=1, color='blue', alpha=0.5)

# Configurar el gráfico
plt.title('Conjetura de Collatz: Número de Pasos vs. Número Inicial')
plt.xlabel('Número de Iteraciones (Pasos para Convergencia)')
plt.ylabel('Número Inicial (n)')
plt.grid(True)

# Mostrar el gráfico
plt.show()
