module.exports = {
  port: process.env.PORT || 3000,
  bnbRpcUrl: process.env.BNB_RPC_URL,
  encryptionKey: process.env.ENCRYPTION_KEY,  // For data encryption
  p2pPort: process.env.P2P_PORT || 3001,  // For future P2P networking
  aiApiKey: process.env.MEDICAL_AI_API_KEY,
  // Future scalability: Add cross-chain config here
};
