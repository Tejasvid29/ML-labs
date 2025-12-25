# ML 14-Day Theme Sprint

This repository contains a structured, short-term exploration of core machine learning themes using a unified experimental setup.  
The goal is to compare different ML directions through **reproducible experiments, consistent evaluation, and clear documentation**, and then expand one direction into a deeper project.

---

## What This Project Does
- Runs controlled experiments across multiple machine learning themes
- Uses a shared dataset, model, and training pipeline for fair comparison
- Emphasizes clean logging, evaluation, and interpretation of results
- Produces artifacts (figures, tables, summaries) that can be extended into a larger study

---

## Themes Explored
The project explores four machine learning directions:

1. **Optimization & Generalization**  
   Training dynamics, optimizer behavior, and robustness under stress tests.

2. **Uncertainty & Probabilistic ML**  
   Model confidence, calibration, and reliability of predictions.

3. **Representation Learning (Self-Supervised)**  
   Learning transferable embeddings without labels and evaluating them rigorously.

4. **Efficient ML Systems**  
   Benchmarking and improving inference and training efficiency.

---

## Repository Structure

ML-labs/
├── README.md                     # Project overview & navigation
│
├── mini/                         # Theme-specific summaries (NO CODE)
│   ├── 01_optimization/
│   │   └── README.md
│   ├── 02_uncertainty/
│   │   └── README.md
│   ├── 03_self_supervised/
│   │   └── README.md
│   └── 04_efficiency/
│       └── README.md
│
├── common/                       # Shared implementation code
│   ├── data.py
│   ├── model.py
│   ├── train.py
│   └── utils.py
│
├── runs/                         # Experiment logs & checkpoints
│
├── results/                      # Figures & tables
│
├── reports/                      # Cross-theme reasoning & planning
│   ├── decision_memo.md
│   └── project_spec.md



---

## How to Navigate the Project
- Start with `mini/` for high-level summaries of each theme
- Use `common/` for implementation details
- Refer to `reports/` for comparisons and planning
- Generated experiment outputs are organized under `runs/` and `results/`

---

## Status
🚧 In progress — experiments and documentation will be updated as the project evolves.

