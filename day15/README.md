# Day 15: Rambunctious Recitation

[*Link to Original Problem*](https://adventofcode.com/2020/day/{##})

## Explaination

Consider part one takes 2,020 turns while part two takes 30,000,000 (thirty
million) turns. Part 2 is almost 15,000x (fifteen thousand times) as big as part
one. Assuming it takes one second to run part one through brute force, it would
probably take __at least__ 4 hours to find the 30,000,000th turn.

```
30,000,000 / 2,000 ≈ 15,000
15,000 sec = 4 hrs 10 min
```

Unfortunately, I was unable to find an optimized solution below ![ON].


## Time + Space Complexity

(Where ![N] is number of turns)

Part | Time Complexity | Space Complexity
---- | --------------- | ----------------
One  | ![ON]           | ![ON]
Two  | ![ON]           | ![ON]


<!-- MARKDOWN LINKS -->


<!-- MARKDOWN IMAGE LINKS -->
[N]: ./img/N.png
[ON]: ./img/ON.png
