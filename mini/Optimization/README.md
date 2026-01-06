# Optimization & Generalization: AdamW vs SGD on CIFAR-10

## Abstract
We study how optimizer choice affects convergence speed and generalization when training a ResNet-18 on CIFAR-10. Using a strictly controlled setup (same data, model, seed, and training budget), we compare AdamW and SGD with momentum over 20 epochs. We observe that AdamW converges significantly faster and achieves higher test accuracy under a fixed training budget, while SGD improves more slowly but steadily. These results highlight practical trade-offs between adaptive and non-adaptive optimization methods in small-budget regimes.

---

## Hypothesis
We hypothesize that **AdamW will converge faster than SGD** due to its adaptive learning rates and decoupled weight decay, especially under a limited number of training epochs. We further expect SGD to show slower but more stable improvement, potentially requiring longer training to close the performance gap.

---

## Experimental Setup
- **Dataset:** CIFAR-10  
- **Model:** ResNet-18  
- **Epochs:** 20  
- **Batch size:** 128  
- **Learning rate:** 1e-3  
- **Seed:** 42  
- **Optimizers:**  
  - AdamW  
  - SGD with momentum (0.9)  
- **Hardware:** NVIDIA T4 GPU (Google Colab)  

All hyperparameters except the optimizer were held constant to ensure a fair comparison.

---

## Results

### Test Accuracy vs Epoch
![Accuracy](../../results/figures/opt_adamw_vs_sgd_acc.png)

### Training Loss vs Epoch
![Loss](../../results/figures/opt_adamw_vs_sgd_loss.png)

---

## Interpretation
AdamW demonstrates substantially faster early convergence, reaching higher test accuracy within the first few epochs and maintaining a consistent advantage throughout training. The training loss curve shows a smoother and more rapid decrease for AdamW, suggesting more effective optimization dynamics under the same learning rate.

SGD, while slower to converge, exhibits steady improvement and a more gradual loss reduction. This behavior is consistent with classical observations that SGD often requires longer training schedules or learning-rate tuning to match adaptive optimizers in short-budget settings.

Together, the accuracy and loss curves indicate that **optimizer choice has a significant impact on practical performance when training time is constrained**, even when model and data remain unchanged.

---

## Limitations
- Only a single learning rate was evaluated for each optimizer  
- Training was limited to 20 epochs  
- No learning-rate schedules were used  
- Results are based on a single random seed  

These factors limit conclusions about long-run generalization and optimal hyperparameter regimes.

---

## Next Steps
- Extend training to longer horizons to test whether SGD closes the gap  
- Evaluate robustness under label noise or stronger data augmentation  
- Compare optimizers under different learning-rate schedules  

These directions motivate the **generalization stress tests** explored in subsequent experiments.

---

## Generalization Stress Test (Augmentation Strength)

### Hypothesis
Stronger data augmentation will slow early optimization and increase training loss, but improve or stabilize test accuracy by encouraging invariance and reducing overfitting. Under a fixed compute budget, this may trade off convergence speed for better generalization.

### Experimental Setup

### Results

### Interpretation

### Limitations

