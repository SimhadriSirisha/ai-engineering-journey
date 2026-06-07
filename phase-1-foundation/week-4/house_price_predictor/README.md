# Purpose of each file
exploration.py  ← understand the data (what you're doing now)
                  EDA (Exploratory Data Analysis), checking unique values, checking scales,
                  visualizing distributions, finding issues

    EDA includes 
    1. Shape          → how many rows, columns (you did this)
    2. Data types     → numerical vs categorical
    3. Missing values → nulls, empty strings (you did this)
    4. Distributions  → what's the range, mean, spread of each feature
    5. Outliers       → values that are suspiciously high or low
    6. Correlations   → which features actually relate to price
    7. Unique values  → what's inside categorical columns

train.py        ← build and train the model (after EDA is done)
                  encoding, scaling, gradient descent, evaluation

# About Dataset:
1. #rows = 545 & #columns = 13
2. columns are 'price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus'
3. Its a clean dataset with no null values. 
4. target columne 'price' range -> min = 1.750000e+06 & max = 1.330000e+07

# Exploration
1. We have 2 types of features i.e. 
    - Numerical:  area, bedrooms, bathrooms, stories, parking
    - Categorical: mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus
    
    Categorical columns contain text like "yes/no" or "furnished/unfurnished/semi-furnished". Gradient descent code can't handle text — needs to be converted to numbers first.

2. All categorical columns have only 2 featurs so can be encoded to 0(No) /1(Yes) except furnishingstatus which has 3 unique columns converted to 0(unfurnished),1(semi-furnished),2(furnished)

3. Need of feature scaling, area has very large value. So needed scaling. **Rule of Thumb for production** : Scale all numerical features by default. Only skip scaling if you have a specific reason.

# Training

4. Always Separate X & Y before training.

5. What to do if null values are found
        
        < 5%  nulls  → drop rows
        5-30% nulls  → fill with mean/median (median preferred when there ARE outliers, Mean gets pulled by extreme values, median doesn't)
        > 40% nulls  → drop the column

6. We need to split the dataset into train and test set to avoid overfitting of model. If we give full data to model it memorized rather than learning. And also with test data we will see how accurately the model is learning. Basic rule is 80/20. 80% - train data & 20% - test data.

        Good (generalizing):        Bad (overfitting):
        Train accuracy: 85%         Train accuracy: 99%
        Test accuracy:  82%         Test accuracy:  45%

        Small gap = model learned   Huge gap = model memorized

7. Scaling before Splitting (a silent failure):
If we scale before the mean and standard deviation of test data can inflence the nodel training which means model can see the test data. So which is indirectly overfitting.

8. Test data must be scaled using training statistics because in production there is no test set — there is only the real world, and the real world gets scaled using whatever parameters you computed at training time.

9. Correct order of execution :

        1. suffle df
        2. Split
        3. Compute mu, sigma from train only
        4. Scale train with those stats
        5. Scale test with those SAME stats
        6. Train model
        7. Evaluate on scaled test

10. Shuffling randomizes the order so both sets get a representative mix of cheap and expensive houses.

11. b converged to essentially 0 — that's expected when data is scaled, because scaling centers everything around 0, so the intercept disappears.

12. With 1000 iteration the cost vs iteration tail plot is still decreasing.

        Iteration 800: 0.157168
        Iteration 900: 0.157167
    so increased to 2000, and it converged because if see the cost remained constant at 0.157167 from 900 iteration
converged at ~1000 iterations, but we only discovered this because of the tail plot.
Without the tail plot, stopping at 1000 looked correct on the full cost curve.
→ Always check tail plot before calling training done.

13. Note : features with higher value of W parameter are important features which are impacting the price of house

14. MSE   → average squared error (not a percentage, lower is better)
RMSE  → square root of MSE (same units as target, easier to read)
R²    → how much price variation model captures (0 to 1, higher is better)
       NOT prediction accuracy

15. Feature Importance (top 5):
area                 : 0.2898  — strongest price driver
bathrooms            : 0.2650  — 4.6x stronger than bedrooms
airconditioning      : 0.2369  — premium feature in Bangalore climate
stories              : 0.2175
prefarea             : 0.1595

Key insight: bathrooms predict price 4.6x better than bedrooms

16. Model Performance:
Train R²:  0.6857  — model captures 68.57% of price patterns
Test R²:   0.6459  — generalises well (small gap = no overfitting)
Train MSE: 0.3143
Test MSE:  0.3569