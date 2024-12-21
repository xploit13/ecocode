import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

/**
 * Fetch data from the given endpoint.
 * @param {string} endpoint - API endpoint to fetch data from.
 * @param {object} [params={}] - Optional query parameters.
 * @returns {Promise} - Response data from the API.
 */
export const fetchData = async (endpoint, params = {}) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${endpoint}`, { params });
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error.message);
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
    console.error('Error posting data:', error.message);
    throw error;
  }
};

/**
 * Update data at the given endpoint.
 * @param {string} endpoint - API endpoint to update data at.
 * @param {object} data - Data to update.
 * @returns {Promise} - Response data from the API.
 */
export const updateData = async (endpoint, data) => {
  try {
    const response = await axios.put(`${API_BASE_URL}/${endpoint}`, data);
    return response.data;
  } catch (error) {
    console.error('Error updating data:', error.message);
    throw error;
  }
};

/**
 * Delete data at the given endpoint.
 * @param {string} endpoint - API endpoint to delete data at.
 * @returns {Promise} - Response data from the API.
 */
export const deleteData = async (endpoint) => {
  try {
    const response = await axios.delete(`${API_BASE_URL}/${endpoint}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting data:', error.message);
    throw error;
  }
};

/**
 * Handle file uploads to the given endpoint.
 * @param {string} endpoint - API endpoint to upload the file to.
 * @param {File} file - File to upload.
 * @param {object} [additionalData={}] - Additional data to include with the upload.
 * @returns {Promise} - Response data from the API.
 */
export const uploadFile = async (endpoint, file, additionalData = {}) => {
  try {
    const formData = new FormData();
    formData.append('file', file);
    Object.keys(additionalData).forEach((key) => {
      formData.append(key, additionalData[key]);
    });

    const response = await axios.post(`${API_BASE_URL}/${endpoint}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    return response.data;
  } catch (error) {
    console.error('Error uploading file:', error.message);
    throw error;
  }
};
