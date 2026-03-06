// validatePhoneNumber.js
function validatePhoneNumber(phoneNumber) {
  // Regular expression to match the format (XXX) XXX-XXXX
  const phoneRegex = /^\(\d{3}\) \d{3}-\d{4}$/;
  return phoneRegex.test(phoneNumber);
}

module.exports = validatePhoneNumber;
