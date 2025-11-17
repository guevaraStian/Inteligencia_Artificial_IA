# Generador.py
import torch
from Model import TextGenModel
from dataset import TextDataset

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset = TextDataset("data/Entrenamiento.txt")
Model = TextGenModel(dataset.vocab_size)
Model.load_state_dict(torch.load("Model.pth", map_location=device))
Model.to(device)
Model.eval()

def Generador_text(start="Hola", length=500, temperature=0.8):
    chars = list(start)
    input_ids = torch.tensor([dataset.stoi[c] for c in chars]).unsqueeze(0).to(device)

    hidden = None

    for _ in range(length):
        logits, hidden = Model(input_ids[:,-1:].to(device), hidden)
        logits = logits[0, -1] / temperature
        prob = torch.softmax(logits, dim=0)
        next_id = torch.multinomial(prob, 1).item()
        
        chars.append(dataset.itos[next_id])
        input_ids = torch.tensor([[next_id]]).to(device)

    return "".join(chars)

print(Generador_text("Hola,"))