const { ethers } = require("hardhat");

async function main() {
    console.log("Deploying MedIntel contracts for NeuroGrid...");

    const MedToken = await ethers.getContractFactory("MedToken");
    const medToken = await MedToken.deploy();
    await medToken.deployed();
    console.log("MedToken deployed to:", medToken.address);

    const MedIntel = await ethers.getContractFactory("MedIntel");
    const medIntel = await MedIntel.deploy(medToken.address);
    await medIntel.deployed();
    console.log("MedIntel deployed to:", medIntel.address);

    const config = require('../config/app');
    config.tokenContractAddress = medToken.address;
    const fs = require('fs');
    fs.writeFileSync('./config/app.js', `module.exports = ${JSON.stringify(config, null, 2)};`);
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
