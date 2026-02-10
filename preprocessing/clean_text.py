import re
import string

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


if __name__ == "__main__":
    sample = "This is a SAMPLE text! Visit https://example.com"
    print(clean_text(sample))
