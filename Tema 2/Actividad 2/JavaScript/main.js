const { performance } = require('perf_hooks');

function collatz(n) {
    if (n % 2 === 0) {
        return Math.floor(n / 2);
    } else {
        return 3 * n + 1;
    }
}

function recursivaCollatz(n, buffer) {
    buffer.push(n);
    if (n === 1) {
        return;
    } else {
        buffer.push(" -> ");
        recursivaCollatz(collatz(n), buffer);
    }
}

function simularCollatz(n) {

    let totalBuffer = [];
    
    for (let i = 2; i <= n; i++) {
        let lineaBuffer = [];
        recursivaCollatz(i, lineaBuffer);
        totalBuffer.push(lineaBuffer.join(''));
    }
    
    process.stdout.write(totalBuffer.join('\n') + '\n');
}

function benchmarkCollatz(n, repeticiones = 10) {
    const tiempos = [];
    const picosMemoria = [];

    for (let r = 0; r < repeticiones; r++) {
        if (global.gc) global.gc();

        const inicioTiempo = performance.now();
        
        simularCollatz(n);

        const finTiempo = performance.now();
        
        const memoriaBytes = process.memoryUsage().heapUsed;

        tiempos.push((finTiempo - inicioTiempo));

        picosMemoria.push(memoriaBytes / (1024 * 1024));
    }

    const tiempoPromedio = tiempos.reduce((a, b) => a + b, 0) / repeticiones;
    const ramPromedio = picosMemoria.reduce((a, b) => a + b, 0) / repeticiones;

    console.log(`\nLenguaje: JavaScript (Node.js)`);
    console.log(`Tamaño (n): ${n}`);
    console.log(`Tiempo Promedio: ${tiempoPromedio.toFixed(6)} milisegundos`);
    console.log(`RAM Promedio (Pico): ${ramPromedio.toFixed(6)} MB\n`);
}

benchmarkCollatz(100000);