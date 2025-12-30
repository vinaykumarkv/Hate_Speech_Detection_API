from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nltk.sentiment.vader import SentimentIntensityAnalyzer


app = FastAPI(title="Hate Speech Text Classifier")


analyzer = SentimentIntensityAnalyzer()

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {
        "message": "Text Classification API",
        "endpoint": "POST /classify",
        "example": {"text": "I love this so much!"}
    }

@app.post("/classify")
def classify_text(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    text = input.text.strip()

    # Get sentiment scores
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    # These scores can be modified as per thresholds
    if compound <= -0.5:
        category = "hateful"
    elif compound >= 0.5:
        category = "friendly"
    else:
        category = "neutral"

    return {
        "text": text,
        "classification": category,
        "confidence": round(abs(compound), 3),
        "compound_score": round(compound, 3),
        "details": {
            "neg": scores['neg'],
            "neu": scores['neu'],
            "pos": scores['pos']
        }
    }