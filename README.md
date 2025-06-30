# PROPHECG-Age Single
Single-lead ECG age prediction model using a ResNet1D-based convolutional neural network.

## Overview
This repository contains all code, data samples, and documentation needed to train and evaluate the PROPHECG-Age Single model, which predicts a subject’s physiological age from raw single-lead ECG waveforms (500 Hz, 10 s).

## Repository Structure
```text
PROPHECG-Age-Single/
├── src/                  # Core Python modules (train, evaluate, model definition)
│   ├── resnet.py
├── scripts/              # Configuration & helper scripts (e.g., age_prediction.yaml)
├── models/               # Trained model weights (.pth/.pt)
├── data/                 # Sample ECG CSV/pickle files
├── notebooks/            # Jupyter notebooks for analysis
├── docs/                 # Documentation (CONTRIBUTING, CODE_OF_CONDUCT)
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── README.md             # This file
└── requirements.txt      # Python dependencies
