from abc import ABC, abstractmethod

class Sensor(ABC):
    """
    Abstract Base Class that serves as a blueprint contract for all lab sensors.
    """
    def __init__(self, name: str = "Generic"):
        self.name = name

    @abstractmethod
    def get_reading(self):
        """Abstract method that MUST be implemented by child classes."""
        pass

class PHSensor(Sensor):
    """Child class that fulfills the contract for a pH sensor."""
    def __init__(self, name: str):
        super().__init__(name)  

    def get_reading(self):
        """Implements get_reading to fulfill the contract."""
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")


class TempSensor(Sensor):
    """Child class that fulfills the contract for a Temperature sensor."""
    def __init__(self, name: str):
        super().__init__(name)

    def get_reading(self):
        """Implements get_reading to fulfill the contract."""
        print("[Temperature Sensor] Reading: 24.5°C")

if __name__ == "__main__":
    # SUCCESS RUN (Tasks 1–4)
    print("--- Lab Inventory System ---")
    
    ph_probe = PHSensor("Alpha pH Probe")
    temp_probe = TempSensor("Beta Thermocouple")
    
    ph_probe.get_reading()
    temp_probe.get_reading()
    
    print("----------------------------\n")

    # TASK 5: The "Break it" Test ---
    print("Executing Task 5 ('Break it' Test)...")
    
    my_sensor = Sensor("Broken Blueprint")
# Using """ and super()