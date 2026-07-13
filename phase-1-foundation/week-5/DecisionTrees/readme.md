### Why decision trees, if logistic existed
Logistic regression draws a straight line (or flat plane in higher dimensions) as the decision boundary. Always. 

That's baked into the math — W·x + b = 0 is always linear.

So if your data looks like this:

        Class 0: low price AND low demand, OR high price AND high demand
        Class 1: low price AND high demand, OR high price AND low demand

No straight line separates this. Logistic regression fundamentally cannot learn this pattern, regardless of how many iterations or how much data you give it.

Decision trees don't draw lines — they ask questions:

        Is price > 50?
        ├── Yes: Is demand > 100? → class 1
        └── No:  Is demand < 20?  → class 0

These are axis-aligned rectangular boundaries — completely different shape from a line.