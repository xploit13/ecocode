import React from "react";
import Alerts from "./Alerts";
import ProcessTable from "./ProcessTable";
import Widgets from "./Widgets";

const Dashboard = () => {
  const alerts = [
    { type: "info", message: "System is running smoothly." },
    { type: "warning", message: "High energy consumption detected." },
  ];

  return (
    <div className="dashboard">
      <h2>EcoCode Dashboard</h2>
      <Alerts alerts={alerts} />
      <Widgets />
      <ProcessTable />
    </div>
  );
};

export default Dashboard;
