import React, { useState } from "react";

/**
 * ProcessTable Component
 * Displays a table of process-related data with sorting and filtering functionality.
 */
const ProcessTable = () => {
  const [processes, setProcesses] = useState([
    { id: 1, name: "Process A", energyUsage: 120, status: "Running" },
    { id: 2, name: "Process B", energyUsage: 80, status: "Idle" },
    { id: 3, name: "Process C", energyUsage: 150, status: "Running" },
  ]);

  const [filter, setFilter] = useState("");
  const [sortKey, setSortKey] = useState("id");
  const [sortOrder, setSortOrder] = useState("asc");

  const handleFilterChange = (event) => {
    setFilter(event.target.value.toLowerCase());
  };

  const handleSort = (key) => {
    const newOrder = sortOrder === "asc" ? "desc" : "asc";
    setSortKey(key);
    setSortOrder(newOrder);

    const sortedProcesses = [...processes].sort((a, b) => {
      if (newOrder === "asc") {
        return a[key] > b[key] ? 1 : -1;
      }
      return a[key] < b[key] ? 1 : -1;
    });

    setProcesses(sortedProcesses);
  };

  const filteredProcesses = processes.filter((process) =>
    process.name.toLowerCase().includes(filter)
  );

  return (
    <div className="process-table">
      <h3>Process Data</h3>
      <input
        type="text"
        placeholder="Filter by name"
        value={filter}
        onChange={handleFilterChange}
        style={{ marginBottom: "10px", padding: "5px", width: "100%" }}
      />
      <table
        border="1"
        style={{ width: "100%", textAlign: "left", borderCollapse: "collapse" }}
      >
        <thead>
          <tr>
            <th onClick={() => handleSort("id")}>ID</th>
            <th onClick={() => handleSort("name")}>Name</th>
            <th onClick={() => handleSort("energyUsage")}>Energy Usage</th>
            <th onClick={() => handleSort("status")}>Status</th>
          </tr>
        </thead>
        <tbody>
          {filteredProcesses.map((process) => (
            <tr key={process.id}>
              <td>{process.id}</td>
              <td>{process.name}</td>
              <td>{process.energyUsage} J</td>
              <td>{process.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProcessTable;
