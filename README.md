# CHIRPtoRT730
Take a CHIRP csv plug and automate entering in RT730 Programming software

## Setup
Install the required python module
```
python pip install pyautogui
```

## Usage
1. Maximize the RT-730 software on screen. This helps with window placement
2. Run `python get_mouse.py` to get a few coordinates to configure the script. (Maybe Optional?)
3. Export your codeplug in CHIRP to a CSV file. Rename the file to `chirp.csv` and place in this programs directory.
4. Run `python CHIRPtoRT730.py` to start creating the new plug. You have 5 seconds to tab back to the RT730 Software before it begins.
5. Wait until complete and review the changes before uploading to radio.
