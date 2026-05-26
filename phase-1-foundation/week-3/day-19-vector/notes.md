- matrix multiplication is application of different trasformation one after the other. That is called composition.
- Matrix multiplication is not commutative (A X B != B X A), geometrically if seen its not possible, check example1
- it is associative

- Matrix multiplication is non-commutative. Order of transformations changes the result. I already knew this intuitively from Spark — .filter().groupBy() gives different results than .groupBy().filter(). Linear algebra just gave me the geometric language for something I've been doing in production for years.

- Grid = the coordinate space itself. Data points = things sitting in that space. Matrix transformation moves the space. Data points ride along. The grid staying parallel is a property of the transformation, not a requirement on the data.

- determinent is magnitude by which the area scaled. 
- How this is true for all shapes ? as grid lines are parallel and fixed origin, if can find by what factor the base square i.e. basis vectors area (1 sq) changes. That same factor other can also be told if the shape is square, if its not square something like oval then we approximate the oval shape with the small squares, if determined by what fact the small square changed we can find it for the big shape.
- if the determinent is -ve then it tells that the space has been inverted
- If the determinant = 0 then it tells that the space has been collapsed to single line or in worst case the grid collapses to single point
- In case of 3 dimenstion, it is the factor by which volume scaled.
- det(M1M2) = det(M1)det(M2), this is true because if M1 scales area by factor A, and M2 scales area by factor B, then applying both scales area by A×B. It's multiplicative because you're scaling a scaling.

- matrix is nothing but a transformation

- Usecases of matrix transformation in 3D is in computer graphics, gamings etc. Also in some technical solution also. 
To Solve those we need to know matrix inverse. 

    eg:
    
        10x + 4y = 6
        8x + 2y = 4

        the above can be represented as :
        |10 4||x|   |6|
        |8  2||y| = |4| => A(x-hat) = v-hat

        here are x & y can be calculated using A invers

- An inverse is not possible for the collapsed space (i.e a line for 2D & plane for 3D)
- After matrix transformation of the output remain single point then Rank 0, single line than Rank 1, if 2D then Rank 2. If 3D space transformation results to 3D space then Rank 3 
- null space is all vectors that get transformed to the zero vector [0,0] after transformation.
- When space collapses to a line, many different points all land on the same spot. Specifically, an entire line of points all gets squished to the origin [0,0]

- In a matrix, rows represent coordinates & columns represent basis vectors

- Determinant = something is wrong. Null space = exactly what is wrong and where.
- Ep 01
Vectors over points — operations are defined on vectors. Fixed origin makes comparison meaningful.
your insight: "if base is same among all products, comparison makes correct"
Ep 02
Span = all reachable points. Correlated features = dependent vectors = removing one doesn't shrink the span.
your insight: "even if we remove one it won't decrease the span so it's ok to remove one"
Ep 03
Matrix = transformation of space. i-hat and j-hat landing points describe everything. Parallel grids make the scaling relationship consistent.
your insight: proved [4,2] → [8,6] geometrically without formula
Ep 04
Matrix multiplication = composition of transformations. Not commutative — order matters.
your insight: ".filter().groupBy() ≠ .groupBy().filter() — same idea from your Spark work"
Ep 05
Determinant = factor by which area scales. Det = 0 means space collapsed. Negative det means space flipped.
your insight: derived why the formula works from landing points, not memorised it
Ep 06
Inverse = undoing a transformation. Impossible when det = 0. Rank = dimensions surviving after transformation.
your insight: connected equations → matrix → inverse as one system
Ep 09
Dot product = how much two vectors point in same direction. Cosine similarity = dot product normalised for length. Small angle = similar.
your insight: raw dot product affected by magnitude — cosine similarity fixes that
the one connected idea across all 9 episodes
→
data becomes vectors, fixed origin makes comparison meaningful
→
correlated features are redundant vectors — removing them doesn't shrink the span
→
matrix transforms that space — two landing points describe everything
→
determinant tells you if information was lost in that transformation
→
null space = the specific combinations your model can never see
→
dot product measures similarity between any two vectors in that space

