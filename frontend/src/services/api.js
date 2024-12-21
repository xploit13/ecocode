import axios from "axios";

const API_BASE_URL = "http://localhost:5000/api";

/**
 * Fetch data from the given endpoint.
 * @param {string} endpoint - API endpoint to fetch data from.
 * @returns {Promise} - Response data from the API.
 */
export const fetchData = async (endpoint) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${endpoint}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Post data to the given endpoint.
 * @param {string} endpoint - API endpoint to post data to.
 * @param {object} data - Data to send to the API.
 * @returns {Promise} - Response data from the API.
 */
export const postData = async (endpoint, data) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/${endpoint}`, data);
    return response.data;
  } catch (error) {
    console.error("Error posting data:", error);
    throw error;
  }
};
