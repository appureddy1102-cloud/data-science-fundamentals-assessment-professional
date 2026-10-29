# Ten viva questions

1. **What is the difference between a list and tuple?** A list is mutable; a tuple is immutable and can represent a fixed record.
2. **What does a Pandas DataFrame represent?** A labeled table with columns that may have different data types.
3. **Why remove duplicates before summarizing?** Repeated records can inflate counts and totals.
4. **What is the IQR?** The third quartile minus the first; it summarizes the spread of the middle half of observations.
5. **Why is sample variance divided by n−1?** The correction accounts for estimating the mean from the same sample and makes sample variance unbiased under standard independent sampling assumptions.
6. **What is a p-value?** Under the null model, the probability of data at least as incompatible with that model as observed, according to the chosen test statistic; it is not the probability the null is true.
7. **Does correlation show causation?** No; confounding, reverse causality and chance can explain association.
8. **What is data leakage?** Information unavailable at prediction time enters training or preprocessing, producing overly optimistic evaluation.
9. **Precision versus recall?** Precision is TP/(TP+FP); recall is TP/(TP+FN).
10. **Why can accuracy mislead on imbalanced data?** Predicting the majority class may achieve high accuracy while missing nearly all minority cases; use class-sensitive metrics and a baseline.
