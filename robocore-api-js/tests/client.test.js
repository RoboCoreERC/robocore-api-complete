// robocore-api-js/tests/client.test.js

// Mock the 'ws' module with a dummy WebSocket class
jest.mock('ws', () => {
  return class {
    constructor() {
      this._callbacks = {};
      // simulate open event
      setTimeout(() => {
        if (this._callbacks.open) this._callbacks.open();
      }, 0);
    }
    on(event, cb) {
      this._callbacks[event] = cb;
    }
    once(event, cb) {
      this._callbacks[event] = cb;
    }
    send(msg) {
      // when READ_SENSORS is sent, trigger the 'message' callback
      if (msg === 'READ_SENSORS' && this._callbacks.message) {
        setTimeout(() => this._callbacks.message('OK'), 0);
      }
    }
    close() {}
  };
});

const RobotClient = require('../lib/client');

test('client methods', async () => {
  const client = new RobotClient('ws://test');
  await client.connect();               // calls .on('open', …)
  client.moveForward(0.5);              // fires send()
  const data = await client.readSensors();  // sets once('message', …) then send()
  expect(data).toBe('OK');
  client.disconnect();
});
