const config = require('../config/app');

class Agent {
    constructor(id, type = 'autonomous') {
        if (!id) throw new Error('Agent ID required');
        this.id = id;
        this.type = type;
        this.capabilities = config.agentCapabilities;
        this.tasks = [];
        this.status = 'idle';
        this.auditLog = [];
    }

    assignTask(task) {
        this.tasks.push(task);
        this.status = 'active';
        this.auditLog.push({ action: 'task assigned', task, timestamp: new Date().toISOString() });
    }

    executeTask() {
        if (this.tasks.length === 0) throw new Error('No tasks');
        const task = this.tasks.shift();
        if (this.tasks.length === 0) this.status = 'idle';
        return `Executed: ${task}`;
    }

    toJSON() {
        return {
            id: this.id,
            type: this.type,
            capabilities: this.capabilities,
            status: this.status,
            tasks: this.tasks,
            auditLog: this.auditLog,
        };
    }
}

module.exports = Agent;
