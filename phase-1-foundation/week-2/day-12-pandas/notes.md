# Pandas
- Pandas is data manipulation and analysis library built specifically to work with structured/tabular data.
- Pandas support 2 data structures:
    - `series` : 1D labelled array with data of different data types
    - `Dataframe` : 2D labelled table

## Dependency with NumPy :
Pandas was built on top of NumPy library. These data structures `seires` & `dataframe` internally stores its data sa ndarray in numPy. All mathematical operations are handed over to numPy's optimized c level functions

# Titanic dataset Analysis with pandas:
### Task 1
1. file reading using pd.read_csv() into a dataframe
2. to see few content with header, used df.head()
3. df.shape - gives dimension of dataset
4. df.dtypes - gives information about column types 
5. df.info() - gives the information about every column, their types and their not null count.
6. df.describe() - gives all mathematical information about all numerical columns.
7. df.assign() - returns a new dataframe with added column. During method chaining its always better to pass a function instead of direct column.
    **for eg**:
        df2 = df.dropna(subset = ["colx"]).assign(new_col = df["colx"]*4)
        -> here assign() taking df["colx"] * 4 takes original df's colx and not the changed one that is NA removed col then it will produce an error of shape missmatch.

        df2 = df.dropna(subset = ["colx"]).assign(new_col = lambda x: x["colx"]*4)
        -> here x["colx"] takes current colx values and not the original colx
8. df["col_n"].value_count() - gives count of each category. Checks the value distribution

### Task 2
1. fillna() : fills the column value which are na
2. isna() : returns rows which are NA
3. dropped cabin column becuase lots of NA values and doesn't give much impact and cant replace nan values with mean or median.
4. always use median because its the exact middle value and not influenced by outliers.
5. there no null values in embrked so thought of encoding the the column value but not possible because it has 4 different values
6. Groupby is split, apply & combine.
    - split : always grouping happens in row level i.e. split along rows. If we split along columns then first transpose.
    - apply : function will be applied on the group
    - combine : each groups applied function result will be combined together and gets the final result.
7. groupby with as_index, if `true`(default) then on the column which we are grouping will be act as index and when `false` then the column will be as column and not index. Difference is mostly readability purpose and when method chaining or merging, if there is any use with that column then as_index = false makes sense.
8. aggregate() shrinks the rows and transform() keeps the original dataframe shape.
9. filter() applied on group level and not row level. That means on aggregate functions. Filters to keep/drop the group.
