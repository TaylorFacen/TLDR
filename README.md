# Text Summarizer

This app was written for a talk for Twilio's Signal 2020 Conference. This repo has the following 3 branches:
* starter - Starter code if you want to start from scratch
* extractive-summarization - Example code for extractive summarization
* main - Deployed TLDR app

To follow along, create a virtual environment and install all dependencies

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Then to run the app, run the following
```python
python run.py
```
*Note this step is for the starter and ex-summarization branches only

## Interacting with Autopilot
While working locally, you can use a service like [ngrok](https://ngrok.com) to connect Twilio Autopilot to the API. After using ngrok or another service to make the API publically, accessible, add the public url to line 95 of `summarizer.json` use the Twilio Autopilot CLI to create and / or update an autopilot bot. You can also configure the bot manually on twilio.com. 

For the production deployment of this app, I deployed a serverless function via Google Cloud Functions. Code and requirements for function can be found in the `functions` folder on the `main` branch.