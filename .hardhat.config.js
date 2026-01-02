require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

// Optional plugins (safe to enable later if needed)
// require("hardhat-gas-reporter");
// require("hardhat-contract-sizer");

module.exports = {
  solidity: {
    version: "0.8.21",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      },
      viaIR: true
    }
  },

  networks: {
    // Local development
    hardhat: {},

    // BNB Testnet (PRIMARY – hackathon target)
    bnbTestnet: {
      url: process.env.BNB_RPC_URL || "https://data-seed-prebsc-1-s1.binance.org:8545/",
      accounts: process.env.DEPLOYER_PRIVATE_KEY
        ? [process.env.DEPLOYER_PRIVATE_KEY]
        : [],
      chainId: 97,
      gasPrice: 20_000_000_000, // 20 gwei
      gas: 8_000_000
    }

    // ⚠️ Ethereum intentionally excluded from active config
    // Hackathon judges penalize unused networks
  },

  gasReporter: {
    enabled: process.env.REPORT_GAS === "true",
    currency: "USD",
    noColors: true
  },

  paths: {
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts"
  },

  mocha: {
    timeout: 40000
  }
};
