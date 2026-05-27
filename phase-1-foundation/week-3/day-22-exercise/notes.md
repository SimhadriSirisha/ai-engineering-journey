# 2D Matrix Transformation Visualizer

## What this project shows :
This project visualizes how matrix multiplication transforms 2D space geometrically. Each transformation shows where i-hat [1,0] and j-hat [0,1] land after multiplying by a matrix — and how the entire grid follows. Built as part of Week 3 of my AI engineering learning journey.

## Transformations
### Shear
**Geomaetric observation**: x - axis remained contant and slight movement to y axis, we can see j hat only sifted
**ML usecase**: Shear is mainly important in computer graphics and data augmentation for images — rotating/skewing training images slightly so the model learns to handle varied inputs.

### Rotation
**Geomaetric observation**: Rotated 90 degree, j moved to (-1, 0) & i came to (0, 1)
**ML usecase** : In image classification, the same product photographed at different angles produces a rotated feature space. Data augmentation applies rotation transformations to training images so the model learns to recognise products regardless of orientation i.e identify that the product is same regardless of its orientation.

### Scale
**Geomaetric observation**: increase in size
**ML usecase**: When features have very different ranges — price 0-10000, rating 1-5 — one feature dominates the others during training. Feature scaling (normalisation) transforms all features to the same range. That's a scale transformation applied to your feature space.

### Collapse
**Geomaetric observation**: Collapsed to single line 
**ML usecase**: Determinant = 0 means dependent features collapsed the space to a single line. The model loses an entire dimension of information. Correlated features like price and price_after_discount cause this — removing one is safe because the span doesn't shrink.

## Why this matters for ML
Every layer in a neural network applies a matrix transformation to your data — 
rotating, scaling, and shearing the feature space until patterns become separable. 
Understanding these transformations geometrically is the foundation for understanding 
why neural networks work, why correlated features hurt models, and why feature 
normalisation is necessary before training.

## How to run
run this command : `python matrix_visulizer.py`