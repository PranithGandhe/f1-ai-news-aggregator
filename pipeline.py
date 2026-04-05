from ingestion import ingest
from processing import process_articles
from database import initialize_database

import nltk
nltk.download('punkt_tab')

def run_pipeline():
    
    initialize_database()
    print("Starting Pipeline.!!!!!!!")
    ingest()
    process_articles()
    print("Pipeline Completed.!!!!!!!")