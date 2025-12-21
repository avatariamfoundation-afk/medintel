require("@nomiclabs/hardhat-waffle");
require("@nomiclabs/hardhat-ethers");
require("dotenv").config();
// Add for gas reporting: require("hardhat-gas-reporter");
// Add for contract sizing: require("hardhat-contract-sizer");

module.exports = {
  solidity: "0.8.19",  // Optimized for security and gas efficiency

  networks: {
    // BNB Testnet for hackathon deployment
    testnet: {
      url: process.env.BNB_RPC_URL,
      accounts: [process.env.PRIVATE_KEY],
      gasPrice: 20000000000,  // Lower gas for cost savings
      gasLimit: 8000000,  // Prevent out-of-gas errors
    },
    // Placeholder for cross-chain (e.g., Ethereum mainnet)
    ethereum: {
      url: process.env.ETHEREUM_RPC_URL || "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
      accounts: [process.env.PRIVATE_KEY],
      gasPrice: 50000000000,  // Adjust for Ethereum costs
    },
  },

  // Plugins for optimization and security
  gasReporter: {
    enabled: process.env.REPORT_GAS !== undefined,
    currency: "USD",
  },
  contractSizer: {
    alphaSort: true,
    disambiguatePaths: false,
    runOnCompile: true,
  },

  // Paths for scalability (e.g., multiple contracts)
  paths: {
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts",
  },

  // Mocha for testing (optimized for quick runs)
  mocha: {
    timeout: 40000,  // 40 seconds to handle slow tests
  },
};
