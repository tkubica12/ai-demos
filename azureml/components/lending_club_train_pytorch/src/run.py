import argparse
import numpy as np
import torch
from torch import nn
import mlflow
import pytorch_lightning as pl
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
import torchmetrics as tm

parser = argparse.ArgumentParser("prep")
parser.add_argument("--x-train", type=str, help="Training features file")
parser.add_argument("--x-test", type=str, help="Testing features file")
parser.add_argument("--y-train", type=str, help="Training labels file")
parser.add_argument("--y-test", type=str, help="Testing labels file")
parser.add_argument("--saved-scaler", type=str, help="Saved scaler file to log with model as artefact")
parser.add_argument("--finished", type=str, help="Signal training is finished")
args = parser.parse_args()

mlflow.autolog()

# Load data
X_train = np.loadtxt(args.x_train, delimiter=",", dtype=float)
X_test = np.loadtxt(args.x_test, delimiter=",", dtype=float)
y_train = np.loadtxt(args.y_train, delimiter=",", dtype=float)
y_test = np.loadtxt(args.y_test, delimiter=",", dtype=float)

# Set tag
mlflow.set_tag("algorithm", "pytorch")

# Log scaler artefact
mlflow.log_artifact(args.saved_scaler, "model")

# Create tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).reshape(-1, 1)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32).reshape(-1, 1)

# Define model
class LandingClub(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(150, 75)
        self.layer2 = nn.Linear(75, 37)
        self.layer3 = nn.Linear(37, 18)
        self.layer4 = nn.Linear(18, 1)
        self.layer_norm = nn.LayerNorm(75)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer_norm(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.relu(x)
        x = self.layer3(x)
        x = self.relu(x)
        x = self.layer4(x)
        x = self.sigmoid(x)
        return x

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_pred = self.forward(x)
        loss = nn.BCELoss()(y_pred, y)
        acc = tm.functional.accuracy(y_pred, y, task="binary")
        auc = tm.functional.auroc(y_pred, y.long(), task="binary")
        self.log('train_loss', loss)
        self.log('train_accuracy', acc)
        self.log('train_auc', auc)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_pred = self.forward(x)
        loss = nn.BCELoss()(y_pred, y)
        acc = tm.functional.accuracy(y_pred, y, task="binary")
        auc = tm.functional.auroc(y_pred, y.long(), task="binary")
        self.log('val_loss', loss)
        self.log('val_accuracy', acc)
        self.log('val_auc', auc)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=0.01)
        return optimizer

# Loaders
train_dataset = torch.utils.data.TensorDataset(X_train, y_train)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=1000, shuffle=True)
test_dataset = torch.utils.data.TensorDataset(X_test, y_test)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1000)

# Early stopping
early_stop_callback = EarlyStopping(monitor="val_auc", min_delta=0.00, patience=20, verbose=True, mode="max")

# Training
model = LandingClub()
trainer = pl.Trainer(max_epochs=200, callbacks=[early_stop_callback])
trainer.fit(model, train_loader, test_loader)

# Finished
from pathlib import Path
Path(args.finished).touch()