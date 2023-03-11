from textblob import TextBlob


feedback = "The lesson was interesting, but the teacher seemed stressed."
def analyse_polarity(user_data):
    blob = TextBlob(feedback)
    polarity = blob.sentiment.polarity

    if polarity < -0.5:
        results = "Very Negative"
    elif polarity < 0:
        results = "SomeHow Negative Feelings"
    elif polarity == 0:
        results = "Neutral Feelings"
    elif polarity < 0.5:
        results = "Positive Feelings"
    else:
        results = "Very Positive"

    return results

if __name__ == "__main__":
    pol = analyse_polarity("I found the Lesson soo touch especially because I was unfamilier with the students!.")
    print(f"Polarity of the text is  {pol}")
