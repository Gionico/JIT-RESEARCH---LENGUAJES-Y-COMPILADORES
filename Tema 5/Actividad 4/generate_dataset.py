# generate_dataset.py
import os

def generate_docker_compose(num_networks, num_services, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("version: '3.8'\n\n")
        f.write("networks:\n")
        for i in range(num_networks):
            f.write(f"  net_custom_{i}:\n")
            f.write("    driver: bridge\n")
            f.write("    attachable: true\n")
            
        f.write("\nservices:\n")
        for j in range(num_services):
            f.write(f"  web_service_{j}:\n")
            f.write("    image: nginx:latest\n")
            f.write("    networks:\n")
            f.write(f"      net_custom_{j % num_networks}\n")

os.makedirs("test_files", exist_ok=True)
for n in range(1, 11):
    filename = f"test_files/docker_compose_{n}.yml"
    generate_docker_compose(num_networks=n * 10, num_services=n * 20, filename=filename)
    print(f"Generado {filename}")