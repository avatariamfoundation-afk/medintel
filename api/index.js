const express = require('express');
const axios = require('axios');
require('dotenv').config();

const app = express();
app.use(express.json());

// Endpoint for medical AI predictions (e.g., using a free API like Hugging Face)
app.post('/predict', async (req, res) => {
  try {
    const { data } = req.body;  // e.g., patient symptoms
    const response = await axios.post('https://api-inference.huggingface.co/models/your-model', {
      inputs: data,
    }, {
      headers: { Authorization: `Bearer ${process.env.MEDICAL_AI_API_KEY}` }
    });
    res.json({ prediction: response.data });
  } catch (error) {
    res.status(500).json({ error: 'Prediction failed' });
  }
});

app.listen(3000, () => console.log('MedIntel API running on port 3000'));
