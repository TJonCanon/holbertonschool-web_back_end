// a very promising test suite
const { expect } = require('chai');
const getPaymentTokenFromApi = require('./6-payment_token');

describe('getPaymentTokenFromApi', () => {
  it('returns a resolved promise', (done) => {
    getPaymentTokenFromApi(true)
      .then((res) => {
        expect(res).to.eql({
          data: 'Successful response from the API',
        });
        done();
      })
      .catch((err) => {
        done(err);
      });
  });
});
