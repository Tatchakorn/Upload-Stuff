'''
Author: Saitako
Description:
Simulltaneously Upload Video(s) To 5 Platforms 
(Tiktok, IG, FB, YT, VOOM)
With PreDetermined Time.
'''

from datetime import datetime
from typing import Tuple
import re

class DateTimeHandler:
    def __init__(self) -> None:
        self.date_pattern = '^[0-9]{2}/[0-9]{2}/[0-9]{4}$'
        self.time_pattern = '^[0-9]{2}:[0-9]{2}$'
    

    def validate_input_date(self, date: str) -> bool:
        return re.match(self.date_pattern, date)
    

    def validate_input_time(self, time: str) -> bool:
        return re.match(self.time_pattern, time)


    @staticmethod
    def get_datetime_now() -> Tuple[str, str]:
        '''return date and time str'''
        current_time = datetime.now()
        time = current_time.strftime("%H:%M")
        date = current_time.strftime("%d/%m/%Y")
        return date, time
    
    
    def input_time(self) -> Tuple[str, str]:
        '''return date and time str'''
        curr_date, curr_time = self.get_datetime_now()
        print('Current Date:', curr_date, curr_time)
        
        while True:
            date = input('input date (dd/mm/yy):')
        
            if date == '':
                date = curr_date
                print('default to:', date)
                break
            else:
                if not self.validate_input_date(date):
                    print('Invalid date format!')
                else:
                    break
            
        while True:
            time = input('input time (hh:mm):')
            if not self.validate_input_time(time):
                print('Invalid time format!')
            else:
                break

        return date, time


class Main:
    def __init__(self) -> None:
        self.dt = DateTimeHandler()
    
    
    def test_timer(self) -> None:
        set_date, set_time = self.dt.input_time()
        
        while True:
            curr_date, curr_time = self.dt.get_datetime_now()
            if (curr_date, curr_time) == (set_date, set_time):
                print('IT IS TIME!')
                break


    def run(self) -> None:
        self.test_timer()


if __name__ == '__main__':
    Main().run()