from tqdm import tqdm
def barload():
    for i in tqdm(range(int(9e6)), ascii = True, desc = "Loading.."):
        pass
