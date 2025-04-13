import streamlit as st
import pandas as pd
import openai
import re
import time

# Set OpenAI API Key
openai.api_key = "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"

# Load Dataset
df = pd.read_csv("BBCNews.csv").head(100)

# Text Cleaning
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

df['clean_descr'] = df['descr'].apply(clean_text)

# Extract Keywords from OpenAI
@st.cache_data(show_spinner=False)
def extract_keywords(text):
    prompt = f"Extract 5 relevant and concise keywords from this news article:\n\n{text}\n\nKeywords:"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=60
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Categorize Keywords using OpenAI
@st.cache_data(show_spinner=False)
def categorize_keywords(keywords_text):
    prompt = f"Classify these keywords into categories like Politics, Sports, Tech, Health, Entertainment:\n\n{keywords_text}\n\nCategories:"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=80
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Main Streamlit App
st.title("🔍 AI Keyword Extractor + Smart Tag Matching")

if st.button("🚀 Start Processing Keywords"):
    with st.spinner("Processing articles..."):
        extracted, categories, matches = [], [], []

        for _, row in df.iterrows():
            keywords = extract_keywords(row['clean_descr'])
            cat = categorize_keywords(keywords)

            tag = row['tags'].lower()
            match_score = sum([1 for kw in keywords.lower().split(',') if tag in kw]) / 5

            extracted.append(keywords)
            categories.append(cat)
            matches.append(round(match_score, 2))

            time.sleep(1.5)

        df['extracted_keywords'] = extracted
        df['keyword_categories'] = categories
        df['tag_match_score'] = matches

        st.success("✅ Keyword Extraction Complete!")

        st.write("### 📊 Extracted Results")
        st.dataframe(df[['tags', 'extracted_keywords', 'keyword_categories', 'tag_match_score']])

        st.write("### 📈 Tag Match Score Distribution")
        st.bar_chart(df['tag_match_score'])

        # Optional: Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", csv, "Enhanced_BBCNews.csv", "text/csv")

else:
    st.info("Click the button above to begin extracting keywords and visualizing matches.")
