# Vectors

Vectors are represented in 3 different ways by different people.
Physics people see it as direction
CS people see it as list
Mathematics people see it as combination of direct + list, because we do operation on numbers and find the direction

vectors in 2D are nothing but coordinated which tells at what distance from origin and in which direction
It's an arrow that always starts at (0, 0). That constraint is what makes vectors useful in ML. Every product in your retail dataset is a point measured from the same origin. That's what allows you to compare them, add them, find distances between them.

### Adding 2 vectors :
It's the tip-to-tail movement. You walk along the first vector, then walk along the second from where you landed. The result is where you end up. 

### What would two similar products look like relative to each other?
Similar products would be vectors pointing in roughly the same direction, not overlapping. Identical products overlap. Similar products form a small angle between them. 

### if I give you two vectors [1,0] and [0,1], can you reach every point in 2D space by scaling and combining them? What if both vectors pointed in the same direction?
yes reachable
if pointed in same direction then can access only in single line. This is called linearly dependent vectors because one of them is redundant and doesn't add any value to the span. 
`Span` is the collection of all linear combination of 2 vectors, its the collection of all reachable points.

### linearly dependent :
 set of vectors is linearly dependent, one of those vectors can be expressed as a linear combination of the others, because it is already sitting within the span of those other vectors. This tells that on of the vector is redundant

### linearly independent 
Those vectors where each vector adds a new dimension to the span, and no vector can be removed without making the span smaller

- A basis is the minimal, sufficient set of vectors needed to describe a coordinate system. If they weren't linearly independent, you'd have unnecessary, redundant vectors; if they didn't span the space, you wouldn't be able to reach every point.

- If your vectors are zero, their span is just the origin. Because a zero vector contributes nothing to the span, it is technically "redundant" and does not contribute to the dimensionality of the space.

Correlated features are always the same direction or opposite direction (perfectly correlated or perfectly anti-correlated). A small angle means highly correlated but not perfectly. The important production case is perfect correlation — that's when one vector is literally inside the span of another, determinant becomes zero, and your model breaks.

A DataFrame with 10 columns = 10 vectors trying to span a 10-dimensional space. If 2 columns are correlated, you actually only have 9 independent dimensions. Your model thinks it has 10 features of information. It actually has 9. That's why correlated features hurt model performance — not because of some abstract rule, but because they're geometrically redundant.