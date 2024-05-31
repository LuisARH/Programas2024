import os
import subprocess

def create_executable(script_path):
    # Verificar que el archivo de script existe
    if not os.path.isfile(script_path):
        print(f"Error: El archivo {script_path} no existe.")
        return

    # Construir el comando de PyInstaller
    command = f"pyinstaller --onefile {script_path}"

    # Ejecutar el comando
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Mostrar la salida del comando
    print(process.stdout.decode())
    print(process.stderr.decode())

    if process.returncode == 0:
        print("¡El ejecutable se ha creado exitosamente!")
    else:
        print("Hubo un error al crear el ejecutable.")

if __name__ == "__main__":
    script_path = input("Ingrese la ruta del archivo .py que desea convertir en un ejecutable: ")
    create_executable(script_path)
