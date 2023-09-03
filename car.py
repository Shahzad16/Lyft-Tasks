from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

    @abstractmethod
    def engine_should_be_serviced(self):
        pass

    @abstractmethod
    def battery_should_be_serviced(self):
        pass