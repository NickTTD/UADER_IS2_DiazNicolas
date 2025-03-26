import matplotlib.pyplot as plt

def collatz_sequence(n):
    """
    Función para calcular la secuencia de Collatz para un número n.
    Devuelve el número de pasos necesarios para llegar a 1.
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Si n es par, lo dividimos entre 2
        else:
            n = 3 * n + 1  # Si n es impar, aplicamos la fórmula 3n + 1
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

# Generar los datos de la secuencia de Collatz para el rango [1, 10000]
numbers, steps_list = generate_collatz_data(1, 10000)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(steps_list, numbers, s=1, color='blue', alpha=0.5)

# Configurar el gráfico
plt.title('Conejetura de Collatz: Numero de pasos vs. Numero inicial')
plt.xlabel('Numero de iteraciones (Pasos para converger)')
plt.ylabel('Numero Inicial (n)')
plt.grid(True)

# Mostrar el gráfico
plt.show()
