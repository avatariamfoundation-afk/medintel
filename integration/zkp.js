async function generateProof(data) {
    return { proof: 'placeholder-proof', publicSignals: [data] };
}

async function verifyProof(proof, publicSignals) {
    return true;
}

module.exports = { generateProof, verifyProof };
