import pyautogui
from time import sleep

######################################
#  Configure these
######################################

m_line = [110, 165]  # Screen location of topmost RX Field

v_dist = 27  # Space between FIelds vertically
h_dist = 80  # Space between Fields horizontally
max_line = 16  # Number of completely visible fields

scroll_loc = [1035, 560]  # Location Right Above bottom Scroll arrow

######################################
#  End Config
######################################


class code_plug:
    Name = ""
    Frequency = ""
    Duplex = ""
    Offset = ""
    Tone = ""
    rToneFreq = ""
    cToneFreq = ""
    DtcsCode = ""
    DtcsPolarity = ""
    RxDtcsCode = ""
    CrossMode = ""
    Mode = ""
    TStep = ""
    Skip = ""
    Power = ""


plugs = []

with open('chirp.csv', 'r') as f:
    l = f.readline()
    for l in f.readlines():
        tmp = code_plug()
        s = l.split(',')
        tmp.Name = s[1]
        tmp.Frequency = s[2]
        tmp.Duplex = s[3]
        tmp.Offset = s[4]
        tmp.Tone = s[5]
        tmp.rToneFreq = s[6]
        tmp.cToneFreq = s[7]
        tmp.DtcsCode = s[8]
        tmp.DtcsPolarity = s[9]
        tmp.RxDtcsCode = s[10]
        tmp.Mode = s[12]
        tmp.Skip = s[14]
        tmp.Power = s[15]
        tmp.CrossMode = s[11]
        plugs.append(tmp)

sleep(5)  # Give some time to switch to app
ln = m_line
count = 1
reset = m_line[1]
for p in plugs:
    pyautogui.click(ln[0], ln[1], 1)  # RX Freq
    pyautogui.write(p.Frequency)

    if p.Duplex == '+':
        freq = str(float(p.Frequency) + float(p.Offset))
    elif p.Duplex == '-':
        freq = str(float(p.Frequency) - float(p.Offset))
    else:
        freq = p.Frequency
    pyautogui.click(ln[0] + h_dist, ln[1], 1)  # TX Freq
    pyautogui.write(freq)

    pyautogui.click(ln[0] + (h_dist * 9), ln[1], 1)  # Name
    pyautogui.write(p.Name)

    pyautogui.click(ln[0] + (h_dist * 2), ln[1], 1)  # RxTone
    if p.Tone in ['Tone', 'TSQL', 'DTCS', 'Cross']:
        if p.Tone == 'TSQL':
            pyautogui.write(p.cToneFreq)
        elif p.Tone == 'Tone':
            pyautogui.write(p.rToneFreq)
        elif p.Tone == 'DTCS':
            tmp = 'D' + p.DtcsCode + p.DtcsPolarity[:1]
            pyautogui.write(tmp)
        elif p.Tone == 'Cross':
            if p.CrossMode[:4] == "Tone":
                pyautogui.write(p.cToneFreq)
            else:
                tmp = 'D' + p.DtcsCode + p.DtcsPolarity[:1]
                pyautogui.write(tmp)

        pyautogui.click(ln[0] + (h_dist * 3), ln[1], 1)  # TxTone
        if p.Tone == 'TSQL':
            pyautogui.write(p.cToneFreq)
        elif p.Tone == 'Tone':
            pyautogui.write(p.rToneFreq)
        elif p.Tone == 'DTCS':
            tmp = 'D' + p.DtcsCode + p.DtcsPolarity[1:]
            pyautogui.write(tmp)
        elif p.Tone == 'Cross':
            if p.CrossMode[6:] == "Tone":
                pyautogui.write(p.cToneFreq)
            else:
                tmp = 'D' + p.DtcsCode + p.DtcsPolarity[1:]
                pyautogui.write(tmp)

    #  If we are at bottom of screen, scroll and start back at top
    count += 1
    if count > max_line:
        ln[1] = reset
        pyautogui.click(scroll_loc[0], scroll_loc[1])
        count = 1
        sleep(1)
    else:
        ln[1] = ln[1] + v_dist

if __name__ == '__main__':
    pass
