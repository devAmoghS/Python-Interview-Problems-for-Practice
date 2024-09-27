## Popular Algorithms in Data Science with Mathematical Formulations

Here is an expanded overview of popular algorithms in data science, including their mathematical formulations, loss functions, performance metrics, and caveats.

### 1. **Linear Regression**
- **Mathematical Formula:** 
  $$ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n + \epsilon $$
  where $$y$$ is the dependent variable, $$x_i$$ are independent variables, $$\beta_i$$ are coefficients, and $$\epsilon$$ is the error term.
- **Loss Function:** Mean Squared Error (MSE)
  $$ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
- **Performance Metrics:** R-squared (R²), Adjusted R², Mean Absolute Error (MAE)
- **Caveats:** Sensitive to outliers; performs poorly with non-linear relationships.

### 2. **Logistic Regression**
- **Mathematical Formula:** 
  $$ P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + ... + \beta_n x_n)}} $$
- **Loss Function:** Binary Cross-Entropy Loss (Log Loss)
  $$ L = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i)] $$
- **Performance Metrics:** Accuracy, Precision, Recall, F1 Score
- **Caveats:** Assumes linearity in log odds; not suitable for multi-class without modification.

### 3. **Decision Trees**
- **Mathematical Formula:** 
  - For classification using Gini Impurity:
    $$ Gini(D) = 1 - \sum_{j=1}^{C} p_j^2 $$
    where $$p_j$$ is the proportion of class $$j$$ in dataset $$D$$.
  - For regression:
    $$ MSE(D) = \frac{1}{|D|} \sum_{i=1}^{|D|} (y_i - \bar{y})^2 $$
    where $$y_i$$ are the actual values and $$\bar{y}$$ is the mean of $$y$$.
- **Loss Function:** Gini Impurity or Mean Squared Error
- **Performance Metrics:** Accuracy, MAE
- **Caveats:** Prone to overfitting; sensitive to data changes.

### 4. **Support Vector Machines (SVM)**
- **Mathematical Formula:** 
  $$ f(x) = w^T x + b $$
  where $$w$$ is the weight vector and $$b$$ is the bias.
- **Loss Function:** Hinge Loss
  $$ L(y, f(x)) = \max(0, 1 - y f(x)) $$
- **Performance Metrics:** Accuracy, Precision, Recall
- **Caveats:** Computationally expensive for large datasets; requires careful tuning of hyperparameters.

### 5. **Random Forest**
- **Mathematical Formula:** 
  The prediction is made by averaging the predictions from multiple decision trees:
  $$ \hat{y} = \frac{1}{N} \sum_{i=1}^{N} T_i(x) $$
  where $$T_i$$ are individual trees.
- **Loss Function:** Mean Squared Error or Gini Impurity
- **Performance Metrics:** Out-of-Bag Error, Accuracy
- **Caveats:** Less interpretable than single trees; requires significant computational resources.

### 6. **Gradient Boosting Machines (GBM)**
- **Mathematical Formula:**
  $$ F(x) = F_{m-1}(x) + \gamma_m h_m(x) $$
  where $$h_m(x)$$ is the new tree added at iteration $$m$$.
- **Loss Function:** Log Loss or Mean Squared Error
- **Performance Metrics:** RMSE
- **Caveats:** Sensitive to overfitting; requires careful tuning of learning rate and tree depth.

### 7. **Neural Networks**
- **Mathematical Formula:**
  $$ y = f(WX + b) $$
  where $$W$$ are weights, $$X$$ is input data, and $$b$$ is bias.
- **Loss Function:** Cross-Entropy Loss or Mean Squared Error
  - Cross-Entropy for classification:
    $$ L = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i)] $$
- **Performance Metrics:** Accuracy, F1 Score, AUC
- **Caveats:** Requires large amounts of data; less interpretable than traditional models.

### 8. **K-Means Clustering**
- **Mathematical Formula:**
$$ J = \sum_{i=1}^{k} \sum_{j=1}^{n} ||x_j^{(i)} - c_i||^2 $$
where $$c_i$$ are centroids and $$x_j^{(i)}$$ are data points assigned to cluster $$i$$.
- **Loss Function:** Sum of Squared Errors (SSE)
- **Performance Metrics:** Silhouette Score, Davies-Bouldin Index
- **Caveats:** Assumes spherical clusters; sensitive to initial centroid placement.

## Summary of Formulations

| Algorithm               | Mathematical Formula                                                                 | Loss Function                       | Performance Metrics                     |
|------------------------|-------------------------------------------------------------------------------------|------------------------------------|----------------------------------------|
| Linear Regression       | $$ y = \beta_0 + \beta_1 x_1 + ... + \beta_n x_n + \epsilon $$                    | MSE                                | R², MAE                                |
| Logistic Regression     | $$ P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + ... + \beta_n x_n)}} $$                 | Binary Cross-Entropy               | Accuracy, F1 Score                     |
| Decision Trees          | Gini: $$ Gini(D) = 1 - \sum p_j^2 $$                                              | Gini Impurity / MSE               | Accuracy, MAE                          |
| Support Vector Machines | $$ f(x) = w^T x + b $$                                                             | Hinge Loss                         | Accuracy, Precision                     |
| Random Forest           | $$ \hat{y} = \frac{1}{N} \sum T_i(x) $$                                           | MSE / Gini Impurity                | Out-of-Bag Error                       |
| Gradient Boosting       | $$ F(x) = F_{m-1}(x) + h_m(x) $$                                                  | Log Loss / MSE                     | RMSE                                   |
| Neural Networks         | $$ y = f(WX + b) $$                                                                 | Cross-Entropy / MSE                | Accuracy, AUC                          |
| K-Means Clustering      | $$ J = \sum ||x_j^{(i)} - c_i||^2 $$                                              | SSE                                | Silhouette Score                       |

This comprehensive overview provides insights into each algorithm's mathematical foundation along with its practical applications and limitations. Understanding these aspects can help in selecting the right algorithm for specific data science tasks.

Citations:
[1] https://www.kdnuggets.com/2020/01/decision-tree-algorithm-explained.html
[2] http://fiascodata.blogspot.com/2018/08/decision-tree-mathematical-formulation.html
[3] https://en.wikipedia.org/wiki/Decision_tree_learning
[4] https://www.datascienceprophet.com/understanding-the-mathematics-behind-the-decision-tree-algorithm-part-i/
[5] https://towardsdatascience.com/the-mathematics-of-decision-trees-random-forest-and-feature-importance-in-scikit-learn-and-spark-f2861df67e3?gi=36fa533e014a
[6] https://www.datacamp.com/tutorial/loss-function-in-machine-learning
[7] https://neptune.ai/blog/performance-metrics-in-machine-learning-complete-guide
[8] https://towardsdatascience.com/estimators-loss-functions-optimizers-core-of-ml-algorithms-d603f6b0161a?gi=5432fa9d3888
