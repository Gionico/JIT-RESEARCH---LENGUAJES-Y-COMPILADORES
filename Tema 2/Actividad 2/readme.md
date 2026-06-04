Pruebas
n	    Lenguaje	    ms	            MB
5000	JavaScript	    532,0149	    26,126051
        Python	        4.222,5967	    0,023397
        Rust	        509,4000	    0,00791
        Zig	            511,6647	    0,000061
10000	JavaScript	    1.142,2960	    45,665901
        Python	        10.111,1300	    0,026167
        Rust	        1.012,8000	    0,00791
        Zig	            1.127,6699	    0,000061
50000	JavaScript	    6.804,8727	    116,140936
        Python	        56.718,6152	    0,034247
        Rust	        6.057,9000	    0,00791
        Zig	            5.785,3608	    0,000061


Versiones instaladas:
 zig > 0.13.0
 python > 3.11.7
 javaScript - node > 22.16.0
 rust-cargo >  1.96.0

Comandos utilizados para ejecutar:
 python > py .\main.py
 zig > zig build run -Doptimize=ReleaseFast
 rust-cargo > cargo run --release
 javaScript-node > node .\main.js