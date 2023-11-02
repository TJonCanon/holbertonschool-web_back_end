// Test suite for Sinon spy

const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('checks to see if the math used in sendPaymentRequestToApi(100, 20) is the same as Utils.calculateNumber("SUM", 100, 20)', () => {
    const spyUtils = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');
    // make desired response
    const res = sendPaymentRequestToApi(100, 20);
    // set expectations
    expect(spyUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 10')).to.be.true;
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(10);
    expect(res).to.equal(10);
    // remove spies from methods
    spyUtils.restore();
    consoleSpy.restore();
  });
});
