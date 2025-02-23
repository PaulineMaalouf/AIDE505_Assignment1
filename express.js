const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.post('/analyze-sentiment', async (req, res) => {
    const { text } = req.body;
    if (!text) {
        return res.status(400).json({ error: "No text provided" });
    }

    try {
        const response = await axios.post('http://127.0.0.1:5000/predict', { text });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Error connecting to Flask API" });
    }
});

app.listen(3000, () => {
    console.log('Express server running on port 3000');
});
