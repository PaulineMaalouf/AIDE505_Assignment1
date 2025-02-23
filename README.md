# Sentiment Analysis API

This project consists of two components:
1. A **Flask API** that serves a sentiment analysis model using `vaderSentiment`.
2. An **Express.js API** that forwards user requests to the Flask API.

## Project Structure
```
flask-api/
    app.py  # Flask API
express-server/
    index.js  # Express.js API
README.md
```

## Setup Instructions

### 1. Setting up the Flask API
#### Prerequisites
- Python 3.x
- `pip` installed

#### Installation
```sh
cd flask-api
pip install flask vaderSentiment
python app.py
```
This will start the Flask server on `http://127.0.0.1:5000`

### 2. Setting up the Express.js API
#### Prerequisites
- Node.js installed

#### Installation
```sh
cd express-server
npm init -y
npm install express axios body-parser
node index.js
```
This will start the Express server on `http://127.0.0.1:3000`

## Usage

### Sending a request to the Express API
```sh
curl -X POST http://127.0.0.1:3000/analyze-sentiment -H "Content-Type: application/json" -d '{"text": "I love programming!"}'
```

### Expected Response
```json
{
    "sentiment": "positive"
}
```

## Deployment
For deployment, consider using Docker or cloud platforms like Heroku, AWS, or GCP.

## License
This project is open-source and available under the MIT License.

