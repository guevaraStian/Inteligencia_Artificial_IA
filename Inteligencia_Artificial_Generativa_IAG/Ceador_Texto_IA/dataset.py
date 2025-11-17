# dataset.py
import torch

class TextDataset(torch.utils.data.Dataset):
    def __init__(self, path, seq_len=128):
        self.text = open(path, "r", encoding="utf-8").read()
        self.chars = sorted(list(set(self.text)))
        self.stoi = {c:i for i,c in enumerate(self.chars)}
        self.itos = {i:c for c,i in self.stoi.items()}
        self.vocab_size = len(self.chars)
        self.seq_len = seq_len

        self.ids = torch.tensor([self.stoi[c] for c in self.text])

    def __len__(self):
        return len(self.ids) - self.seq_len

    def __getitem__(self, idx):
        x = self.ids[idx:idx+self.seq_len]
        y = self.ids[idx+1:idx+self.seq_len+1]
        return x, y