// test suite for index
const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  it('should return correct status code and result for /', (done) => {
    request('http://localhost:7865', (err, res, text) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      expect(text).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('returns correctly for /cart/:id when id is number', (done) => {
    request('http://localhost:7865/cart/69', (err, res, text) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      expect(text).to.equal('Payment methods for cart 69');
      done();
    });
  });

  it('returns correctly for /cart/:id when id is NaN', (done) => {
    request('http://localhost:7865/cart/nan', (err, res, text) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
