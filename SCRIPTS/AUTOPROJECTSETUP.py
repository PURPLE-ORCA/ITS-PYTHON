import os
import subprocess

target_directory = r"C:\Users\purple Orca\New projects"
project_name = input("Enter project name:").strip()

laravel_path = r"C:\Users\purple Orca\AppData\Roaming\Composer\vendor\bin\laravel.bat"
npm_path = r"C:\Program Files\nodejs\npm.cmd"
composer_path = r"C:\ProgramData\ComposerSetup\bin\composer.bat"
breeze_options = ["react", "--dark", "--typescript", "--eslint", "--ssr"]

os.makedirs(target_directory, exist_ok=True)
os.chdir(target_directory)
subprocess.run([laravel_path, "new", project_name, "--react", "--pest"])

full_project_path = os.path.join(target_directory, project_name)

subprocess.run([npm_path, "install", "--legacy-peer-deps"], cwd=full_project_path)
subprocess.run([npm_path, "install", "react-router-dom", "--legacy-peer-deps"], cwd=full_project_path)
subprocess.run([npm_path, "run", "build"], cwd=full_project_path)

print(f"✅{full_project_path} has been created successfully!")