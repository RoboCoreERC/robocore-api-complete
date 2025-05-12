const WebSocket = require('ws');

class RobotClient {
  constructor(uri) {
    this.uri = uri;
    this.ws  = null;
  }

  connect() {
    return new Promise((resolve, reject) => {
      this.ws = new WebSocket(this.uri);
      this.ws.on('open', () => resolve());
      this.ws.on('error', reject);
    });
  }

  disconnect() {
    if (this.ws) this.ws.close();
  }

  moveForward(speed) {
    this.ws.send(`MOVE_FORWARD ${speed}`);
  }

  readSensors() {
    return new Promise(resolve => {
      this.ws.once('message', data => resolve(data));
      this.ws.send('READ_SENSORS');
    });
  }
}

module.exports = RobotClient;
