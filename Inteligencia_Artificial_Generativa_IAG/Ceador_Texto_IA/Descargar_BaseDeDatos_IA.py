import os
from datasets import load_dataset

# pip install datasets transformers


# -----------------------------------------
# 1) SELECCIONA AQUÍ EL DATASET A DESCARGAR
# -----------------------------------------
# Opciones recomendadas:
#   wikitext: "wikitext", subset "wikitext-2-raw-v1"
#   openwebtext: "openwebtext"
#   gutenberg: "gutenberg"
#   bookcorpus: "bookcorpus"

DATASET_NAME = "wikitext"           # cámbialo si quieres otro
DATASET_SUBSET = "wikitext-2-raw-v1"  # solo para wikitext

# -----------------------------------------
# 2) Carpeta donde guardaremos los .txt
# -----------------------------------------
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------------------
# 3) Descargar dataset
# -----------------------------------------
print(f"Descargando dataset: {DATASET_NAME} ...")
if DATASET_NAME == "wikitext":
    dataset = load_dataset(DATASET_NAME, DATASET_SUBSET)
else:
    dataset = load_dataset(DATASET_NAME)

print("Dataset descargado.")
print(dataset)

# -----------------------------------------
# 4) Función para guardar cada parte como .txt
# -----------------------------------------
def save_split(split_name, filename):
    print(f"Procesando {split_name}...")

    texts = dataset[split_name]["text"]
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        for line in texts:
            if line.strip():
                f.write(line.strip() + "\n")

    print(f"{filename} guardado ({len(texts)} líneas).")

# -----------------------------------------
# 5) Guardar Entrenamiento / valid / test
# -----------------------------------------
if "Entrenamiento" in dataset:
    save_split("Entrenamiento", "Entrenamiento.txt")
if "validation" in dataset:
    save_split("validation", "valid.txt")
if "test" in dataset:
    save_split("test", "test.txt")

print("\n✔ Listo. Los archivos están en la carpeta 'data/'")