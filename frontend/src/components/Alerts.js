import React from "react";

const Alerts = ({ alerts }) => {
  return (
    <div className="alerts">
      {alerts.length > 0 ? (
        alerts.map((alert, index) => (
          <div key={index} className={`alert alert-${alert.type}`}>
            {alert.message}
          </div>
        ))
      ) : (
        <p>No alerts to display.</p>
      )}
    </div>
  );
};

export default Alerts;
