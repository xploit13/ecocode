import React from 'react';
import PropTypes from 'prop-types';

/**
 * Alerts Component
 * Displays a list of alerts with different types and supports dismiss functionality.
 */
const Alerts = ({ alerts, onDismiss }) => {
  if (!alerts || alerts.length === 0) {
    return <p>No alerts to display.</p>;
  }

  return (
    <div className="alerts">
      {alerts.map((alert, index) => (
        <div
          key={index}
          className={`alert alert-${alert.type}`}
          style={{ border: `2px solid ${getAlertBorderColor(alert.type)}`, marginBottom: '10px', padding: '10px' }}
        >
          <strong>{alert.title || 'Alert'}:</strong> {alert.message}
          {onDismiss && (
            <button
              onClick={() => onDismiss(index)}
              style={{ marginLeft: '10px', cursor: 'pointer', backgroundColor: '#ccc', border: 'none', padding: '5px' }}
            >
              Dismiss
            </button>
          )}
        </div>
      ))}
    </div>
  );
};

/**
 * Get border color based on alert type.
 * @param {string} type - Alert type (e.g., 'info', 'warning', 'error').
 * @returns {string} - Corresponding border color.
 */
const getAlertBorderColor = (type) => {
  switch (type) {
    case 'info':
      return '#007bff';
    case 'warning':
      return '#ffc107';
    case 'error':
      return '#dc3545';
    case 'success':
      return '#28a745';
    default:
      return '#6c757d';
  }
};

Alerts.propTypes = {
  alerts: PropTypes.arrayOf(
    PropTypes.shape({
      type: PropTypes.oneOf(['info', 'warning', 'error', 'success']).isRequired,
      message: PropTypes.string.isRequired,
      title: PropTypes.string,
    })
  ),
  onDismiss: PropTypes.func,
};

export default Alerts;
