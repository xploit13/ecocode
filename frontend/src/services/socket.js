import { io } from 'socket.io-client';

const SOCKET_SERVER_URL = 'http://localhost:5000';

/**
 * Initialize a WebSocket connection.
 * @returns {Socket} - The initialized WebSocket connection.
 */
export const initializeSocket = () => {
  const socket = io(SOCKET_SERVER_URL);

  socket.on('connect', () => {
    console.log('WebSocket connected:', socket.id);
  });

  socket.on('disconnect', () => {
    console.log('WebSocket disconnected');
  });

  socket.on('error', (error) => {
    console.error('WebSocket error:', error);
  });

  return socket;
};

/**
 * Subscribe to a specific WebSocket event.
 * @param {Socket} socket - The WebSocket connection.
 * @param {string} event - Event name to subscribe to.
 * @param {function} callback - Callback function to handle event data.
 */
export const subscribeToEvent = (socket, event, callback) => {
  socket.on(event, callback);
  console.log(`Subscribed to WebSocket event: ${event}`);
};

/**
 * Emit data to a specific WebSocket event.
 * @param {Socket} socket - The WebSocket connection.
 * @param {string} event - Event name to emit data to.
 * @param {object} data - Data to send with the event.
 */
export const emitEvent = (socket, event, data) => {
  socket.emit(event, data);
  console.log(`Emitted event: ${event} with data:`, data);
};

/**
 * Unsubscribe from a specific WebSocket event.
 * @param {Socket} socket - The WebSocket connection.
 * @param {string} event - Event name to unsubscribe from.
 */
export const unsubscribeFromEvent = (socket, event) => {
  socket.off(event);
  console.log(`Unsubscribed from WebSocket event: ${event}`);
};

/**
 * Reconnect the WebSocket connection.
 * @param {Socket} socket - The WebSocket connection.
 */
export const reconnectSocket = (socket) => {
  if (socket.disconnected) {
    socket.connect();
    console.log('WebSocket reconnected');
  }
};
