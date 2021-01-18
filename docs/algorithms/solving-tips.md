# Tips for solving (interview and exam style) algorithm problems

## Steps

1. Input -> Output
1. Conditions
1. Edge cases
1. Best time/space complexity?
1. Talk about the basic idea
1. Write while talking (hard!)
1. Dry run with edge cases
1. Complexity recheck
1. Potential improvements, shortness

## Tips

1. Logarithm (对数)

   log<sub>10</sub>(x) = ln(x) / ln(10)

   log<sub>a</sub>(b) = ln(b) / ln(a)

   log(a * b) = log(a) + log(b)

   log(a / b) = log(a) - log(b)

1. How many digits does a number have?

   For positive integers, `floor(log10(n)) + 1`.

   For all integers?

   ```python
   from math import floor, log10
   def number_of_digits(n):
     if n == 0:
       return 1
     else:
       return floor(log10(abs(n))) + 1
   ```
