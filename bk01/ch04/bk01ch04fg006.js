// validatePhoneNumber.js
function validatePhoneNumber(phoneNumber) {
  // Return validation result with meaningful error messages
  const result = {
    isValid: false,
    message: '',
    normalized: '',
  };

  // Check if input is provided
  if (!phoneNumber || typeof phoneNumber !== 'string') {
    result.message = 'Phone number is required and must be a string';
    return result;
  }

  const trimmed = phoneNumber.trim();

  // Check for empty string after trimming
  if (trimmed.length === 0) {
    result.message = 'Phone number cannot be empty';
    return result;
  }

  // Extract digits and check for country code
  const digitsOnly = trimmed.replace(/\D/g, '');
  const hasPlus = trimmed.startsWith('+');

  // Validate based on number of digits
  if (digitsOnly.length < 7) {
    result.message = 'Phone number is too short (minimum 7 digits)';
    return result;
  }

  if (digitsOnly.length > 15) {
    result.message = 'Phone number is too long (maximum 15 digits)';
    return result;
  }

  // US/Canada number validation (10 or 11 digits)
  if (digitsOnly.length === 10) {
    // Standard US 10-digit number
    const areaCode = digitsOnly.substring(0, 3);
    if (areaCode[0] === '0' || areaCode[0] === '1') {
      result.message = 'Invalid US area code (cannot start with 0 or 1)';
      return result;
    }
    result.isValid = true;
    result.message = 'Valid US/Canada phone number';
    result.normalized = `(${digitsOnly.substring(0, 3)}) ${digitsOnly.substring(3, 6)}-${digitsOnly.substring(6)}`;
    return result;
  }

  if (digitsOnly.length === 11 && digitsOnly[0] === '1') {
    // US number with country code
    const areaCode = digitsOnly.substring(1, 4);
    if (areaCode[0] === '0' || areaCode[0] === '1') {
      result.message = 'Invalid US area code (cannot start with 0 or 1)';
      return result;
    }
    result.isValid = true;
    result.message = 'Valid US/Canada phone number with country code';
    result.normalized = `+1 (${digitsOnly.substring(1, 4)}) ${digitsOnly.substring(4, 7)}-${digitsOnly.substring(7)}`;
    return result;
  }

  // International number validation
  if (digitsOnly.length >= 7 && digitsOnly.length <= 15) {
    result.isValid = true;
    result.message = 'Valid international phone number';
    result.normalized = hasPlus ? `+${digitsOnly}` : digitsOnly;
    return result;
  }

  // If we reach here, something unexpected happened
  result.message = 'Invalid phone number format';
  return result;
}

module.exports = validatePhoneNumber;
