# Optimizer Comparison: AdamW vs SGD

## Abstract
This experiment investigates how optimizer choice affects optimization dynamics and generalization behavior when training a fixed architecture (ResNet-18) on a fixed dataset (CIFAR-10). By holding all other variables constant and varying only the optimizer, we aim to observe differences in convergence speed, loss smoothness, and test accuracy trajectories over training epochs. Rather than focusing solely on final accuracy, this study emphasizes learning dynamics as evidence of optimizer behavior, with the goal of building intuition for controlled ablation studies in deep learning.

## Rationale
AdamW and SGD with momentum differ fundamentally in how they update parameters. AdamW uses adaptive per-parameter learning rates derived from first and second moments of gradients, often leading to faster early convergence and smoother optimization. SGD with momentum, while less adaptive, is known to introduce implicit regularization effects that can improve generalization, particularly on vision tasks. Prior empirical work suggests that these differences manifest not only in final performance but also in how loss and accuracy evolve across epochs, especially under limited training budgets.

## Hypotheses
- H1 (Convergence Speed): AdamW will achieve higher test accuracy in early epochs due to adaptive learning rates.
- H2 (Stability): AdamW will exhibit smoother and less noisy loss curves compared to SGD.
- H3 (Generalization Trend): SGD with momentum may close the accuracy gap or surpass AdamW in later epochs due to implicit regularization effects.
- H4 (Failure Mode): If SGD fails to converge adequately within 20 epochs, it may indicate sensitivity to learning rate choice rather than optimizer inferiority.

## Setup
- Model: ResNet-18
- Dataset: CIFAR-10 (subset)
- Batch size: 32
- Epochs: 1
- Learning rate: 1e-3

## Results

### AdamW
- Training loss (epoch 1): 1.9976
- Test accuracy: 30.90 %

### SGD (momentum = 0.9)
- Training loss (epoch 1): 2.1302
- Test accuracy: 30.80 %

## Immediate Observations
- AdamW convergence speed:
- SGD convergence speed:
- Stability (loss smoothness):

