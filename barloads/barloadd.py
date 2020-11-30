from tqdm import tqdm
from time import sleep

def barloadnew():
    for i in tqdm(range(0, 100), desc ="Text You Want"): 
        sleep(.1) 

barloadnew()
