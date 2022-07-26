# calculators

<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/39266310/182230990-6ce4cb70-0764-464c-8172-ca4354028ce6.png">
</p>

Exploration of interpreters for algebraic expressions. 
Inspiration came from watching [Brian Harvey’s lecture](https://archive.org/details/ucberkeley_webcast_nzMPF59Ackg) about calculator, 
as a part of my [SICP reading](https://github.com/msztylko/SICP)

## [Reverse Polish (Postfix) Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

Notation in which operators **follow** their operands e.g. `2 3 +`

More examples available as [tests](./test_calculators.py).

Interpreter for Postfix Notation has a simple implementation with a single stack
\- push operands onto stack and when you encounter operator, 
pop 2 operands from the top of the stack and evaluate with a current operator.

## [Polish (Prefix) Notation](https://en.wikipedia.org/wiki/Polish_notation)

Notation in which operators **precede** their operands e.g. `+ 2 3`

More examples available as [tests](./test_calculators.py).

Stack-based implementation of interpreter for Prefix Notation requires two stacks 
\- one for keeping track of operands and another one for operators. 
When we encounter operand and we already have another operand on stack, 
we pop it from stack, pop operator from stack and use it to evaluate current two operands.

## [Infix Notation](https://en.wikipedia.org/wiki/Infix_notation)

My initial plan was to re-implement infix calculator with *yacc* and *lex* 
as I remember reading about it in [The Unix Programming Environment](https://en.wikipedia.org/wiki/The_Unix_Programming_Environment) book. 
However, this reminded me about a more modern tool, 
[SLY](https://github.com/dabeaz/sly) which I wanted to try for a long time.

Calculator using infix notation is provided as en [example](https://github.com/dabeaz/sly#an-example) in SLY documentation. Based on that I created two new parsers:
 - PNCalcParser  
 - RPNCalcParser  

that use the same Lexer. Implementation can be found towards the end of [calculators.py](./calculators.py)

## Alternative Approach

**Fun fact:** None of the so far presented implementations is related to 
[Brian Harvey’s lecture](https://archive.org/details/ucberkeley_webcast_nzMPF59Ackg) 
I've mentioned at the beginning. 
So far, I've only focused on my approach to the calculator interpreter and 
it's very different from [the one explained during the lecture](./calculator.scm).  

One important difference is that this calculators works with Polish Notation, but expects the input to be in the form of [S-expression](https://en.wikipedia.org/wiki/S-expression), i.e.
`(+ 2 3)` instead of `+ 2 3`.
