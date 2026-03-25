// API Configuration
// Works with environment variables set in Vercel dashboard

function getApiBaseURL() {
  if (typeof window === 'undefined') return '';
  
  // Check if running on Vercel (production)
  if (window.location.hostname.includes('vercel.app') || window.location.hostname.includes('yourdomain.com')) {
    return window.__API_BASE__ || 'https://texandco-backend.vercel.app';
  }
  
  // Local development
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    return 'http://localhost:5000';
  }
  
  // Fallback to environment variable
  return 'https://texandco-backend.vercel.app';
}

const API_BASE_URL = getApiBaseURL();

const API_ENDPOINTS = {
  health: `${API_BASE_URL}/api/health`,
  products: `${API_BASE_URL}/api/products`,
  orders: `${API_BASE_URL}/api/orders`,
  cart: `${API_BASE_URL}/api/cart`
};

console.log('API Base URL:', API_BASE_URL);

// Export for use in other modules (if needed)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { API_BASE_URL, API_ENDPOINTS };
}
