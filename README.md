# Collatz Conjecture
# Python 3.x

The Collatz Conjecture is very straightforward to state and test, but has so far been unsuccessfully proven.

It states: 
  Start with any whole number (1, 2, etc.).
    If it's odd, multiply it by 3, then add 1.
    If it's even, divide by 2.
  Iterate that.
  The conjecture is that every whole number eventually falls to 1 (wherein 1 gets trapped in a loop of 
  1 -> 4 -> 2 -> 1).

This can be simplified slightly since as soon as the number hits a power of 2 (i.e. 2^n), then it'll always 
be even until it reaches 1.

This program is just a fun program to run and test up to the precision of the computer used.
