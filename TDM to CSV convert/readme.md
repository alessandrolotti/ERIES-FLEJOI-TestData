
# TDM to CSV Conversion Script

## Overview

This script automates the process of converting `.tdm` (or `.TDM`) files into `.csv` format. It allows users to select a specific folder (or work with the current directory) and generates `.csv` files with additional time data for each channel in the `.tdm` files.

## Features

- **File Handling**: Automatically identifies `.tdm` and `.TDM` files, regardless of case.
- **Dynamic Folder Selection**: Option to select a folder containing `.tdm` files or use the current working directory.
- **Progress Tracking**: Displays a progress bar while converting files.

## Requirements

- **File Structure**: `.tdm` (or `.TDM`) files must be in the same folder as their corresponding `.tdx` files.
- Python 3.x
- Required Python packages:
  - `pandas`
  - `numpy`
  - `tdm_loader`
  - `tqdm`
  - `tkinter` (default in most Python distributions)

## How to Use

### 1. Setup
Ensure all the `.tdm` files you want to convert, along with their corresponding `.tdx` files, are in the current working directory or a specific folder.

### 2. Run the Script
Execute the script using Python:

```bash
python tdm_to_csv_converter.py
```

### 3. Folder Selection
- **Option 1**: Select a folder:
  - When prompted with `Do you want to select a folder containing .tdm files? (y/n):`, type `y` and press Enter.
  - A dialog will open allowing you to select the folder containing `.tdm` files.
- **Option 2**: Use the current directory:
  - Type `n` when prompted, and the script will process files in the current working directory.

### 4. View Progress
A progress bar will display the conversion progress for each `.tdm` file.

### 5. Output
- The script generates `.csv` files in the same folder as their corresponding `.tdm` files.
- The `.csv` file will include:
  - **All channel data** from the `.tdm` file.
  - A **time column** (`time`) with values calculated as $\( \text{index} \times \frac{1}{\text{fs}} \)$.

### Example `.csv` Output
If `Test.tdm` contains three channels (`Channel1`, `Channel2`, `Channel3`), the output file `Test.csv` will look like:

| time (s) | Channel1 | Channel2 | Channel3 |
|----------|----------|----------|----------|
| 0.000    | 0.5      | 1.2      | 2.3      |
| 0.001    | 0.6      | 1.3      | 2.4      |
| ...      | ...      | ...      | ...      |
