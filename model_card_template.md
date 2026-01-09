# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Name: Census Income Logistic Regression Classifier

Developed by: Christopher DuPée

Organization: Independent academic project

Model Date: 2026-01-08

Model Version: v1.0

Model Type: Binary classification model

### Training Algorithm

Logistic Regression implemented using scikit-learn (LogisticRegression).

### Key Parameters

Solver: saga

Random state: 42

Regularization: Default L2 regularization

Maximum iterations: Default (convergence warning observed)

### Feature Processing

Categorical features encoded using OneHotEncoder

Continuous features scaled using StandardScaler

Target labels binarized using LabelBinarizer


### Training Data Source

U.S. Census Income Dataset derived from the 1994 Census database.
Extraction performed by Barry Becker and distributed via the UCI Machine Learning Repository.

## Intended Use
### Primary Intended Uses
Educational demonstration of a complete machine learning pipeline
Practice in data preprocessing, model training, evaluation, and deployment readiness
Illustration of responsible ML documentation practices

### Primary Intended Users
Instructors evaluating ML pipeline design

## Training Data
### Dataset
UCI Census Income Dataset (“Adult” dataset)

### Preprocessing

Missing or unknown categorical values handled via encoder configuration
Categorical features one-hot encoded
Continuous features standardized
Dataset split into training (80%) and test (20%) sets with shuffling

## Evaluation Data
The evaluation dataset mirrors the training dataset and consists of approximately 20% of the full Census Income dataset after preprocessing.

## Metrics
### Model Performance Measures

-Precision
-Recall
-F1 score (β = 1)

### Observed test-set performance:

-Precision ≈ 0.75
-Recall ≈ 0.62
-F1 ≈ 0.68

### Decision Threshold

Default Logistic Regression probability threshold (0.5)

### Variation Approaches

Performance was evaluated on categorical data slices in addition to complete evaluation set.
Slice-based metrics were reported individually.

## Ethical Considerations
Demographic distributions reflect those present in the original 1994 Census sample and were not balanced or reweighted.
## Caveats and Recommendations
