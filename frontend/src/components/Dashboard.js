import React, { useState } from 'react';
import Alerts from './Alerts';
import ProcessTable from './ProcessTable';
import Widgets from './Widgets';

/**
 * Dashboard Component
 * Displays the main dashboard with alerts, widgets, and a process table.
 */
const Dashboard = () => {
  const [alerts, setAlerts] = useState([
    { type: 'info', message: 'System is running smoothly.', title: 'Info' },
    { type: 'warning', message: 'High energy consumption detected.', title: 'Warning' },
    { type: 'error', message: 'A critical error occurred.', title: 'Error' },
  ]);

  const dismissAlert = (index) => {
    setAlerts((prevAlerts) => prevAlerts.filter((_, i) => i !== index));
  };

  const handleAddAlert = () => {
    setAlerts((prevAlerts) => [
      ...prevAlerts,
      { type: 'success', message: 'New alert added!', title: 'Success' },
    ]);
  };

  return (
    <div className="dashboard">
      <header>
        <h1>EcoCode Dashboard</h1>
        <button
          onClick={handleAddAlert}
          style={{ padding: '10px', margin: '10px', backgroundColor: '#007bff', color: '#fff', border: 'none' }}
        >
          Add Alert
        </button>
      </header>
      <Alerts alerts={alerts} onDismiss={dismissAlert} />
      <Widgets />
      <ProcessTable />
    </div>
  );
};

export default Dashboard;
