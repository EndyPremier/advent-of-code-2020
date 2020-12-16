# Day 16: Ticket Translation

[*Link to Original Problem*](https://adventofcode.com/2020/day/16)

## Explaination

The first section of the puzzle input is a list of rules in terms of two ranges,
and there is only one unambiguous order of those rules for every ticket.

### Part One

This part only filters out only values that are not part of _any_ ranges. Checking if a value is not in those ranges has a time complexity of ![OR] where ![R] is the number of rules, and the space complexity is ![O1] as there are no use of additional space. Checking and summing specific values is in a time complexity of ![OTR] where ![T] is the number of tickets, and the space complexity is ![O1] as there are no use of additional space.

### Part Two

The first part is to filter all possible rules to rules that are valid for all tickets in the specific field. This process is initialized with a time and space complexity of ![OR2]. Filtering specific rules for each ticket down the line requires getting the current ticket's possibile rules (also ![OR2]) and doing an intersect against the previous valid rules (![OR], time and space). After going through all of the tickets, the time complexity is ![OTR2] - where ![T] is the number of tickets - as adding tickets is constant, but adding rules is quadratic.

After getting the possibilities, those possibilities are normalized where included in the possibilities are fields with only one possibility, meaning the field is unambiguous and that means all other fields shouldn't have that rule since only one rule can fit with one field. With removing those possibilities off of ambiguous field, one of them becomes unambiguous with their own rule, and this continues on until there are no more ambiguities. While this process doesn't require additional space (![O1]), this has the upfront time complexity of ![OR2], checking all ![R] rules ![R] times for each unambiguous rules.

Overall, the time complexity reaches to ![OTR2] and the space complexity is ![OR2].

## Time + Space Complexity

(Where ![R] is number of rules and ![T] is the number of tickets)

Part | Time Complexity | Space Complexity
---- | --------------- | ----------------
One  | ![OTR]          | ![O1]
Two  | ![OTR2]         | ![OR2]


<!-- MARKDOWN IMAGE LINKS -->
[R]: ./img/R.png
[T]: ./img/T.png
[O1]: ./img/O1.png
[OR]: ./img/OR.png
[OR2]: ./img/OR2.png
[OTR]: ./img/OTR.png
[OTR2]: ./img/OTR2.png
