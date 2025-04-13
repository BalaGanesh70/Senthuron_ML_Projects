# streamlit_app.py

import streamlit as st
import pandas as pd
import evaluate

st.set_page_config(page_title="ROUGE Score App", layout="wide")

# ⚡ Step 1: Load dataset with caching
@st.cache_data
def load_data():
    df = pd.read_csv("Generated_Summaries.csv")
    return df.head(1000)  # Only first 1000 rows

df = load_data()

# ⚡ Step 2: Load ROUGE metric once
@st.cache_resource
def load_rouge():
    return evaluate.load("rouge")

rouge = load_rouge()

# ⚡ Step 3: Compute ROUGE-1 scores with caching
@st.cache_data
def compute_rouge(df):
    scores = []
    for p, r in zip(df['text'], df['article_summaries']):
        result = rouge.compute(predictions=[str(p)], references=[str(r)])
        scores.append(result['rouge1'])  # Already float, no need for .fmeasure
    df['rouge1'] = scores
    return df

df = compute_rouge(df)

# Streamlit UI
st.title("📊 ROUGE Score Evaluation App")

st.write("### 🔍 Dataset Preview")
st.dataframe(df[['text', 'article_summaries', 'rouge1']])

st.write("### 📈 ROUGE-1 F1 Score Distribution")
st.bar_chart(df['rouge1'])
