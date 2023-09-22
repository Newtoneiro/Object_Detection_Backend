import torch
from torchvision.utils import save_image


tensor = torch.load('./tensor').float()
save_image(tensor, 'img1.png')
