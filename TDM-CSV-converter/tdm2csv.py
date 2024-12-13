import os
import pandas as pd
import tdm_loader as tdm
import numpy as np
from tqdm import tqdm
from tkinter import Tk, filedialog

"""
This script converts all `.tdm` files in the current directory to `.csv` format.

Features:
- Handles both `.tdm` and `.TDM` file extensions automatically.
- Allows user to select a folder or use the current working directory.
- Adds a time column based on the specified sampling frequency (default is 1000 Hz).
- Displays a progress bar for the conversion process.
"""

def select_folder():
    """
    Opens a dialog for folder selection.

    Returns:
        str: Path to the selected folder.
    """
    # Create Tkinter root window
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    # Open folder selection dialog
    folder_path = filedialog.askdirectory(title="Select Folder Containing .tdm Files")
    # Destroy the root window after dialog is closed
    root.destroy()

    return folder_path


def convert_tdm_to_csv(tdm_filename, fs=1000):
    """
    Converts a .tdm file to a .csv file.

    Args:
        tdm_filename (str): path of .tdm file
    Returns:
        str: .csv filename
    """
    # Load TDM file
    data = tdm.OpenFile(tdm_filename)
    # Initialise a dictionary for the data
    d = {}
    group_index = 0  # first group contains all data
    channel_index = 0  # initialise first channel
    while True:
        try:
            # retrieve channel name and data
            channel_name = data.channel_name(group_index, channel_index)
            channel_data = data.channel(group_index, channel_index)
            d[channel_name] = channel_data
            channel_index += 1  # move to next channel
        except IndexError:
            break

    # Create a DataFrame from the dictionary
    df = pd.DataFrame.from_dict(d)

    # Add a time column and set it as the index
    time = np.array(range(len(df))) * 1 / fs
    df['time'] = time
    df = df.set_index('time')

    # Save the DataFrame as a .csv file
    csv_filename = tdm_filename[:-4] + '.csv'
    df.to_csv(csv_filename, index=True, header=True) # save csv

    return csv_filename


def find_tdm_files(folder_path):
    """
    Finds all .tdm and .TDM files in the specified folder.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        list: List of .tdm and .TDM file paths.
    """
    return [file for file in os.listdir(folder_path) if file.lower().endswith('.tdm')]


def main():

    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Ask for folder selection
    # y - open Tkinter
    # n - use current folder
    user_input = input("Do you want to select a folder containing .tdm files? (y/n): ").strip().lower()

    if user_input == 'y':
        folder_path = select_folder()
        if not folder_path:
            print("No folder selected. Exiting.")
            return
    else:
        folder_path = os.getcwd()

    # Find all .tdm and .TDM files in the folder
    tdm_files = find_tdm_files(folder_path)
    # return if no files are found
    if not tdm_files:
        print("No .tdm or .TDM files found in the selected folder. Exiting.")
        return

    # Progress bar
    progress_bar = tqdm(total=len(tdm_files), desc='Converting files')

    # Convert .tdm file to .csv
    for tdm_file in tdm_files:
        tdm_filepath = os.path.join(folder_path, tdm_file)
        try:
            convert_tdm_to_csv(tdm_filepath)
        except Exception as e:
            print(f"Error converting {tdm_file}: {e}")
        progress_bar.update(1)

    # Close the progress bar
    progress_bar.close()
    print("Conversion process completed.")


if __name__ == "__main__":
    main()
