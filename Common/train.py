import argparse
import os

import torch
import torch.nn as nn
import torch.optim as optim

from Common.data import get_dataloaders
from Common.model import get_model

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type = int, default=5)
    parser.add_argument("--batch_size", type=int, default = 128)
    parser.add_argument("--lr", type=float, default = 1e-3)
    parser.add_argument("--run_name", type=str, default = "baseline")
    return parser.parse_args()

def prepare_run_dir(run_name): #creates a new file to keep records isolated and clean
    run_dir = os.path.join("runs", run_name)
    os.makedirs(run_dir, exist_ok = True)
    return run_dir

def main():
    args = parse_args()

    #Prepare run directory
    run_dir = prepare_run_dir(args.run_name)

    #Devuce setup
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    #Load Data
    train_loader, test_loader = get_dataloaders(
        batch_size=args.batch_size
    )

    #Initialize model
    model = get_model()
    model = model.to(device)

    #Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr = args.lr)

    #Training loop 
    model.train()
    total_loss = 0.0

    for batch_idx, (images, labels) in enumerate(train_loader):
        if batch_idx % 50 == 0:
            print(f"Training batch {batch_idx}/{len(train_loader)}")

        images = images.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        #backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss/ len(train_loader)
    print(f"Training loss (epoch 1): {avg_loss:.4f}")

    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            _, predicted = torch.max(outputs, dim = 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = 100.0 * correct/total
    print(f"Test accuracy: {accuracy:.2f}")

    print(f"Run direcorty: {run_dir}")
    print(f"Using device: {device}")
    print(f"Train batches: {len(train_loader)}, Test batches: {len(test_loader)}")

if __name__ == "__main__":
    main()