- direction tells you whether they're similar. Magnitude tells you how strongly similar.
But here's the problem you already identified earlier — magnitude is also affected by the length of the vectors themselves. A long vector and a short vector pointing in exactly the same direction give different dot product values. That's misleading.

- Change of basis = translating between coordinate systems. The formula with inverse of basis is just the translation mechanism.
- Eigen vectors are the vectors which remain on the span after the transformation, only scales by value which is called eigenValue. If eigen value is -ve then its orientation flipped during transformation, its not about shrinking.
- Eigenvalue = 1 means the vector doesn't scale at all — it stays exactly the same length and direction after transformation. No rotation involved.
- Rotation is when there are NO real eigenvectors — like a 90° rotation matrix where every vector changes direction
- There can be chance that there would be no eigenVectors
- eigenbasis are the basis vectors which are eigenVectors
- For eigenvectors specifically — if you use eigenvectors as your basis, the transformation matrix becomes diagonal. Much simpler to work with. That's why eigenbasis matters.

- Eigenvectors — Use Cases
1. PCA (Dimensionality Reduction)
Original features are correlated and overlap. Eigenvectors give completely independent directions. Keep eigenvectors with large eigenvalues — they carry most variation. Drop small eigenvalue directions — they carry almost no information. 100 features → 5 eigenvectors → same data, less noise.
2. Understanding your data's natural structure
Eigenvectors reveal the directions your data actually varies in — not the axes you chose to measure. In retail data, the first eigenvector might capture "overall product value" — a combination of price, rating, and sales rank moving together.
3. Removing noise
Small eigenvalue directions = directions where data barely varies = mostly noise. Dropping them cleans your data before training.
4. Detecting multicollinearity
If two features are correlated, their combined direction dominates one eigenvector. Eigenvalue = 0 or near 0 means dependent features exist — same as determinant = 0.
5. Speeding up ML models
Less features after PCA = faster training, less memory, cheaper inference in production.

- Eigenvectors give you completely independent directions — no correlation between them. Each eigenvector captures a unique direction of variation that no other eigenvector captures.
So when you drop low-eigenvalue eigenvectors, you're dropping genuinely independent directions of variation — not just raw features that might be hiding shared information.


### Retail Product Recommendation System

The problem:
You have 10,000 products. Each product has 100 features — price, rating, discount, category, sales rank etc. A customer views a product. Find the 5 most similar products to recommend.

Every concept you learned, in order:

Vectors (Ep 1)
Convert each product into a vector of 100 numbers. Fixed origin means every product is measured from the same reference point — comparisons are meaningful.

Span + Linear Dependence (Ep 2)
Check your 100 features. Price and price_after_discount are correlated — dependent vectors. They don't add new dimensions to the span. Flag them for removal.

Matrix as Transformation (Ep 3)
Pass your product vectors through a neural network layer — a matrix transformation. i-hat and j-hat landing points describe what happens to every product vector automatically.

Composition — Order Matters (Ep 4)
Your neural network has 3 layers — transformations A, B, C applied in sequence. A×B×C ≠ C×B×A. Order of transformations changes the result. Wrong order = wrong recommendations.

Determinant (Ep 5)
Before training, check your feature matrix determinant. If det = 0, your feature space has collapsed — dependent features exist. Model will break or give unstable results.

Inverse + Rank + Null Space (Ep 6)
Null space = feature combinations your model literally cannot see. Price and price_in_dollars together → [1, -1] maps to zero → model can never distinguish them. Remove one before training.

Dot Product + Cosine Similarity (Ep 9)
Customer views Product A. Convert their viewed product into a vector. Calculate cosine similarity — normalised dot product — against all 10,000 product vectors. Small angle = similar product. Top 5 highest cosine similarity = your recommendations.

Eigenvectors + Eigenvalues (Ep 13–14)
100 features is too many — slow, noisy, expensive. Find eigenvectors of your feature matrix. Keep top 5 by eigenvalue size — they capture maximum variation independently, no double counting. Now each product is a 5-dimensional vector instead of 100. Faster, cleaner, cheaper.