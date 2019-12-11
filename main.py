import pandas
import matplotlib.pyplot as plt
from collections import Counter
from dynamic import *
from frequency import *
from caesar import *




text = "abc"
print(percentage(text))

#print(frequency(text))
#rot = 2
#inc_int = 1
#print("Normal tekst: " + text)
#print("Dynamisk tekst: " + dynamic(text, rot, inc_int))
#print("Dynamisk tekst 2 tilbage: " + dynamic(dynamic(dynamic(text, 2, 1), 2, 1), -4, -2))