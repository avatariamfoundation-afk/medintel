const axios = require('axios');
require('dotenv').config();

async function getMedicalPrediction(data) {
  try {
    const response = await axios.post('https://api-inference.huggingface.co/models/your-medical-model', {
      inputs: data,
    }, {
      headers: { Authorization: `Bearer ${process.env.MEDICAL_AI_API_KEY}` }
    });
    return response.data;
  } catch (error) {
    console.error('AI integration error:', error);
    return null;
  }
}

module.exports = { getMedicalPrediction };
