use std::io::{self, Write, BufWriter};
use std::time::Instant;
use stats_alloc::{Region, StatsAlloc, INSTRUMENTED_SYSTEM};
use std::alloc::System;

// Configuramos el rastreador de memoria global (equivalente a preparar tracemalloc)
#[global_allocator]
static GLOBAL: &StatsAlloc<System> = &INSTRUMENTED_SYSTEM;

fn collatz(n: u64) -> u64 {
    if n % 2 == 0 {
        n / 2
    } else {
        3 * n + 1
    }
}

fn recursiva_collatz<W: Write>(n: u64, writer: &mut W) {
    let _ = write!(writer, "{}", n);
    
    if n == 1 {
        return;
    } else {
        let _ = write!(writer, " -> ");
        recursiva_collatz(collatz(n), writer);
    }
}

fn simular_collatz(n: u64) {
    // Creamos un Buffer de Escritura gigante para la consola de manera global
    let stdout = io::stdout();
    let mut writer = BufWriter::new(stdout.lock());

    for i in 2..=n {
        recursiva_collatz(i, &mut writer);
        let _ = writeln!(writer);
    }
    
    let _ = writer.flush(); 
}
fn benchmark_collatz(n: u64, repeticiones: usize) {
    let mut tiempos = Vec::new();
    let mut picos_memoria = Vec::new();

    for _ in 0..repeticiones {
        // Inicializar el contador de memoria para esta iteración (como tracemalloc.start())
        let region = Region::new(&GLOBAL);
        let inicio_tiempo = Instant::now();

        simular_collatz(n);

        let duracion = inicio_tiempo.elapsed();
        // Obtener estadísticas de memoria asignada
        let stats = region.change(); 
        
        tiempos.push(duracion.as_secs_f64());
        // stats.bytes_allocated nos da el total de bytes pedidos a la RAM en este bloque
        picos_memoria.push((stats.bytes_allocated as f64) / (1024.0 * 1024.0));
    }

    let tiempo_promedio: f64 = tiempos.iter().sum::<f64>() / (repeticiones as f64);
    let ram_promedio: f64 = picos_memoria.iter().sum::<f64>() / (repeticiones as f64);

    println!("\nLenguaje: Rust");
    println!("Tamaño (n): {}", n);
    println!("Tiempo Promedio: {:.6} segundos", tiempo_promedio);
    println!("RAM Promedio (Pico): {:.6} MB", ram_promedio);
}

fn main() {
    benchmark_collatz(5000, 5);
}
