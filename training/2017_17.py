"""My solution to AoC 2017 day 17"""
from tqdm import tqdm


class Spinlock:
    def __init__(self, steps: int) -> None:
        self.steps = steps
        self.buffer = [0]
        self.ind = 0
        self.insertion_val = 1

    def move(self) -> None:
        self.ind = (self.ind + self.steps) % len(self.buffer) + 1
        self.buffer.insert(self.ind, self.insertion_val)
        self.insertion_val += 1


if __name__ == "__main__":
    sl = Spinlock(377)
    for _ in range(2017):
        sl.move()
    ind = sl.buffer.index(2017)
    answer = sl.buffer[ind + 1]  # assuming 2017 does not come last in the buffer list
    print(answer)

# part 2
# let's avoid manipulating a list and inserting elements and simplify the simulation
ind = 0
len_buffer = 1
steps = 377
val = 1
answer = 0
for _ in tqdm(range(50_000_000)):
    ind = (ind + steps) % len_buffer + 1
    if ind - 1 == 0:
        answer = val
    len_buffer += 1
    val += 1
    
print(answer)
