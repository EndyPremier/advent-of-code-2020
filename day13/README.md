# Day 13: Shuttle Search

[*Link to Original Problem*](https://adventofcode.com/2020/day/13)

## Explaination

Consider for each bus ID ![Bi] depart at time ![t] where ![t] is divisible to
![Bi].

### Part One

Finding the ID of earliest bus requires finding the time to arrival. Given the
current time ![t] and a bus ID ![B]:

1. Time since last departure:
   > ![EQ1]

2. Time to next departure (after ![t]):
   > ![EQ2]

3. Time to next departure (at ![t]):
   > ![EQ3]

Finding the min time and the bus ID just require comparing all times and keeping
track of the min time and the current bus ID with that time. Thus time time and
space complexity be at both ![O(B)].

### Part Two

In mathematical definition, there must exist the earliest time time ![t] where
all buses ![B] which for each bus ![Bi] with offset ![Oi] arrive at time
![t+Oi].

> ![EQ4]

The first pattern is to stick to one of the bus ID ![Bi] and its offset time
![Oi], limiting ![T] to just all possible time where ![t+Oi] is divisible to
![Bi].

Loop from time ![t] by incrementing by ![Bi]. If there is a time in ![T] where a
bus ![Bj] - where ![j] is not ![i] - arrive at ![t+Oj], find the least common
multiple (LCM) between ![Bi] and ![Bj] and use that value to increment ![t]
guarenteeing that ![t] meet the condition of those two buses. With any new
buses, find the LCM between the curent increment and the new buses and the
incrementation will grow exponentially (![O(B)] where ![B] is the number of
buses).

The time complexity of the LCM of a group of number is predicated on the time
complexity of the greatest common denominator (GCD), which using the [Euclidean
algorithm][Euclidean Algorithm] is ![O(log n)] (where ![n] is the sum of input
![a] and ![b]). Reducing to finding the LCM of all numbers retains to ![O(log
n)] applying ![log log n] is equivalent to ![log n].

Thus, the time complexity in the nested LCM to find common time ![t] is![O(log
B)] where ![B] is the number of buses, and the time complexity retains to be
![O(B)] as it retains the amount of buses.

## Time + Space Complexity

(Where ![B] is number of buses)

Part | Time Complexity | Space Complexity
---- | --------------- | ----------------
One  | ![O(B)]         | ![O(B)]
Two  | ![O(log B)]     | ![O(B)]


<!-- MARKDOWN LINKS -->
[Euclidean Algorithm]: https://en.wikipedia.org/wiki/Euclidean_algorithm

<!-- MARKDOWN IMAGE LINKS -->
[a]: https://render.githubusercontent.com/render/math?math=a
[a]: https://render.githubusercontent.com/render/math?math=b
[i]: https://render.githubusercontent.com/render/math?math=i
[j]: https://render.githubusercontent.com/render/math?math=j
[n]: https://render.githubusercontent.com/render/math?math=n
[t]: https://render.githubusercontent.com/render/math?math=t

[T]: https://render.githubusercontent.com/render/math?math=T
[B]: https://render.githubusercontent.com/render/math?math=B
[Bi]: https://render.githubusercontent.com/render/math?math=B_i
[Bj]: https://render.githubusercontent.com/render/math?math=B_j
[Oi]: https://render.githubusercontent.com/render/math?math=O_i

[t+Oi]: https://render.githubusercontent.com/render/math?math=t%2BO_i
[t+Oj]: https://render.githubusercontent.com/render/math?math=t%2BO_j

[O(B)]: https://render.githubusercontent.com/render/math?math=O(B)
[O(log n)]: https://render.githubusercontent.com/render/math?math=O(\log+n)
[O(log B)]: https://render.githubusercontent.com/render/math?math=O(\log+B)
[log n]: https://render.githubusercontent.com/render/math?math=\log+n
[log log n]: https://render.githubusercontent.com/render/math?math=\log+(\log+n)

[EQ1]: https://render.githubusercontent.com/render/math?math=t%20\mod%20B
[EQ2]: https://render.githubusercontent.com/render/math?math=B-t%20\mod%20B
[EQ3]: https://render.githubusercontent.com/render/math?math=(B-t%20\mod%20B)\mod%20B
[EQ4]: https://quicklatex.com/cache3/14/ql_b73a7406533951bb8390cbd68fe82814_l3.png