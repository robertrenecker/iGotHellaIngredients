###Question 1:

Exercise. In your write-up, give a refactored version of the re grammar from ?? that eliminates ambiguity in BNF (not EBNF). Use the following template for the new non-terminal names:

re ::= union

union ::= union '|' intersect | intersect

intersect ::= intersect '&' concat | concat

concat ::= concat not | not

not ::= star | '~' not

star ::= star "*" | star "+" | star "?" | atom

atom ::= c | '#' | '!' | '.' | '(' re ')'

###Question 2:

Exercise. Explain briefly why a recursive descent parser following your grammar with left recursion would go into an infinite loop.

In left recursion, we wont consume a character. We recurse prior to consuming a character, so we might get stuck in an infinite loop.

###Question 3:

Exercise. In your write-up, give a refactored version of the re grammar that replaces left-associative binary operators with n-ary versions using EBNF using the following template:

re ::= union

union ::= intersect { ‘|’ intersect }

intersect ::= concat { '&' concat}

concat ::= not { not}

not ::= { '~'} star

star ::= atom{ "*" | "+" | "?"}

atom ::= c | '#' | '!' | '.' | '(' re ')'

###Question 4:

In your write-up, give the full refactored grammar in BNF without left recursion and new non-terminals like unions for lists of symbols. You will need to introduce new terminals for intersects and so forth.

re ::= union

union ::= intersect unions

unions ::= e | ‘|’ intersect unions

intersect ::= concat intersects

intersects ::= e | '&' concat intersects

concat ::= not concats

concats ::= e | not concats

not ::= '' star | '' not

star ::= atom stars

stars ::= e |"*" atom stars | "+" atom stars | "?" atom stars

atom ::= c | '#' | '!' | '.' | '(' re ')'

###Question 5:

Type Rules:

_________________
|Gamma |- e : t |
|_______________|


-------------------------
Gamma |- /^re$/ : RegExp

Gamma |- e1 : RegExp   Gamma |- e2 : String
--------------------------------------------
    Gamma |- e1.test(e2) : bool
Small Step Rules:

___________________
|<M,e> -> <M',e'>|
|_________________|

            <M,e> -> <M',e'>
--------------------------------------   (search rule)
<M, e1.test(e2)> -> <M', e1'.test(e2)>

          <M,e2> -> <M',e2'>
----------------------------------------------  (search rule)
<M, /^re$/.test(e2)> -> <M', /^re$/.test(e2')>