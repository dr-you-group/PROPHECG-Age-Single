# PROPHECG-Age Single
A single-lead ECG age prediction model built on a 1D ResNet-based convolutional neural network.

## Overview
This repository provides all the code, data samples, and documentation needed to train, evaluate, and run inference with the PROPHECG-Age Single model.
The model predicts a subject’s physiological age from raw wearable single-lead ECG waveforms sampled at 200 Hz over 10 seconds.
The complete code for training and inference is available in this repository. The final trained model weights will be released upon the publication of our manuscript.

## Repository Structure
```text
PROPHECG-Age-Single/
├── src/                  # Core Python modules
│   ├── resnet.py         # ResNet1D model definition
│   └── preprocess.py     # ECG preprocessing pipeline
├── scripts/              # Configuration & helper scripts (e.g., age_prediction.yaml)
├── models/               # Pretrained model weights (.pth/.pt)
├── data/                 # Example ECG inputs (CSV, Pickle)
├── notebooks/            # Jupyter notebooks for analysis & inference
│   └── main.ipynb        # Interactive example: load sample data, preprocess, and predict age
├── docs/                 # Documentation files (CONTRIBUTING.md, CODE_OF_CONDUCT.md)
├── .gitignore            # Ignored files and directories
├── LICENSE               # MIT License
├── README.md             # Project overview and instructions
└── requirements.txt      # Python dependency list
```

## ECG Data Processing
- **Sampling**: 200 Hz, 10 s duration, single lead
- **Preprocessing pipeline**:
  1. Resample to 200 Hz if source rate differs
  2. Remove DC offset
  3. Apply 0.5–50 Hz Butterworth bandpass filter
  4. Normalize to [0, 1]
- **Model input shape**: `(1, 2000)` (single lead, 2000 samples)

## Model Architecture
Our model adapts the ResNet1D design introduced by Cho _et al._ (2025), which builds on the original 1D ResNet framework from Lima _et al._ (2021). We adjusted block depths and sampling strides for optimal age‐prediction performance, and added a final regression layer.

### Output Scaling
During training, true ages were divided by 5 to stabilize regression targets; at inference, multiply the model’s raw output by 5 to recover age in years.

## Quickstart
1. **Clone the repository**:
   ```bash
   git clone https://github.com/dr-you-group/PROPHECG-Age-Single.git
   cd PROPHECG-Age-Single
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the interactive example**:
   ```bash
   jupyter lab # or jupyter notebook
   ```
   Open `notebooks/main.ipynb` to load sample data, apply preprocessing, and compute age predictions with one click.

## References
- Lima _et al._, *Nature Communications* 12, 5117 (2021). https://doi.org/10.1038/s41467-021-25351-7
- Cho _et al._, “Artificial intelligence–derived electrocardiographic aging and risk of atrial fibrillation: a multi-national study,” *European Heart Journal* 46(9):839–852 (2025). https://doi.org/10.1093/eurheartj/ehae790
