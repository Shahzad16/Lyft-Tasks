from datetime import datetime
from car import Car
from engine.sternman_engine import SternmanEngine

class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.engine = SternmanEngine(warning_light_is_on)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine.engine_should_be_serviced():
            return True
        else:
            return False
