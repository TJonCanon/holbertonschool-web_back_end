// Test suite using hooks

const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;
  // create a spy on console.log() before each test
  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });
  // restore console.log() after each test
  afterEach(() => {
    consoleSpy.restore();
  });
  // check if console.log() is called with correct arguments
  it('checks if the console.log is called with the right arg', () => {
    const res = sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(res).to.equal(120);
  });
  // check if the console.log is called with other arguments
  it('checks if the console.log is called with the right arg', () => {
    const res = sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(res).to.equal(20);
  });
});
