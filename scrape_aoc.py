# trying to find aoc puzzles that talk about chess (in their first part)
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

links = []
# for year in tqdm(range(2015,2022)):
#     for day in range(1,26):
#         url = f'https://adventofcode.com/{year}/day/{day}'
#         r = requests.get(url).text
#         links.append((url, len(r)))
#     print(f'current shortest: {sorted(links, key=lambda x: x[1])[:10]}')
            
# # as of septemebr 2022, searching 'chess' yields: https://adventofcode.com/2016/day/5 where 'chess' is indeed in the title

# print(sorted(links, key=lambda x: x[1])[:10])
# print('\n'*3, links)

results = [('https://adventofcode.com/2015/day/1', 5213), ('https://adventofcode.com/2015/day/2', 4854), ('https://adventofcode.com/2015/day/3', 4628), ('https://adventofcode.com/2015/day/4', 4814), ('https://adventofcode.com/2015/day/5', 4966), ('https://adventofcode.com/2015/day/6', 5075), ('https://adventofcode.com/2015/day/7', 6369), ('https://adventofcode.com/2015/day/8', 6122), ('https://adventofcode.com/2015/day/9', 4582), ('https://adventofcode.com/2015/day/10', 4887), ('https://adventofcode.com/2015/day/11', 5846), ('https://adventofcode.com/2015/day/12', 4595), ('https://adventofcode.com/2015/day/13', 6036), ('https://adventofcode.com/2015/day/14', 5047), ('https://adventofcode.com/2015/day/15', 5920), ('https://adventofcode.com/2015/day/16', 5775), ('https://adventofcode.com/2015/day/17', 4394), ('https://adventofcode.com/2015/day/18', 5882), ('https://adventofcode.com/2015/day/19', 5812), ('https://adventofcode.com/2015/day/20', 5378), ('https://adventofcode.com/2015/day/21', 6916), ('https://adventofcode.com/2015/day/22', 9182), ('https://adventofcode.com/2015/day/23', 6040), ('https://adventofcode.com/2015/day/24', 6762), ('https://adventofcode.com/2015/day/25', 7220), ('https://adventofcode.com/2016/day/1', 5811), ('https://adventofcode.com/2016/day/2', 5835), ('https://adventofcode.com/2016/day/3', 4690), ('https://adventofcode.com/2016/day/4', 5156), ('https://adventofcode.com/2016/day/5', 5491), ('https://adventofcode.com/2016/day/6', 4966), ('https://adventofcode.com/2016/day/7', 5314), ('https://adventofcode.com/2016/day/8', 6729), ('https://adventofcode.com/2016/day/9', 6112), ('https://adventofcode.com/2016/day/10', 6281), ('https://adventofcode.com/2016/day/11', 10611), ('https://adventofcode.com/2016/day/12', 6714), ('https://adventofcode.com/2016/day/13', 6262), ('https://adventofcode.com/2016/day/14', 6625), ('https://adventofcode.com/2016/day/15', 7029), ('https://adventofcode.com/2016/day/16', 8279), ('https://adventofcode.com/2016/day/17', 7258), ('https://adventofcode.com/2016/day/18', 7577), ('https://adventofcode.com/2016/day/19', 5298), ('https://adventofcode.com/2016/day/20', 5294), ('https://adventofcode.com/2016/day/21', 7882), ('https://adventofcode.com/2016/day/22', 5798), ('https://adventofcode.com/2016/day/23', 7422), ('https://adventofcode.com/2016/day/24', 6025), ('https://adventofcode.com/2016/day/25', 6486), ('https://adventofcode.com/2017/day/1', 6500), ('https://adventofcode.com/2017/day/2', 5016), ('https://adventofcode.com/2017/day/3', 5353), ('https://adventofcode.com/2017/day/4', 4580), ('https://adventofcode.com/2017/day/5', 6216), ('https://adventofcode.com/2017/day/6', 6620), ('https://adventofcode.com/2017/day/7', 6371), ('https://adventofcode.com/2017/day/8', 5677), ('https://adventofcode.com/2017/day/9', 8139), ('https://adventofcode.com/2017/day/10', 8381), ('https://adventofcode.com/2017/day/11', 5100), ('https://adventofcode.com/2017/day/12', 6105), ('https://adventofcode.com/2017/day/13', 9875), ('https://adventofcode.com/2017/day/14', 6370), ('https://adventofcode.com/2017/day/15', 6224), ('https://adventofcode.com/2017/day/16', 5595), ('https://adventofcode.com/2017/day/17', 7505), ('https://adventofcode.com/2017/day/18', 7774), ('https://adventofcode.com/2017/day/19', 5767), ('https://adventofcode.com/2017/day/20', 7191), ('https://adventofcode.com/2017/day/21', 7313), ('https://adventofcode.com/2017/day/22', 8356), ('https://adventofcode.com/2017/day/23', 5556), ('https://adventofcode.com/2017/day/24', 6495), ('https://adventofcode.com/2017/day/25', 8184), ('https://adventofcode.com/2018/day/1', 6816), ('https://adventofcode.com/2018/day/2', 6638), ('https://adventofcode.com/2018/day/3', 6428), ('https://adventofcode.com/2018/day/4', 8144), ('https://adventofcode.com/2018/day/5', 6053), ('https://adventofcode.com/2018/day/6', 6472), ('https://adventofcode.com/2018/day/7', 7278), ('https://adventofcode.com/2018/day/8', 6399), ('https://adventofcode.com/2018/day/9', 8521), ('https://adventofcode.com/2018/day/10', 9051), ('https://adventofcode.com/2018/day/11', 7716), ('https://adventofcode.com/2018/day/12', 9081), ('https://adventofcode.com/2018/day/13', 8872), ('https://adventofcode.com/2018/day/14', 7899), ('https://adventofcode.com/2018/day/15', 16459), ('https://adventofcode.com/2018/day/16', 11717), ('https://adventofcode.com/2018/day/17', 9703), ('https://adventofcode.com/2018/day/18', 7732), ('https://adventofcode.com/2018/day/19', 9879), ('https://adventofcode.com/2018/day/20', 11260), ('https://adventofcode.com/2018/day/21', 6448), ('https://adventofcode.com/2018/day/22', 10151), ('https://adventofcode.com/2018/day/23', 7309), ('https://adventofcode.com/2018/day/24', 13403), ('https://adventofcode.com/2018/day/25', 8254), ('https://adventofcode.com/2019/day/1', 5759), ('https://adventofcode.com/2019/day/2', 9071), ('https://adventofcode.com/2019/day/3', 6149), ('https://adventofcode.com/2019/day/4', 5078), ('https://adventofcode.com/2019/day/5', 9363), ('https://adventofcode.com/2019/day/6', 7022), ('https://adventofcode.com/2019/day/7', 8593), ('https://adventofcode.com/2019/day/8', 6055), ('https://adventofcode.com/2019/day/9', 7653), ('https://adventofcode.com/2019/day/10', 7916), ('https://adventofcode.com/2019/day/11', 8148), ('https://adventofcode.com/2019/day/12', 14264), ('https://adventofcode.com/2019/day/13', 5783), ('https://adventofcode.com/2019/day/14', 9273), ('https://adventofcode.com/2019/day/15', 7823), ('https://adventofcode.com/2019/day/16', 9200), ('https://adventofcode.com/2019/day/17', 7897), ('https://adventofcode.com/2019/day/18', 8234), ('https://adventofcode.com/2019/day/19', 5900), ('https://adventofcode.com/2019/day/20', 8170), ('https://adventofcode.com/2019/day/21', 9351), ('https://adventofcode.com/2019/day/22', 9633), ('https://adventofcode.com/2019/day/23', 6774), ('https://adventofcode.com/2019/day/24', 6601), ('https://adventofcode.com/2019/day/25', 6309), ('https://adventofcode.com/2020/day/1', 5662), ('https://adventofcode.com/2020/day/2', 5676), ('https://adventofcode.com/2020/day/3', 7595), ('https://adventofcode.com/2020/day/4', 6513), ('https://adventofcode.com/2020/day/5', 7947), ('https://adventofcode.com/2020/day/6', 6522), ('https://adventofcode.com/2020/day/7', 6473), ('https://adventofcode.com/2020/day/8', 7114), ('https://adventofcode.com/2020/day/9', 6875), ('https://adventofcode.com/2020/day/10', 8432), ('https://adventofcode.com/2020/day/11', 6901), ('https://adventofcode.com/2020/day/12', 6923), ('https://adventofcode.com/2020/day/13', 7483), ('https://adventofcode.com/2020/day/14', 7634), ('https://adventofcode.com/2020/day/15', 8157), ('https://adventofcode.com/2020/day/16', 7582), ('https://adventofcode.com/2020/day/17', 7562), ('https://adventofcode.com/2020/day/18', 6420), ('https://adventofcode.com/2020/day/19', 8251), ('https://adventofcode.com/2020/day/20', 8318), ('https://adventofcode.com/2020/day/21', 6476), ('https://adventofcode.com/2020/day/22', 7355), ('https://adventofcode.com/2020/day/23', 7532), ('https://adventofcode.com/2020/day/24', 7020), ('https://adventofcode.com/2020/day/25', 8803), ('https://adventofcode.com/2021/day/1', 6623), ('https://adventofcode.com/2021/day/2', 6021), ('https://adventofcode.com/2021/day/3', 6321), ('https://adventofcode.com/2021/day/4', 8096), ('https://adventofcode.com/2021/day/5', 6238), ('https://adventofcode.com/2021/day/6', 7685), ('https://adventofcode.com/2021/day/7', 6561), ('https://adventofcode.com/2021/day/8', 10449), ('https://adventofcode.com/2021/day/9', 5970), ('https://adventofcode.com/2021/day/10', 8341), ('https://adventofcode.com/2021/day/11', 10854), ('https://adventofcode.com/2021/day/12', 7349), ('https://adventofcode.com/2021/day/13', 8009), ('https://adventofcode.com/2021/day/14', 7335), ('https://adventofcode.com/2021/day/15', 5922), ('https://adventofcode.com/2021/day/16', 12427), ('https://adventofcode.com/2021/day/17', 11110), ('https://adventofcode.com/2021/day/18', 13151), ('https://adventofcode.com/2021/day/19', 12874), ('https://adventofcode.com/2021/day/20', 9413), ('https://adventofcode.com/2021/day/21', 8412), ('https://adventofcode.com/2021/day/22', 8822), ('https://adventofcode.com/2021/day/23', 8791), ('https://adventofcode.com/2021/day/24', 9754), ('https://adventofcode.com/2021/day/25', 11207)]
for e in sorted(results, key = lambda x: x[1]):
    if not '/2015/' in e[0] and e[1]<6_000:
        print(e)
    
    