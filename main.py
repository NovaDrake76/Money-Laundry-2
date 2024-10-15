import pyautogui
import time

# Add a delay to ensure the screen is fully loaded
time.sleep(2)

# Locate images with a confidence level
betButton = pyautogui.locateOnScreen('images/betButton.png', confidence=0.8)
redButton = 1160, 715
blackButton = 1260, 715
resetButton = pyautogui.locateOnScreen('images/resetButton.png', confidence=0.8)
doubleButton = pyautogui.locateOnScreen('images/doubleButton.png', confidence=0.8)

wasGreen = False
isProfit0 = True

def placeBets():
    pyautogui.click(resetButton)
    print('Placing bets...')
    pyautogui.click(redButton)
    pyautogui.click(blackButton)
    pyautogui.click(betButton)
    time.sleep(1)


def checkIsProfit0():
    try:
        isProfit0 = pyautogui.locateOnScreen('images/isProfit0.png', confidence=0.9)
        if isProfit0:
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        return False

def martingaling():
    if checkIsProfit0():
        print('Profit is 0! martingale is no more needed.')
        pyautogui.click(resetButton)
        main()
        return
    
    print('Martingaling...')
    pyautogui.click(doubleButton)
    pyautogui.click(betButton)

    time.sleep(1)

    if not checkIsProfit0():
        martingaling()
    else:
        main()

def main():
    print('Starting...')
    placeBets()
    pyautogui.click(resetButton)
    pyautogui.click(redButton)
    martingaling()
    time.sleep(1) 
    
if __name__ == "__main__":
    main()