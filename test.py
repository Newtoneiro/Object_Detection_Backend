import torch
import matplotlib.pyplot as plt

tensor = torch.load("./saved_images/some_tensor.pt")
print(tensor.shape)
plt.imshow(torch.flip(tensor, [1]))
plt.show()
