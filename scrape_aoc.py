# trying to find aoc puzzles that talk about chess (in their first part)
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

for year in tqdm(range(2015,2022)):
    for day in range(1,32):
        url = f'https://adventofcode.com/{year}/day/{day}'
        r = requests.get(url).text
        if 'chess' in r.lower():
            print(url)
            
# as of septemebr 2022, this yields: https://adventofcode.com/2016/day/5 where 'chess' is indeed in the title