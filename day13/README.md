# Day 13: Shuttle Search

[*Link to Original Problem*](https://adventofcode.com/2020/day/13)

## Explaination

Consider for each bus ID ![Bi] depart at time ![t] where ![t] is divisible to
![Bi].

### Part One

Finding the ID of earliest bus requires finding the time to arrival. Given the
current time ![t] and a bus ID ![capB]:

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
all buses ![capB] which for each bus ![Bi] with offset ![Oi] arrive at time
![t+Oi].

> ![EQ4]

The first pattern is to stick to one of the bus ID ![Bi] and its offset time
![Oi], limiting ![capT] to just all possible time where ![t+Oi] is divisible to
![Bi].

Loop from time ![t] by incrementing by ![Bi]. If there is a time in ![capT] where a
bus ![Bj] - where ![j neq i] - arrive at ![t+Oj], find the least common
multiple (LCM) between ![Bi] and ![Bj] and use that value to increment ![t]
guarenteeing that ![t] meet the condition of those two buses. With any new
buses, find the LCM between the curent increment and the new buses and the
incrementation will grow exponentially (![O(B)] where ![capB] is the number of
buses).

The time complexity of the LCM of a group of number is predicated on the time
complexity of the greatest common denominator (GCD), which using the [Euclidean
algorithm][Euclidean Algorithm] is ![O(log n)] (where ![nab]). Reducing to finding the LCM of all numbers retains to ![O(log
n)] applying ![log log n] is equivalent to ![log n].

Thus, the time complexity in the nested LCM to find common time ![t] is![O(log
B)] where ![capB] is the number of buses, and the time complexity retains to be
![O(B)] as it retains the amount of buses.

## Time + Space Complexity

(Where ![capB] is number of buses)

Part | Time Complexity | Space Complexity
---- | --------------- | ----------------
One  | ![O(B)]         | ![O(B)]
Two  | ![O(log B)]     | ![O(B)]


<!-- MARKDOWN LINKS -->
[Euclidean Algorithm]: https://en.wikipedia.org/wiki/Euclidean_algorithm

<!-- MARKDOWN IMAGE LINKS -->
[t]: ./img/t.png
[capT]: ./img/capT.png
[capB]: ./img/capB.png
[Bi]: ./img/Bi.png
[Bj]: ./img/Bj.png
[Oi]: ./img/Oi.png

[t+Oi]: ./img/tOi.png
[t+Oj]: ./img/tOj.png
[j neq i]: ./img/jneqi.png
[nab]: ./img/nab.png

[O(B)]: ./img/OB.png
[O(log n)]: ./img/Ologn.png
[O(log B)]: ./img/OlogB.png
[log n]: ./img/logn.png
[log log n]: ./img/loglogn.png

[EQ1]: ./img/EQ1.png
[EQ2]: ./img/EQ2.png
[EQ3]: ./img/EQ3.png
[EQ4]: ./img/EQ4.png