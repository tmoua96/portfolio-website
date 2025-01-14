from langdetect import detect, LangDetectException

def is_english(text: str) :
    try:
        return detect(text) == "en"
    except LangDetectException:
        return False