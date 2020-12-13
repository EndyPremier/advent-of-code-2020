# Day 13: Shuttle Search

[*Link to Original Problem*](https://adventofcode.com/2020/day/13)

## Explaination

Consider for each bus ID _Bi_ depart at time _t_
where _t_ is divisible to _Bi_.

### Part One

Finding the ID of earliest bus requires finding the time to arrival. Given the
current time _t_ and a bus ID _B_:

1. Time since last departure:
   > _t_ mod _B_

2. Time to next departure (after _t_):
   > _B_ - _t_ mod _B_

3. Time to next departure (at _t_):
   > (_B_ - _t_ mod _B_) mod _B_

Finding the min time and the bus ID just require comparing all times and keeping
track of the min time and the current bus ID with that time. Thus time time and
space complexity be at both _O_(_B_).

### Part Two

In mathematical definition, there must exist the earliest time time _t_ where all buses _B_ which for each bus _Bi_ with offset _Oi_ arrive at time _t_ + _Oi_.

> _t_ = min(_t_ | ∀_i_ (_t_ + _Oi_)|_Bi_)

Start with the naive appro

The first pattern is to stick to one of the bus ID _Bi_ and its offset time _Oi_, limiting _T_ to just all possible time where _t_ + _Oi_ is divisible to _Bi_.

Loop from time _t_ by incrementing by _Bi_. If there is a time in _T_ where a bus _Bj_ - where _j_ is not _i_ - arrive at _t_ + _Oj_, find the least common multiple (LCM) between _Bi_ and _Bj_ and use that value to increment _t_ guarenteeing that _t_ meet the condition of those two buses. With any new buses, find the LCM between the curent increment and the new buses and the incrementation will grow exponentially (_O_(_B_) where _B_ is the number of buses).

The time complexity of the LCM of a group of number is predicated on the time complexity of the greatest common denominator (GCD), which using the [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) is _O_(log _n_) (where _n_ is the sum of input _a_ and _b_). Reducing to finding the LCM of all numbers retains to _O_(log _n_) applying log(log _n_ + _n_) is equivalent to log _n_.

Thus, the time complexity in the nested LCM to find common time _t_ is _O_(log _B_) where _B_ is the number of buses, and the time complexity retains to be _O_(_B_) as it retains the amount of buses.

## Time + Space Complexity

(Where _B_ is number of buses)

Part | Time Complexity | Space Complexity
---- | --------------- | ----------------
One  | _O_(_B_)        | _O_(_B_)
Two  | _O_(log _B_)    | _O_(_N_)
