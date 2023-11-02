// Connect to Redis server asynchronously

// require('@babel/register');

const redis = require('redis');
const client = redis.createClient();
const { promisify } = require('util');

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

const setNewSchool = async (schoolName, value) => {
  await setAsync(schoolName, value);
  redis.print('Reply: OK');
};

const displaySchoolValue = async (schoolName) => {
  const res = await getAsync(schoolName);
  console.log(res);
};


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
