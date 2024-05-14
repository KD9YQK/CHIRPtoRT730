# CHIRPtoRT730
Take a CHIRP csv plug and automate entering in RT730 Programming software

## Setup
1. Install the required python module
```
python pip install pyautogui
```
2. Maximize the RT-730 software on screen. This helps with window placement
3. Run `python get_mouse.py` to get a few coordinates to configure the script. (Maybe Optional?)
4. Export your codeplug in CHIRP to a CSV file. Rename the file to `chirp.csv` and place in this programs directory.
5. Run `python CHIRPtoRT730.py` to start creating the new plug. You have 5 seconds to tab back to the RT730 Software before it begins.
6. Wait until complete and review the changes before uploading to radio.
