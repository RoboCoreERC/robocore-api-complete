#!/usr/bin/env node
const { program } = require('commander');
const RobotClient = require('./lib/client');

program
  .command('info <uri>')
  .description('Show sensor data')
  .action(async uri => {
    console.log(`Connecting to ${uri}…`);
    const client = new RobotClient(uri);
    await client.connect();
    const data = await client.readSensors();
    console.log(`Sensors: ${data}`);
    client.disconnect();
  });

program
  .command('forward <uri> <speed>')
  .description('Move forward at specified speed (m/s)')
  .action(async (uri, speed) => {
    console.log(`Moving ${uri} forward at ${speed} m/s…`);
    const client = new RobotClient(uri);
    await client.connect();
    client.moveForward(parseFloat(speed));
    console.log('Done.');
    client.disconnect();
  });

program.parse(process.argv);
