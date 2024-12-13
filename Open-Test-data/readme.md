# TDM File Inspection Notebook

## Overview

This Jupyter Notebook allows the user to inspect `.tdm` files (and their corresponding `.tdx` files) interactively. The user can explore metadata, view time histories of experimental data, and visualize specific channels.

## Features

- **File Selection**:
  - Use a file dialog to select a `.tdm` file interactively.
  - Optionally, specify the file path manually in the notebook.
- **Metadata Display**:
  - Provides information such as the number of channels, channel length, and file path.
- **Data Exploration**:
  - Displays the available channel names.
  - Allows plotting time histories of specific channels.
- **Time-Based Index**:
  - Automatically computes a `time` column as the index, assuming a default sampling frequency of 1000 Hz.

## Requirements

- **Python 3.x**
- Required libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `tkinter` (default in most Python distributions)
  - `tdm_loader`

## How to Use

### 1. Setup
- Ensure your `.tdm` files and corresponding `.tdx` files are in the same directory.

### 2. Run the Notebook
Open the notebook in Jupyter and execute the cells step by step.

### 3. File Selection
- **Interactive Selection**:
  - A file dialog will open, allowing you to select a `.tdm` file.
- **Manual Selection**:
  - Uncomment the line `# tdm_file = path...` in the notebook and specify the full file path.

### 4. Outputs
- **Metadata**:
  - Displays information such as the number of channels, the length of the data, and the file path.
- **Channel Names**:
  - Lists all channel names in the file.
- **Plots**:
  - Plots the time history of the first channel by default.
  - Modify `channel_to_plot` in the notebook to visualize other channels.


