import subprocess

req = {
    "python", "tqdm", "pip", "ipython", "numpy", "scipy", "pandas", 
    "scikit-learn", "matplotlib", "seaborn", "ipywidgets", "nltk", "umap-learn",
    "xgboost", "scikit-optimize", "jcopml", "luwiji", "pillow", "kmodes", "pytorch",
    "torchvision", "torchtext"
}
env_name = "jcop_usl"
working_folder = "unsupervised_learning"
env_file = "env_jcop_usl.yml"


def existing_env():
    result = subprocess.run(["conda", "env", "list"], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8').split("\n")
    return [r.split()[0] for r in result if "envs" in r]


def existing_package(env):
    result = subprocess.run(["conda", "list", "--name", env], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8').split("\n")
    return [r.split()[0] for r in result[4:-1]]


def main():
    # Langsung cek environment jcop_usl tanpa peduli dengan environment base
    if env_name in existing_env():
        print(f"✓ Environment {env_name} terdeteksi.\n")
        exist = set(existing_package(env_name))
        
        # Mengecek apakah semua library utama sudah lengkap
        if req.issubset(exist):
            print(f"✓ Package telah terinstall dengan baik di dalam environment {env_name}\n")
            print("✓ Selesai! Environment siap digunakan di Jupyter VS Code. Selamat belajar!")                
        else:
            print(f"Kelihatannya package {req - exist} belum terinstall.")
            print("Silakan jalankan ulang installernya atau install package yang kurang menggunakan pip/conda.")
    else:
        print(f"Environment {env_name} tidak ditemukan.")
        print(f"Mohon jalankan command berikut pada folder kerja `{working_folder}`:")
        print(f">> conda env create -f {env_file}")
        
if __name__ == "__main__":
    main()
