'''
Simulltaneously Upload Video(s) To 5 Platforms 
(Tiktok, IG, FB, YT, VOOM)
With PreDetermined Time.

'''

from datetime import datetime



class Main:
    def __init__(self) -> None:
        pass
    
    
    @staticmethod
    def input_time() -> None:
        current_time = datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        


    def run(self) -> None:

        
        print('now:', now)
        print('date:', date)
        


if __name__ == '__main__':
    Main().run()