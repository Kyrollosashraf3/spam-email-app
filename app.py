import streamlit as st
import joblib

# تحميل الموديل والـ vectorizer
model = joblib.load("spam_classifier.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📧 Spam Email Classifier")
email_text = st.text_area("أدخل نص الإيميل هنا:")

if st.button("تحليل"):
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)
    st.write("النتيجة:", "🚨 Spam" if prediction[0] == 0 else "✅ Not Spam")
