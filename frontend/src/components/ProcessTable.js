import React from "react";

const ProcessTable = () => {
  const processes = [
    { id: 1, name: "Process A", energyUsage: "120 J", status: "Running" },
    { id: 2, name: "Process B", energyUsage: "80 J", status: "Idle" },
    { id: 3, name: "Process C", energyUsage: "150 J", status: "Running" },
  ];

  return (
    <div className="process-table">
      <h3>Process Data</h3>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Energy Usage</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {processes.map((process) => (
            <tr key={process.id}>
              <td>{process.id}</td>
              <td>{process.name}</td>
              <td>{process.energyUsage}</td>
              <td>{process.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProcessTable;
