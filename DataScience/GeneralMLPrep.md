CNN
==========
* CNN are deep learning architectures that are primarily used for processing image data. 
* The special operation known as Convolution helps them extract features like edges and textures, in combination with filters.
* ReLU is applied as a activation function to add non linearity
* Pooling is perfomed to reduce the spatial dimensions while retainign important information. This is helpful in computational load and controlling overfitting
* Fully Connected Layer (FCL) , after several convolution and pooling operations, the output is passes through a FCL to generate class probabilties needed for classification.

How CNNs Work:
==========
* The input image is transformed into a numerical representation, where each pixel is assigned a value based on its intensity.
* The convolution operation involves sliding the filter across the image and performing element-wise multiplication, followed by summation to create a feature map.
* As data progresses through multiple layers, CNNs learn increasingly complex features, from simple edges in early layers to intricate shapes in deeper layers.

Applications:
==========
CNNs are widely used in various fields such as:
* Image Recognition: Identifying objects in images (e.g., facial recognition).
* Medical Image Analysis: Analyzing X-rays or MRIs for diagnostic purposes.
* Autonomous Vehicles: Object detection and scene understanding.

RNN
==========
* RNN are a class of nerual networks that are excellent at processing sequential data
* They maintain an internal state at time step `t` for input `x(t)`, and combines it with hidden state from the previous step `h(t-1)` to produce a new hidden state `h(t)`
* h (t) = f [ W(h) * h(t−1)  + W(x) * x(t) + b], W(h) and W(x) are weight matrics and b is the bias term, f is the activation function

Applications:
==========
RNNs are commonly used in:
* Natural Language Processing: Tasks such as language modeling, text generation, and sentiment analysis.
* Speech Recognition: Processing audio signals to convert speech into text.
* Time Series Prediction: Forecasting stock prices or weather conditions based on historical data.

Decision Tree
==========
* Decision tree is a supervised ML algorithm used in classification and regression taks
* It is able to model decision and possible consequences in the form of a tree like strcuture
* The branch represents a `decision rule` and the internal node represents a `feature`. The leaf node or the terminal node of the branch is the `outcome`

Building a Decision Tree:
==========
DEINR (pronounced as "Diner") : Data; Entropy; InformationGain ; NodeSeletion; RecursiveSplitting
* Data Input: Start with the entire dataset.
* Entropy Calculation: Calculate the entropy of the target variable and predictor attributes to measure impurity.
* Information Gain: Determine the information gain for each attribute to identify which feature best splits the data.
* Node Selection: Choose the attribute with the highest information gain as the root node.
* Recursive Splitting: Repeat this process recursively for each branch until all branches are finalized or a stopping criterion is met (e.g., maximum depth or minimum samples per leaf)

Advantages:
==========
* Easy to interpret and visualize.
* Requires little data preprocessing (no need for normalization).
* Can handle both numerical and categorical data.

Disadvantages:
============
* Prone to overfitting, especially with deep trees.
* Sensitive to small variations in data.

