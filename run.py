from flask import Flask, request
import json

from generate_summary import generate_summary
from parse_article import parse_article

app = Flask(__name__)

@app.route('/api/summary', methods = ['POST'])
def get_summary():
    """ Returns a summary of an article found at a given url """
    # Parse url from form response
    req = request.form.to_dict()
    memory = json.loads(req['Memory'])
    url = memory['twilio']['collected_data']['summarize_article']['answers']['article_url']['answer']

    # Parse article text
    text = parse_article(url)

    # Generate summary
    summary = generate_summary(text)

    # Return summary
    actions = {
        "actions": [
            {
                "say": summary
            }
        ]
    }
    return actions

if __name__ == "__main__":
    app.run(debug = True)