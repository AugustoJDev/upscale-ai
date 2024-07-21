import os
import subprocess
import shutil

def run_bat_file(bat_file):
    try:
        subprocess.run(bat_file, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o arquivo .bat: {e}")

def delete_files(folder):
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        print("Todos os arquivos foram deletados!")
    except Exception as e:
        print(f"Erro ao deletar arquivos: {e}")

def main():
    base_path = os.path.abspath(os.path.dirname(__file__))

    # Executa o arquivo start.bat
    bat_file = os.path.join(base_path, "start.bat")
    run_bat_file(bat_file)

    # Exclui todos os arquivos da pasta input
    input_folder = os.path.join(base_path, "input")
    delete_files(input_folder)

    # Abre a pasta output
    output_folder = os.path.join(base_path, "output")
    os.startfile(output_folder)

if __name__ == "__main__":
    main()
