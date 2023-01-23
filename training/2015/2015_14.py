import re

INPUT="""Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.
"""
# INPUT="""
#     Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
#     Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# """
# after exactly 2503 seconds, what distance has the winning reindeer traveled?

inp = [_ for _ in INPUT.split('\n') if _]
pat = re.compile(r'\d+')
inp = [list(map(int, pat.findall(animal))) for animal in inp]

def distance_after(race_duration: int, speed:int, moving_time:int, still_time:int) -> int:
    """Computes and returns the distance made

    Args:
        race_duration (int): _description_
        speed (int): _description_
        moving_time (int): _description_
        still_time (int): _description_

    Raises:
        ValueError: _description_

    Returns:
        int: _description_
    """
    if not isinstance(race_duration, int) or race_duration < 0:
        raise ValueError('race duration should be a positive integer')
    if race_duration <= moving_time:
        speed * race_duration
    nb_full_blocks = race_duration // (moving_time+still_time)
    return nb_full_blocks * speed * moving_time + min(moving_time, race_duration - nb_full_blocks*(moving_time+still_time)) * speed

#print(max(distance_after(2_503, *elem) for elem in inp))

# part 2
# at the end of each second, he awards one point to the reindeer currently in the lead. 
# (If there are multiple reindeer tied for the lead, they each get one point.)

# let's try the naïve approach; we'll look to optimize only of it's too costly
scores = [0]*len(inp)
for sec in range(1, 2_504):
    distances = [distance_after(sec, *elem) for elem in inp]
    m = max(distances)
    for idx in [i for i in range(len(distances)) if distances[i]==m]:#(distances.index(elem) for elem in distances if elem == m):
        scores[idx] += 1

print(max(scores))
        


    