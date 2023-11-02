// redis client subscriber

const redis = require('redis');
const client = redis.createClient();

client.subscribe('holberton school channel');
client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
  })
  .on('message', (channel, message) => {
    console.log(`Received message on channel ${channel}: ${message}`);

    if (message === 'KILL_SERVER') {
      client.unsubscribe('holberton school channel');
      client.quit();
    }
  });
