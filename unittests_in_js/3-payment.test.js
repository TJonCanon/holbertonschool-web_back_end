// Test suite for Sinon spy

const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('checks to see if the math used in sendPaymentRequestToApi(100, 20) is the same as Utils.calculateNumber("SUM", 100, 20)', () => {
    const spyUtils = sinon.spy(Utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    const res = sendPaymentRequestToApi(100, 20);

    expect(spyUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.be.true;
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(res);

    spyUtils.restore();
    consoleSpy.restore();
  });
});
