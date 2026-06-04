import time
import tracemalloc

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def recursiva_collatz(n):
    print( n , end="")
    if n == 1:
        return
    else:
        print(" -> ", end="")
        return recursiva_collatz(collatz(n))

def simular_collatz(n):
    for i in range(2, n+1):
        recursiva_collatz(i)
        print()

def benchmark_collatz(n, repeticiones=10):
    tiempos = []
    picos_memoria = []

    for _ in range(repeticiones):
        tracemalloc.start()
        inicio_tiempo = time.perf_counter()

        simular_collatz(n)

        fin_tiempo = time.perf_counter()
        _, pico_ram = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        tiempos.append((fin_tiempo - inicio_tiempo)*1000)
        picos_memoria.append(pico_ram / (1024*1024))

    tiempo_promedio = sum(tiempos) / repeticiones
    ram_promedio = sum(picos_memoria) / repeticiones

    # Salida en formato plano texturizado
    print(f"Lenguaje: Python")
    print(f"Tamaño (n): {n}")
    print(f"Tiempo Promedio: {tiempo_promedio:.6f} milisegundos")
    print(f"RAM Promedio (Pico): {ram_promedio:.6f} MB\n")

if __name__ == "__main__":
    benchmark_collatz(n=50000)
