# Day 14: Docking Data

[*Link to Original Problem*](https://adventofcode.com/2020/day/14)

## Explaination

### Part One

Given the bitmask rule,

- `0` or `1` changed the bit to that value
- `X` keep the current bit

So given the mask,

- To change the bit to `0`, all `X` bits change to `1` and apply an `AND (&)`
  bitmask, where the bit with the mask set to `1` keep the previous bit while
  the bit with the mask set to `0` sets to `0`.
- To change the bit to `1`, all `X` bits change to `0` and apply an `OR (|)`
  bitmask, where the bit with the mask set to `0` keep the previous bit while
  the bit with the mask set to `1` sets to `1`.

The bitmask operation itself is ![O1] for time and space complexity, and the entire run is ![ON] for time and space complexity where ![N] is the number of lines.

### Part Two

Given the bitmask rule,

- `0` keeps the current bit
- `1` sets the current bit to `1`
- `X` is marked as _floating_, changing to all possible value.

So given the mask,

- To change the bit to `1`, all `X` bits change to `0` and apply an `OR (|)`
  bitmask, where the bit with the mask set to `0` keep the previous bit while
  the bit with the mask set to `1` sets to `1`.
- For utilizing `X` bits, they first have to be set to `0`, first by setting all
  `0` bits to `1` and setting `X` bits to `0`. Apply an `AND (&)` bitmask -
  after applying the changes with `1` bits - so all other bits kept unchanged
  with mask set to `1` while bit with mask set to `0` sets to `0`.
- Also for the `X` bits, make a list of integer where the one bit was set to
  `X`. Using that, generate the [Power set][Power Set] of the possible bits to
  add to the original address (after the `1` and `X` bitmasking) and set the
  value to all the possible addresses.

The initial bitmask is still ![O1] time and space complexity, but when generating all possible values, the time complexity goes to ![O2B] where ![B] is the number of bits set to `X`. However, the mask are only average around 5 to 6 bits (32 - 64 permutations) and even the worst possible case is only up to 9 bits (512 permutations), so one could infer that to be ![O1] for time if it's sufficiently small enough.

With that in mind, the entire run is ![ON] for time and space complexity where ![N] is the number of lines.

## Time + Space Complexity

(Where ![N] is number of lines)

Part | Time Complexity | Space Complexity
---- | --------------- | ----------------
One  | ![ON]          | ![ON]
Two  | ![ON]          | ![ON]


<!-- MARKDOWN LINKS -->
[Power Set]: https://en.wikipedia.org/wiki/Power_set

<!-- MARKDOWN IMAGE LINKS -->
[N]: ./img/N.png
[B]: ./img/B.png
[O1]: ./img/O1.png
[ON]: ./img/ON.png
[O2B]: ./img/O2B.png
