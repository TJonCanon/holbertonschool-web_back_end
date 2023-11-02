// Creating an object with job data using Kue

const kue = require('kue');
const queue = kue.createQueue();

// Create an object with job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'thinking about thos beans',
};

// Create the queue named push_notification_code
const pushNotificationQueue = queue.create('push_notification_code', jobData);

// Save the job to the queue
pushNotificationQueue.save(function (error) {
  if (error) {
    console.error('Failed to save job:', error);
  } else {
    console.log(`Notification job created: ${pushNotificationQueue.id}`);
  }
});
