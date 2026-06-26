class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        l=[]
        l.append(Kelvin)
        l.append(Fahrenheit)
        return l