import os
import subprocess

target_directory = r"C:\Users\purple Orca\New projects"
project_name = input("Enter project name:").strip()

laravel_path = r"C:\Users\purple Orca\AppData\Roaming\Composer\vendor\bin\laravel.bat"
npm_path = r"C:\Program Files\nodejs\npm.cmd"
composer_path = r"C:\ProgramData\ComposerSetup\bin\composer.bat"
breeze_options = ["react", "--dark", "--typescript", "--eslint", "--ssr"]
vscode_cmd = r"C:\Program Files\Microsoft VS Code\bin\code.cmd"

os.makedirs(target_directory, exist_ok=True)
os.chdir(target_directory)

subprocess.run([laravel_path, "new", project_name, "--react", "--pest", "--no-interaction"])

full_project_path = os.path.join(target_directory, project_name)
env_path = os.path.join(full_project_path, ".env")

subprocess.run([npm_path, "install", "--legacy-peer-deps"], cwd=full_project_path)
subprocess.run([npm_path, "install", "react-router-dom", "--legacy-peer-deps"], cwd=full_project_path)
subprocess.run([npm_path, "run", "build"], cwd=full_project_path)

# === 💾 Configure MySQL in .env ===
if os.path.exists(env_path):
    with open(env_path, "r") as file:
        env_content = file.readlines()

    with open(env_path, "w") as file:
        for line in env_content:
            if line.startswith("DB_CONNECTION="):
                file.write("DB_CONNECTION=mysql\n")
            elif line.startswith("DB_HOST="):
                file.write("DB_HOST=127.0.0.1\n")
            elif line.startswith("DB_PORT="):
                file.write("DB_PORT=3306\n")
            elif line.startswith("DB_DATABASE="):
                file.write(f"DB_DATABASE={project_name}\n")
            elif line.startswith("DB_USERNAME="):
                file.write("DB_USERNAME=\n")
            elif line.startswith("DB_PASSWORD="):
                file.write("DB_PASSWORD=\n")
            else:
                file.write(line)

# Run migrations and seed the DB
subprocess.run(["php", "artisan", "migrate:fresh", "--seed"], cwd=full_project_path)

subprocess.run([vscode_cmd, "."], cwd=full_project_path)
print(f"✅ {full_project_path} has been created , configured, migrated, opened in VS Code, and Vite is running. You're welcome.")

subprocess.Popen(["start", "cmd", "/K", "composer run dev"], cwd=full_project_path, shell=True)