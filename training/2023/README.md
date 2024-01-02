see Makefile for day file creation boilerplate, example command: Created py file and input file for day 3

IMPORTANT NOTE: on Jan 2nd 2024, I checked out Peter Norvig's solutions in pytudes: https://github.com/norvig/pytudes/blob/42f497d097c6d4752c6e50e4c4649f3e40113dd0/ipynb/Advent-2023.ipynb

I saw he had bugs on day 17 part 2 and day 23 part 2 and wanted to see if I'd be able to debug.

- day 17 part 2: his code worked on my input, and because he did not share his input (as per AoC request), I could not start debugging
- day 23 part 2: more interesting as his initial solution worked on the example input but did not scale to his actual input, and his subsequent optimization was wrong on both his input and the example input. After some research I found out he had an unwanted "+ 1" in the returned value of his final `dfs` function, the one nested inside the `max_cost_graph_path` function

Because I myself had not solved those puzzles (none from day 17 and only part 1 from day 23), this means I can still try and code myself solutions to these puzzles in a bit of time when I've forgotten the details of his implem.