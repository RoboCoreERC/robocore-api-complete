// robocore-api-js/tests/client.test.js

// Mock the 'ws' module by returning a Dummy WebSocket class inside the factory.
jest.mock('ws', () => {
  return class {
    constructor() {
      // emulate async open event
      setTimeout(() => this.onopen(), 0);
    }
    send(msg) {
      // when 'READ_SENSORS' is sent, emit a 'message' with 'OK'
      if (msg === 'READ_SENSORS') {
        setTimeout(() => this.onmessage({ data: 'OK' }), 0);
      }
    }
    close() {}
    // placeholders for event handlers
    onopen() {}
    onmessage() {}
  };
});

const RobotClient = require('../lib/client');

test('client methods', async () => {
  const client = new RobotClient('ws://test');
  await client.connect();
  client.moveForward(0.5);
  const data = await client.readSensors();
  expect(data).toBe('OK');
  client.disconnect();
});
