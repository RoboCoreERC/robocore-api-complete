const RobotClient = require('../lib/client');

test('client methods', async () => {
  class DummyWS {
    constructor() {
      setTimeout(() => this.onopen(), 0);
    }
    send(msg) {
      if (msg === 'READ_SENSORS') {
        setTimeout(() => this.onmessage({ data: 'OK' }), 0);
      }
    }
    close() {}
  }
  jest.mock('ws', () => DummyWS);

  const client = new RobotClient('ws://test');
  await client.connect();
  client.moveForward(0.5);
  const data = await client.readSensors();
  expect(data).toBe('OK');
  client.disconnect();
});
