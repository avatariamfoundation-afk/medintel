const express = require('express');
const rateLimit = require('express-rate-limit');  // Add to package.json if not present
const axios = require('axios');
require('dotenv').config();

const app = express();
app.use(express.json());

// Rate limiter to prevent overload (10 requests per minute)
const limiter = rateLimit({
  windowMs: 60 * 1000,  // 1 minute
  max: 10,  // Limit each IP to 10 requests per windowMs
  message: 'Too many requests, please try again later.',
});
app.use('/predict', limiter);

// This endpoint handles AI predictions for medical data
app.post('/predict', async (req, res) => {
  try {
    const { data } = req.body;
    if (!data || typeof data !== 'string') {
      return res.status(400).json({ error: 'Valid data string required (e.g., symptoms)' });
    }
    const response = await axios.post('https://api-inference.huggingface.co/models/your-model', {
      inputs: data,
    }, {
      headers: { Authorization: `Bearer ${process.env.MEDICAL_AI_API_KEY}` },
      timeout: 10000,  // 10-second timeout for performance
    });
    res.json({ prediction: response.data });
  } catch (error) {
    console.error('Prediction error:', error.message);
    res.status(500).json({ error: 'Prediction failed - check API key or try again' });
  }
});

app.listen(3000, () => console.log('MedIntel API running on port 3000'));
