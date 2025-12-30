# Simple Text Sentiment Classifier API

This is a lightweight web API that takes any text input and classifies it as one of three categories:  
**hateful** – strongly negative / toxic  
**neutral** – factual or emotionally flat  
**friendly** – clearly positive / warm  

It uses a basic, rule-based sentiment analysis tool (NLTK's VADER) so it runs fast, needs almost no resources, and works offline after initial setup.

## How It Works (Implementation Overview)

1. **Web Framework**  
   Built with FastAPI — a modern, fast Python framework that automatically creates interactive documentation and handles input validation.

2. **Sentiment Analysis**  
   Uses NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner):  
   - A pre-built lexicon that assigns sentiment scores to words, phrases, emojis, slang, etc.  
   - Returns a "compound" score between -1 (very negative) and +1 (very positive).  
   - No machine learning or heavy models are involved → quick startup and low memory usage.

3. **Classification Logic**  
   The compound score is mapped to one of three labels using simple thresholds:  
   - ≤ -0.5 → "hateful"  
   - ≥ +0.5 → "friendly"  
   - anything in between → "neutral"  

4. **API Endpoints**  
   - GET / → shows a welcome message and basic usage info  
   - POST /classify → main endpoint that accepts JSON with a "text" field and returns the classification + details

5. **Response**  
   Includes:  
   - the original text  
   - the assigned category ("hateful", "neutral", or "friendly")  
   - a confidence value (based on how strong the sentiment score is)  
   - the raw compound score  
   - breakdown of negative / neutral / positive portions

## How to Adapt or Extend It Later

You can easily modify the behavior without touching complicated machine-learning code. Here are the most common ways users change it:

### 1. Change how strict the categories are
- Adjust the threshold values (currently -0.5 and +0.5).  
  → Make it more sensitive: lower the numbers (e.g., -0.3 and +0.3)  
  → Make it stricter: increase them (e.g., -0.7 and +0.7)

### 2. Add more categories
- Introduce new labels like "very hateful", "mildly positive", etc.  
- Just add more conditions based on the compound score ranges.

### 3. Make "hateful" stronger by combining with keyword checks
- Add a list of bad words or phrases.  
- If any appear, force the result to "hateful" even if the sentiment score is only mildly negative.

### 4. Support other languages
- VADER works best for English.  
- For other languages, you can later swap the analyzer for a different NLTK or TextBlob sentiment tool that supports your target language.

### 5. Improve accuracy for your specific use case
- Keep a log of classified texts and their results.  
- Manually review edge cases and tweak thresholds or add custom rules for phrases that VADER gets wrong.

### 6. Add extra features
Common additions people make:  
- Rate limiting (prevent spam)  
- API key authentication  
- Logging (save every request to a file/database)  
- Batch processing (classify multiple texts at once)  
- Return only the category (strip extra details for faster responses)

### 7. Deploy it somewhere
Once you're happy with the logic:  
- Run it on a free platform like Render, Fly.io, Railway, or Heroku  
- Put it behind a reverse proxy (nginx) with HTTPS  
- Containerize it with Docker for easier deployment

## Why This Approach?
- Extremely lightweight (no GPU, no big downloads after setup)  
- Easy to understand and modify (no black-box ML model)  
- Good enough for many casual or prototype use cases  
- Fast response times even on low-end hardware

If you later need much higher accuracy (especially for subtle hate speech), you can replace the VADER part with a fine-tuned transformer model — but that's a bigger step and not needed for most simple applications.

Feel free to start with this version and tweak it as your needs evolve!