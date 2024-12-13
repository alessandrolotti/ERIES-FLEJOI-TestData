# Rewriting the README content to a file as the environment was reset
readme_content = """
# TDM to CSV Conversion Script

## Overview

This script automates the process of converting `.tdm` (or `.TDM`) files into `.csv` format. It allows users to select a specific folder or work with the current directory and generates `.csv` files with additional time data for each channel in the `.tdm` files.

## Features

- **File Handling**: Automatically identifies `.tdm` and `.TDM` files, regardless of case.
- **Dynamic Folder Selection**: Option to select a folder containing `.tdm` files or use the current working directory.
- **Progress Tracking**: Displays a progress bar while converting files.
- **Time Column Addition**: Adds a time column based on the sampling frequency (`fs`), defaulting to `1000 Hz`.
- **Error Handling**: Skips files that cannot be processed and provides error messages for debugging.

## Requirements

- Python 3.x
- Required Python packages:
  - `pandas`
  - `numpy`
  - `tdm_loader`
  - `tqdm`
  - `tkinter` (default in most Python distributions)

## How to Use

### 1. Setup
Ensure all the `.tdm` files you want to convert are in the current working directory or a specific folder.

### 2. Run the Script
Execute the script using Python:

```bash
python tdm_to_csv_converter.py
