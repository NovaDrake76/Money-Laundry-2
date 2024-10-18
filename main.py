import pyautogui
import time

class RouletteBot:
    def __init__(self):
        # Locate images with a confidence level
        self.betButton = pyautogui.locateOnScreen('images/betButton.png', confidence=0.8)
        self.redButton =  pyautogui.locateOnScreen('images/redButton.png', confidence=0.8)
        self.blackButton =  pyautogui.locateOnScreen('images/blackButton.png', confidence=0.8)
        self.resetButton = pyautogui.locateOnScreen('images/resetButton.png', confidence=0.8)
        self.doubleButton = pyautogui.locateOnScreen('images/doubleButton.png', confidence=0.8)

        self.wasGreen = False
        self.isProfit0 = True
        self.isFirstBet = True

        time.sleep(2)
        pyautogui.click(self.resetButton)

    def placeBets(self):
        #pyautogui.click(self.resetButton)
        print('Placing bets...')
        pyautogui.click(self.redButton)
        pyautogui.click(self.blackButton)

    def bet(self):
        pyautogui.click(self.betButton)
        time.sleep(0.4)

    def checkIsProfit0(self):
        try:
            isProfit0 = pyautogui.locateOnScreen('images/isProfit0.png', confidence=0.9)
            return isProfit0 is not None
        except pyautogui.ImageNotFoundException:
            return False
    
    def martingaling(self, isFirstMartingale):
        while not self.checkIsProfit0():
            if isFirstMartingale:
                pyautogui.click(self.resetButton)
                pyautogui.click(self.redButton)
                isFirstMartingale = False
            
            print('Martingaling...')
            pyautogui.click(self.doubleButton)
            self.bet()
            
            if self.checkIsProfit0():
                print('Profit is 0! martingale is no more needed.')
                pyautogui.click(self.resetButton)
                isFirstMartingale = True
                self.isFirstBet = True
                break
            else:
                print('Martingale failed! Restarting...')

    def main(self):
        isFirstMartingale = True
        print('Starting...')

        if self.isFirstBet:
            self.placeBets()
            self.isFirstBet = False

        self.bet()

        if not self.checkIsProfit0():
            isFirstMartingale = True
            pyautogui.click(self.resetButton)
            self.martingaling(isFirstMartingale)

    def run(self):
        while True:
            self.main()

if __name__ == "__main__":
    bot = RouletteBot()

    bot.run()