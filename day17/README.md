# Day 17: Conway Cubes

[*Link to Original Problem*](https://adventofcode.com/2020/day/17)

## Explaination

Given the multi-dimensional and boundless version of [the famous cellular
automaton][Conway's Game of Life], it would make complete sense assume the
possible permutation to be rather sparse and only checking neighbors by looking
at existing active cubes, and thus, it makes sense to use a sparse hash set to
list active cubes.

> _Note:_ Python gives a lot of leeway in the use of [sets][Python Set] and
> [tuples][Python Tuple] (immutable fixed-length list) as tuples in any length
> are hashable and thus can be put in a (hash) set.
>
> If the use of tuples are restricted, then creating a hashable notation might
> require having some sort of restricted boundary (say 15 units per dimension
> for the 6 cycle from a 3 by 3 slice start) and define the hash from those
> index. For example, given position an ![nt]-tuple, ![P]:
>
> ![EQ0]

The first function is to check on existing neighbors, which requires a way to check all possible neighbors ![N] of a given point of ![nt]-tuple ![P]. This approach utilize an iterable [Cartesian product] of each dimension within a 1 unit distance of the position:

> ![EQ1]

(This is defined generally as the rule stay the same from going from 3-dimensions in part 1 to 4-dimensions in part 2, and it can extend to n-dimensions for generalization.)

This is done for all active points ![A] while also making sure those neighbors are not part of the existing active points in order to get all neighboring points ![I].

> ![EQ2]

For an active cube to stay active, there must have either two or three active neighbors. For inactive cube to become active, there must have exactly three active neighbors.

![Akeep] is the set of all active cubes to continue to be active while ![Anew] is the set of inactive cubes becoming active. ![Anext] is the union of those two to be active on the next step.

> ![EQ3]


<!-- MARKDOWN LINKS -->
[Conway's Game of Life]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
[Python Set]: https://realpython.com/python-sets/
[Python Tuple]: https://realpython.com/python-lists-tuples/#python-tuples
[Cartesian Product]: https://en.wikipedia.org/wiki/Cartesian_product

<!-- MARKDOWN IMAGE LINKS -->
[nt]: ./img/nt.png
[A]: ./img/A.png
[I]: ./img/I.png
[N]: ./img/N.png
[P]: ./img/P.png
[EQ0]: ./img/EQ0.png
[EQ1]: ./img/EQ1.png
[EQ2]: ./img/EQ2.png
[EQ3]: ./img/EQ3.png
[Akeep]: ./img/Akeep.png
[Anew]: ./img/Anew.png
[Anext]: ./img/Anext.png
