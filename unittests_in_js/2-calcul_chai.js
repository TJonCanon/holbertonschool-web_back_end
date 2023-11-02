/* rounds a & b and returns their sum */
function calculateNumber(type, a, b) {
    // check that args are numbers
    if (isNaN(a) || isNaN(b)) {
      throw TypeError('Parameters must be numbers');
    }
    // return the result
    if (type === 'SUM') return Math.round(a) + Math.round(b);
    if (type === 'SUBTRACT') return Math.round(a) - Math.round(b);
    if (type === 'DIVIDE') {
      if (Math.round(a) === 0 || Math.round(b) === 0) {
        return 'Error';
      }
      return Math.round(a) / Math.round(b);
    }
  }
  
  module.exports = calculateNumber;
  