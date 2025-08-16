# Spam Email Classifier

This project builds a machine learning model to classify emails as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques.

## Dataset
- Source: SMS/Email dataset (commonly used for spam detection tasks).
- Contains text messages labeled as `spam` or `ham`.

## Objective
- Preprocess and clean text data.  
- Convert text into numerical features using **TF-IDF Vectorization**.  
- Train machine learning models to classify messages as spam or ham.  
- Evaluate performance using accuracy, confusion matrix, and classification report.

## Steps
1. **Data Loading & Exploration**  
   - Load dataset with labels (spam/ham).  
   - Check data balance and perform exploratory analysis.  

2. **Text Preprocessing**  
   - Lowercasing text.  
   - Removing stopwords and punctuation.  
   - Tokenization and Lemmatization.  

3. **Feature Engineering**  
   - Applied **TF-IDF Vectorizer** to convert text into numerical representation.  

4. **Modeling**  
   - Trained multiple models: Logistic Regression, Naïve Bayes, etc.  
   - Compared performance across models.  

5. **Evaluation**  
   - Confusion Matrix  
   - Accuracy, Precision, Recall, F1-score  

## Results
- The best performing model achieved high accuracy in detecting spam messages.  
- TF-IDF features combined with Logistic Regression gave reliable performance.  

## How to Run
1. Clone this repository.  
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt


