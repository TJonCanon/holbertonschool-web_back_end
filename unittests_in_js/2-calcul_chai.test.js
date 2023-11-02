// Test suite for unit testing project

const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  it('taking positive numbers', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    expect(calculateNumber('DIVIDE', 1, 3)).to.be.closeTo(0.3333333333333333, 0.00000001);
  });

  it('taking negative numbers', () => {
    expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
    expect(calculateNumber('SUBTRACT', -1, -3)).to.equal(2);
    expect(calculateNumber('DIVIDE', -1, -3)).to.be.closeTo(0.3333333333333333, 0.00000001);
  });

  it('taking positive and negative numbers', () => {
    expect(calculateNumber('SUM', -1, 3)).to.equal(2);
    expect(calculateNumber('SUBTRACT', -1, 3)).to.equal(-4);
    expect(calculateNumber('DIVIDE', -1, 3)).to.be.closeTo(-0.3333333333333333, 0.00000001);
  });

  it('taking zeros', () => {
    expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
  });
});
