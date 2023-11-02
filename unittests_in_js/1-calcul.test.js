// Test suite for 1-calcul.js

const assert = require('assert').strict;
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  it('taking positive numbers', () => {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
    assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.equal(calculateNumber('DIVIDE', 1, 3), 0.3333333333333333);
  });

  it('taking negative numbers', () => {
    assert.equal(calculateNumber('SUM', -1, -3), -4);
    assert.equal(calculateNumber('SUBTRACT', -1, -3), 2);
    assert.equal(calculateNumber('DIVIDE', -1, -3), 0.3333333333333333);
  });

  it('taking positive and negative numbers', () => {
    assert.equal(calculateNumber('SUM', -1, 3), 2);
    assert.equal(calculateNumber('SUBTRACT', -1, 3), -4);
    assert.equal(calculateNumber('DIVIDE', -1, 3), -0.3333333333333333);
  });

  it('taking zeros', () => {
    assert.equal(calculateNumber('SUM', 0, 0), 0);
    assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
    assert.throws(() => calculateNumber(('DIVIDE', 0, 0), 'Error'));
  });
});
