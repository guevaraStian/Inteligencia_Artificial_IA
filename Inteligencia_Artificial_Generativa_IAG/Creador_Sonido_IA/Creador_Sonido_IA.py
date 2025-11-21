# pip install simpleaudio music21 numpy 
# pip install numpy requests pydub

# pip 25.2 pip 25.2 
# generador_musica_midi_mutopia.py

import os
import urllib.request
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from scipy.io.wavfile import write
import mido

# ======================
# DESCARGA DE UN MIDI PÚBLICO (MUTOPIA)
# ======================

# Ejemplo: MIDI de dominio público de Mutopia.
# Aquí asumo que tienes una URL directa a un MID (ejemplo imaginario, reemplázala)
#midi_url = "https://www.mutopiaproject.org/ftp/MIDI/bach/bwv846.mid"
midi_file = "MIDI.mid"

#if not os.path.exists(midi_file):
#    print("Descargando MIDI desde Mutopia...")
#    urllib.request.urlretrieve(midi_url, midi_file)
#    print("MIDI descargado.")

# LEER NOTAS DESDE EL MIDI


mid = mido.MidiFile(midi_file)
notes = []

for track in mid.tracks:
    for msg in track:
        if msg.type == 'note_on' and msg.velocity > 0:
            notes.append(msg.note)

if len(notes) < 20:
    raise ValueError("No se obtuvieron suficientes notas del MIDI para entrenar.")

unique_notes = sorted(set(notes))
note_to_int = {n: i for i, n in enumerate(unique_notes)}
int_to_note = {i: n for n, i in note_to_int.items()}
sequence = [note_to_int[n] for n in notes]

# PREPARAR DATOS PARA LSTM

seq_length = 10
X = []
y = []

for i in range(len(sequence) - seq_length):
    X.append(sequence[i:i+seq_length])
    y.append(sequence[i+seq_length])

X = torch.tensor(X, dtype=torch.long)
y = torch.tensor(y, dtype=torch.long)

# MODELO LSTM

class MusicLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=32, hidden_dim=128, num_layers=2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden=None):
        x = self.embedding(x)
        out, hidden = self.lstm(x, hidden)
        out = self.fc(out[:, -1, :])
        return out, hidden

vocab_size = len(unique_notes)
model = MusicLSTM(vocab_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.005)

# ENTRENAMIENTO

epochs = 80
for epoch in range(epochs):
    optimizer.zero_grad()
    out, _ = model(X)
    loss = criterion(out, y)
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

# GENERAR SECUENCIA

start_seq = X[0].unsqueeze(0)
generated = start_seq.tolist()[0]

model.eval()
hidden = None
for _ in range(50):
    inp = torch.tensor([generated[-seq_length:]], dtype=torch.long)
    with torch.no_grad():
        out, hidden = model(inp, hidden)
        prob = torch.softmax(out, dim=1)
        next_idx = torch.multinomial(prob, 1).item()
        generated.append(next_idx)

generated_notes = [int_to_note[i] for i in generated]

# CONVERTIR A AUDIO (WAV)

sample_rate = 44100
audio = np.array([], dtype=np.float32)

def midi_to_freq(midi_note):
    return 440.0 * (2 ** ((midi_note - 69) / 12.0))

for n in generated_notes:
    freq = midi_to_freq(n)
    t = np.linspace(0, 0.2, int(0.2 * sample_rate), False)
    wave = 0.3 * np.sin(2 * np.pi * freq * t)
    audio = np.concatenate((audio, wave))

max_samples = sample_rate * 10
audio = audio[:max_samples]

write("generacion.wav", sample_rate, (audio * 32767).astype(np.int16))

print("¡Música generada en generacion.wav!")