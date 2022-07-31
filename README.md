# calculators

Exploration of interpreters for algebraic expressions. Inspiration came from watching [Brian Harvey’s lecture](https://archive.org/details/ucberkeley_webcast_nzMPF59Ackg) about calculator, as a part of my [SICP reading](https://github.com/msztylko/SICP)

## [Reverse Polish (Postfix) Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

Notation in which operators **follow** their operands e.g. `2 3 +`

More examples available as [tests](./test_calculators.py).

Interpreter for Postfix Notation has a simple implementaion with a single stack - push operands onto stack and when you encounter operator, pop 2 operands from the top of the stack and evaluate with a current operator.

## [Polish (Prefix) Notation](https://en.wikipedia.org/wiki/Polish_notation)

Notation in which operators **precede** their operands e.g. `+ 2 3`

More examples available as [tests](./test_calculators.py).

