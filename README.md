# PROPHECG-Age Single

A single-lead ECG age prediction model built on a 1D ResNet-based convolutional neural network.

## Overview
This repository provides everything needed to train, evaluate, and perform inference with the PROPHECG-Age Single model. The model predicts a subject’s physiological age from raw single-lead ECG waveforms sampled at 200 Hz over 10 seconds.

## Repository Structure
```text
PROPHECG-Age-Single/
├── src/                  # Core Python modules
│   ├── resnet.py         # ResNet1D model definition
│   └── preprocess.py     # ECG preprocessing pipeline
├── scripts/              # Configuration & helper scripts (e.g., age_prediction.yaml)
├── models/               # Pretrained model weights (.pth/.pt)
├── data/                 # Example ECG inputs (CSV, Pickle)
├── notebooks/            # Jupyter notebooks for AI-ECG Age analysis
├── docs/                 # Documentation (CONTRIBUTING.md, CODE_OF_CONDUCT.md)
├── .gitignore            # Ignored files and directories
├── LICENSE               # MIT License
├── README.md             # Project overview and instructions
└── requirements.txt      # Python dependency list
```

## ECG Data Processing
- **Sampling**: 200 Hz, 10 s duration, single lead
- **Preprocessing**:
  1. Resample input to 200 Hz (if needed)
  2. Remove DC offset
  3. Apply 0.5–50 Hz Butterworth bandpass filter
  4. Normalize to [0, 1]
- **Input shape**: `(2000, 1)`

## Model Architecture
Our PROPHECG-Age Single model is an adaptation of the ResNet1D design introduced by Cho _et al._ (2025), which itself builds on the original 1D ResNet framework from Lima _et al._ (2021). We modified the block depths and sampling strides to optimize age prediction from single-lead ECG inputs, with a final regression layer for direct age estimation.

**Output Scaling**
During training, true ages were divided by 5 to stabilize regression targets; at inference time, the model’s raw output is multiplied by 5 to recover the age in years.

## References
- Lima _et al._, _Nature Communications_ 12, 5117 (2021). https://doi.org/10.1038/s41467-021-25351-7
- Cho _et al._, “Artificial intelligence–derived electrocardiographic aging and risk of atrial fibrillation: a multi-national study,” _European Heart Journal_ 46(9):839–852 (2025).
