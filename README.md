# Dread Startup Sound Randomizer

This simple Python script plays a random `.wav` sound from a specified directory when your computer starts up.

## Features

- Randomly selects a `.wav` file from a designated folder.
- Easy to set up and customize.

## Requirements

- **Operating System:** Windows
- **Python:** 3.x

This script uses the `winsound` module, which is part of the standard Python library for Windows.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/dread-startup-sound.git
    cd dread-startup-sound
    ```

2.  **Add your sound files:**
    - Place your desired `.wav` sound files into the `sounds` directory.

3.  **Run the script (optional):**
    - To test the script, you can run it directly from your terminal:
      ```bash
      python dread_startup.py
      ```

## How to Use

To have this script run on startup, you can place a shortcut to it in the Windows Startup folder.

1.  Press `Win + R` to open the Run dialog.
2.  Type `shell:startup` and press Enter. This will open the Startup folder.
3.  Right-click in the Startup folder, select `New` > `Shortcut`.
4.  Browse to the location of `dread_startup.py` and select it.
5.  Click `Next` and then `Finish`.

Now, every time you start your computer, a random sound from the `sounds` folder will play.

## Notes

- If no `.wav` files are found in the `sounds` directory, the script will do nothing.
- This script is for Windows only and will not work on macOS or Linux.
