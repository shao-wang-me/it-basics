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

   ```
   function number_of_digits(n):
     if n = 0:
       return 1
     else:
       return floor(log10(abs(n))) + 1
   ```

1. When using two pointer technique, what would the index of the number we need to fill given the pointers' indices as `l` and `r`, if we are filling numbers from the start or from the end respectively?

   **Forward:** It would be `n - 1 + l - r` because there are `l + (n - 1 - r) = n - 1 + l - r` numbers already filled, and the next number is at index `n - 1 + l - r`.

   **Backward:** It would be `r - l` because there are `r - l + 1` numbers waiting to be filled and the `r - l + 1`th number is at index `r - l`.

   You can use a variable to track it if you don't remember.
