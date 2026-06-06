const std = @import("std");
const time = std.time;

fn collatz(n: u64) u64 {
    if (n % 2 == 0) {
        return n / 2;
    } else {
        return 3 * n + 1;
    }
}

fn recursivaCollatz(n: u64, writer: anytype) void {
    writer.print("{d}", .{n}) catch {};

    if (n == 1) {
        return;
    } else {
        writer.print(" -> ", .{}) catch {};
        recursivaCollatz(collatz(n), writer);
    }
}

fn simularCollatz(n: u64, writer: anytype) void {
    var i: u64 = 2;
    while (i <= n) : (i += 1) {
        recursivaCollatz(i, writer);
        writer.print("\n", .{}) catch {};
    }
}

pub fn main() !void {
    const n: u64 = 5000;
    const repeticiones: usize = 10;

    var tiempos: [repeticiones]f64 = undefined;
    var picos_memoria: [repeticiones]f64 = undefined;

    var r: usize = 0;
    while (r < repeticiones) : (r += 1) {
        var gpa = std.heap.GeneralPurposeAllocator(.{
            .enable_memory_limit = true,
        }){};
        const allocator = gpa.allocator();

        const stdout_file = std.io.getStdOut().writer();

        var bw = std.io.bufferedWriter(stdout_file);
        var dummy_list = std.ArrayList(u64).init(allocator);

        try dummy_list.append(n);

        const inicio_tiempo = time.nanoTimestamp();

        simularCollatz(n, bw.writer());
        try bw.flush();

        const fin_tiempo = time.nanoTimestamp();

        const duracion_milisecs = @as(f64, @floatFromInt(fin_tiempo - inicio_tiempo)) / 1_000_000.0;
        tiempos[r] = duracion_milisecs;

        const memoria_bytes = gpa.total_requested_bytes;
        picos_memoria[r] = @as(f64, @floatFromInt(memoria_bytes)) / (1024.0 * 1024.0);

        dummy_list.deinit();
        _ = gpa.deinit();
    }

    var suma_tiempos: f64 = 0;
    var suma_ram: f64 = 0;
    for (tiempos) |t| {
        suma_tiempos += t;
    }
    for (picos_memoria) |m| {
        suma_ram += m;
    }

    const tiempo_promedio = suma_tiempos / @as(f64, @floatFromInt(repeticiones));
    const ram_promedio = suma_ram / @as(f64, @floatFromInt(repeticiones));

    std.debug.print("\nLenguaje: Zig (0.13.0)\n", .{});
    std.debug.print("Tamaño (n): {d}\n", .{n});
    std.debug.print("Tiempo Promedio: {d:.6} milisegundos\n", .{tiempo_promedio});
    std.debug.print("RAM Promedio (Pico): {d:.6} MB\n", .{ram_promedio});
}
