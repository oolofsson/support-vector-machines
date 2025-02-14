# support-vector-machines
## Machine Learning Lab

### Questions to answer:
#### 1. Move the clusters around and change their sizes to make it easier or
#### harder for the classifier to find a decent boundary. Pay attention
#### to when the optimizer (minimize function) is not able to find a
#### solution at all.

* When using a linear kernel, it can not find an optimal solution when the classes are not linearly separable.

* When using a polynomial kernel, it can not find an optimal when the data is not separeable within the polynomials degree.?

* When using an radial kernel, it can not find an optimal solution when the data is not separable by any means.

#### 2. Implement the two non-linear kernels. You should be able to clas-
#### sify very hard data sets with these.

Done.

#### 3. The non-linear kernels have parameters; explore how they influence
#### the decision boundary. Reason about this in terms of the bias-
#### variance trade-off.

Having a higher polynomial degree and a lower sigma is will classify it more exact according to the training data and thus increasing the variance. Having a lower polynomial degree or higher sigma will instead induce more bias but lower variance.

#### 4. Explore the role of the slack parameter C. What happens for very
#### large/small values?

Having a higher slack paramter makes the classification more strict, including more points which means the "street" gets narrower. It is used as a penalty scale for the misslasified points. Which is then used as a part of the optimization.


#### 5. Imagine that you are given data that is not easily separable. When
#### should you opt for more slack rather than going for a more complex
#### model (kernel) and vice versa?

When having a noisy dataset it's better to have a low slack, so that noisy data is not accounted for.

