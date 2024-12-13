# ERIES-FLEJOI-TestData

This repository contains two main tools for working with `.tdm` (and `.tdx`) files. Each tool is located in its respective subfolder.

## Tools Overview

### 1. **TDM to CSV Converter**
- **Location**: `tdm_to_csv_converter/`
- **Purpose**: Converts `.tdm` files (and their associated `.tdx` files) into `.csv` format for further analysis.
- **Key Features**:
  - Automatically handles `.tdm` and `.TDM` files.
  - Computes a `time` column based on a specified sampling frequency (default: 1000 Hz).
  - Outputs `.csv` files with all channels from the `.tdm` file.

### 2. **TDM File Inspection Notebook**
- **Location**: `inspect_tdm/`
- **Purpose**: Allows interactive inspection of `.tdm` files in a Jupyter Notebook.
- **Key Features**:
  - Opens `.tdm` files and their corresponding `.tdx` files.
  - Displays metadata (number of channels, channel length, file path).
  - Plots time histories of selected channels.

## How to Use

1. **Setup**:
   - Ensure `.tdm` files and their corresponding `.tdx` files are in the same directory.
   - Install the required dependencies for both tools:
     ```bash
     pip install numpy pandas matplotlib tqdm
     ```
   - Ensure `tdm_loader` is installed and correctly configured.

2. **Running the Tools**:
   - Navigate to the respective subfolder and follow the instructions in the tool's `README.md` file.
   - For the CSV converter:
     ```bash
     python tdm_to_csv_converter.py
     ```
   - For the inspection notebook:
     Open the `inspect_tdm.ipynb` file in Jupyter and execute the cells.

## Repository Structure

```
/TDM-Processing-Tools/
│
├── tdm_to_csv_converter/
│   ├── tdm_to_csv_converter.py
│   ├── README.md
│
├── inspect_tdm/
│   ├── inspect_tdm.ipynb
│   ├── README.md
│
└── README.md
```

## License

These tools are provided under the MIT License. Feel free to use and modify them as needed.

