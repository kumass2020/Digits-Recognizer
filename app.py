import torch
import torch.nn.functional as F
import pandas

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

class CustomDataset(Dataset):
    def __init__(self):
        self.x_data = pd.read_csv('./digit-recognizer/')
    def __len__(self):
        return len(self)
    def __getitem__(self, idx):