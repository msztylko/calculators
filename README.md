# calculators

Exploration of interpreters for algebraic expressions. Inspiration came from watching [Brian Harvey’s lecture](https://archive.org/details/ucberkeley_webcast_nzMPF59Ackg) about calculator, as a part of my [SICP reading](https://github.com/msztylko/SICP)

## [Reverse Polish (Postfix) Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

Notation in which operators **follow** their operands e.g. `2 3 +`

More examples available as [tests](./test_calculators.py).

Interpreter for Postfix Notation has a simple implementation with a single stack - push operands onto stack and when you encounter operator, pop 2 operands from the top of the stack and evaluate with a current operator.

## [Polish (Prefix) Notation](https://en.wikipedia.org/wiki/Polish_notation)

Notation in which operators **precede** their operands e.g. `+ 2 3`

More examples available as [tests](./test_calculators.py).

Stack-based implementation of interpreter for Prefix Notation requires two stacks - one for keeping track of operands and another one for operators. When we encounter operand and we already have another operand on stack, we pop it from stack, pop operator from stack and use it to evaluate current two operands.

## [Infix Notation](https://en.wikipedia.org/wiki/Infix_notation)

My initial plan was to re-implement infix calculator with *yacc* and *lex* as I remember reading about it in [The Unix Programming Environment](https://en.wikipedia.org/wiki/The_Unix_Programming_Environment) book. However, this remainded me about a more modern tool, [SLY](https://github.com/dabeaz/sly) which I wanted to try for a long time.
