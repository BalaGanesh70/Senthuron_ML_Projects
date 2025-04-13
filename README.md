Machine Learning Projects: Text Summarization & Keyword Extraction
This repository contains two Natural Language Processing (NLP) projects that demonstrate summarization and keyword extraction capabilities using state-of-the-art models and deployment with Streamlit.

Task 1: Text Summarization using BART Transformer
Objective :
 
To generate concise summaries for large paragraphs using the BART transformer model and evaluate the quality of generated summaries using the ROUGE metric.

Description :
 
The task uses a dataset with multiple long-text paragraphs.
The BART model (facebook/bart-large-cnn) from Hugging Face is used to generate 3–5 line summaries for each paragraph.
Each paragraph is processed individually, and a corresponding summary is generated.

🛠Tools & Technologies :

Python
Hugging Face Transformers (BART)
ROUGE Evaluation (rouge_score)
Matplotlib / Seaborn for visualization

Streamlit for deployment :

Evaluation :
ROUGE Score (F1) is used to evaluate the performance of the summarization.
A line plot of the F1-score distribution is included to visualize the quality of the summaries.

Deployment :
The model is deployed using Streamlit, allowing users to input text or select paragraphs and view their summaries alongside ROUGE scores.




Task 2: Keyword Extraction using OpenAI
Objective:

To extract meaningful keywords from full news articles and categorize them based on topics like "Sports", "Politics", "United Kingdom", etc.

Description :

The BBC News dataset is used where each row contains a full news article.
OpenAI’s GPT model is used to extract keywords for each article.
The extracted keywords are stored in a separate file for further analysis.

Tools & Technologies:

Python
OpenAI API
Pandas
Streamlit

Features :

Performs keyword extraction for all articles in the dataset.
Allows filtering by fields/domains (e.g., "Sports", "United Kingdom").
Computes a relevance score for each keyword.
Users can download the refined keyword list as a CSV file from the Streamlit interface.

Deployment : 
Implemented using Streamlit for interactive exploration.







Installation & Setup
Clone the Repository


git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install Dependencies


pip install -r requirements.txt
Run Streamlit Apps


# For Task 1 - Summarization
streamlit run task1_summarization/streamlit_app.py

# For Task 2 - Keyword Extraction
streamlit run task2_keyword_extraction/streamlit_app.py
Future Enhancements
Integrate multiple summarization models for comparison.

Include keyword relevance visualization (bar graphs, word clouds).
Add user input interface for live summarization or keyword extraction from pasted text.

License
This project is open-source under the MIT License


Users can view, score, filter, and export keywords based on category/domain.



PIPELINED ARCHITECHTURE :

├── task1_summarization/
│   ├── Generated_Summaries.csv
│   ├── summarizer.py
│   ├── rouge_evaluator.py
│   └── streamlit_app.py
│
├── task2_keyword_extraction/
│   ├── BBC_news.csv
│   ├── openai_keyword_extractor.py
│   └── streamlit_app.py
│
├── requirements.txt
├── README.md
└── LICENSE
