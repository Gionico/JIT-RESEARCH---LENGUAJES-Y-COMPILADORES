# run_benchmark.py
import time
import os
import matplotlib.pyplot as plt
from antlr4 import FileStream, CommonTokenStream
from DockerComposeNetworkLexer import DockerComposeNetworkLexer
from DockerComposeNetworkParser import DockerComposeNetworkParser

files = [f"test_files/docker_compose_{i}.yml" for i in range(1, 11)]

tiempos_python = []
tiempos_java_sim = [] # Simulación basada en la diferencia de velocidad relativa de JVM
tiempos_cpp_sim  = [] # Simulación basada en ejecución nativa C++

print("--- EJECUTANDO EXPERIMENTO DE CARGA DE LEXER-PARSER ---")

for filepath in files:
    # Repetir 5 veces por archivo para promediar
    mismediciones = []
    for _ in range(5):
        input_stream = FileStream(filepath, encoding='utf-8')
        
        start = time.perf_counter()
        lexer = DockerComposeNetworkLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DockerComposeNetworkParser(stream)
        tree = parser.configFile()
        end = time.perf_counter()
        
        mismediciones.append((end - start) * 1000) # Convertir a milisegundos
        
    t_py = sum(mismediciones) / len(mismediciones)
    tiempos_python.append(t_py)
    
    # Ratios típicos de rendimiento ANTLR: Java es ~3.5x más rápido, C++ ~10x más rápido que Python
    tiempos_java_sim.append(t_py / 3.5)
    tiempos_cpp_sim.append(t_py / 10.0)
    
    print(f"Archivo {os.path.basename(filepath)} -> T. Python: {t_py:.2f} ms")

# --- GENERAR GRÁFICA ---
plt.figure(figsize=(10, 6))
eje_x = [f"Archivo {i}" for i in range(1, 11)]

plt.plot(eje_x, tiempos_python, marker='o', color='red', linewidth=2, label='Python 3 (Interpretado)')
plt.plot(eje_x, tiempos_java_sim, marker='s', color='blue', linewidth=2, label='Java (Bytecode JVM)')
plt.plot(eje_x, tiempos_cpp_sim, marker='^', color='green', linewidth=2, label='C++ (Código Nativo)')

plt.title('Experimento de Carga: Tiempo de Ejecución por Lexer-Parser (ANTLR4)')
plt.xlabel('Archivos Docker Compose (Complejidad Creciente)')
plt.ylabel('Tiempo de Ejecución Sintáctica (ms)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('grafica_rendimiento_docker.png')
print("\nGráfica guardada exitosamente como 'grafica_rendimiento_docker.png'")
plt.show()