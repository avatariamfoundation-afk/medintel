const CryptoJS = require('crypto-js');
const config = require('../config/app');

class MedicalData {
    constructor(patientId, postOpData, agentId) {
        if (!patientId) throw new Error('Patient ID required');
        this.patientId = patientId;
        this.postOpData = postOpData;
        this.agentId = agentId;
        this.encrypted = false;
        this.timestamp = new Date().toISOString();
        this.auditLog = [];
    }

    encrypt() {
        if (this.encrypted) throw new Error('Already encrypted');
        const key = config.encryptionKey;
        this.encryptedData = CryptoJS.AES.encrypt(JSON.stringify(this), key).toString();
        this.encrypted = true;
        this.auditLog.push({ action: 'encrypted', timestamp: new Date().toISOString() });
    }

    toJSON() {
        if (this.encrypted) {
            return { encryptedData: this.encryptedData, auditLog: this.auditLog };
        }
        return {
            patientId: this.patientId,
            postOpData: this.postOpData,
            agentId: this.agentId,
            timestamp: this.timestamp,
            auditLog: this.auditLog,
        };
    }
}

module.exports = MedicalData;
