import torch.utils.data as data
import torch
from PIL import Image


class AttitudeEstimatorDataset(data.Dataset):
    def __init__(self, data_list, transform, phase,
