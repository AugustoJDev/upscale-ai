# Real-ESRGAN Automated Steps With Python

I developed this script to automate the step-by-step improvement of images for a client who worked as a Thumbmaker, because he was tired of manually typing in the prompt he always wanted, as well as always deleting the images in the input folder and opening the output folder, thus speeding up all the work steps. To help even more, I recommend that you use the **PyInstaller** dependency to turn the `main.py` script into an executable, making it even easier to run the script, just as I did for this client.

## What is Real-ESRGAN

Real-ESRGAN aims at developing Practical Algorithms for General Image/Video Restoration. This project uses the technology known as Image Upscaling, improving the quality and size of images, such as 2x, 4x, 8x...

## What functions are in the script

The script has the following functions:
- Call the `.bat` file with the default prompt
- Delete all files that have already been upgraded from the `input` folder
- Open the `output` folder after the process has finished

## How to configure

For users who want to use the script through an executable, I recommend using the [PyInstaller](https://pyinstaller.org/en/stable/) dependency.

### Quickstart

Install **PyInstaller** with the following command:
```bash
pip install pyinstaller
```

To turn the `main.py` script into an executable, use the command below, which also sets the logo.ico icon:
```bash
pyinstaller --onefile --icon=logo.ico main.py
```

Inside the `dist` folder that will be created, you will find the `main.exe` executable. Simply copy it to the desired location and run it!