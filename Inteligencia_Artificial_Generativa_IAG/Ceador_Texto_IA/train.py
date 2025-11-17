# train.py
import torch
from torch.utils.data import DataLoader
from dataset import TextDataset
from model import TextGenModel
from tqdm import tqdm

device = "cuda" if torch.cuda.is_available() else "cpu"

train_data = TextDataset("data/train.txt")
valid_data = TextDataset("data/valid.txt")

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

model = TextGenModel(train_data.vocab_size).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = torch.nn.CrossEntropyLoss()

EPOCHS = 3

for epoch in range(EPOCHS):
    model.train()
    pbar = tqdm(train_loader)
    for x, y in pbar:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()

        logits, _ = model(x)
        loss = criterion(logits.reshape(-1, train_data.vocab_size), y.reshape(-1))

        loss.backward()
        optimizer.step()
        pbar.set_description(f"Epoch {epoch+1} Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), "model.pth")

print("Entrenamiento completo.")