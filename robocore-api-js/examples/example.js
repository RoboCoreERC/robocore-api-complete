const RobotClient = require('./lib/client');

(async () => {
  const client = new RobotClient('ws://robot.local:8765');
  await client.connect();
  client.moveForward(1.0);
  const sensors = await client.readSensors();
  console.log('Sensors:', sensors);
  client.disconnect();
})();
