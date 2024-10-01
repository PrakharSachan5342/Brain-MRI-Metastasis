import torch
import torch.nn as nn
import segmentation_models_pytorch as smp
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, Dataset
import os

# Define your custom dataset class
class BrainMRIDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.images = os.listdir(image_dir)
        
    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_name = os.path.join(self.image_dir, self.images[idx])
        image = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)  # Load grayscale image
        mask_name = os.path.join(self.mask_dir, self.images[idx])  # Assuming masks have the same name
        mask = cv2.imread(mask_name, cv2.IMREAD_GRAYSCALE)  # Load mask

        if self.transform:
            augmented = self.transform(image=image, mask=mask)
            image = augmented['image']
            mask = augmented['mask']

        return image, mask

# Define the Nested U-Net model
def nested_unet_model():
    return smp.UnetPlusPlus(
        encoder_name="resnet34",
        encoder_weights="imagenet",
        in_channels=1,
        classes=1,
    )

# Define the Attention U-Net model
def attention_unet_model():
    return smp.Unet(
        encoder_name="resnet34",
        encoder_weights="imagenet",
        in_channels=1,
        classes=1,
        decoder_attention_type='scse',
    )

# Function to train the model
def train_model(model, train_loader, val_loader, epochs=10):
    criterion = nn.BCEWithLogitsLoss()  # Change based on your use case
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    for epoch in range(epochs):
        model.train()
        train_loss = 0.0
        
        for images, masks in train_loader:
            images = images.to(device)
            masks = masks.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, masks)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
        
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {train_loss / len(train_loader):.4f}")

    return model

# Function to evaluate the model using DICE Score
def evaluate_model(model, val_loader):
    model.eval()
    dice_scores = []
    with torch.no_grad():
        for images, masks in val_loader:
            images = images.to(device)
            masks = masks.to(device)
            outputs = model(images)
            preds = torch.sigmoid(outputs) > 0.5  # Thresholding
            
            # Calculate DICE score
            intersection = (preds * masks).sum()
            dice_score = (2. * intersection) / (preds.sum() + masks.sum())
            dice_scores.append(dice_score.item())

    avg_dice_score = sum(dice_scores) / len(dice_scores)
    print(f"Average DICE Score: {avg_dice_score:.4f}")
    return avg_dice_score
