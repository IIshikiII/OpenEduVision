from transformers import pipeline
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class CourseAnalyzer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    def analyze_course(self, text: str):
        """НЛП-анализ описания курса"""
        summary = self.summarizer(text, max_length=60, min_length=20, do_sample=False)
        return summary[0]["summary_text"]

class PerformancePredictor:
    def __init__(self):
        self.model = RandomForestClassifier()
    
    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
