import React from "react";

const Widgets = () => {
  const widgetData = [
    { id: 1, title: "Total Energy Usage", value: "350 J", unit: "Joules" },
    { id: 2, title: "Active Processes", value: "5", unit: "" },
    { id: 3, title: "Eco Efficiency", value: "85%", unit: "" },
  ];

  return (
    <div className="widgets">
      <h3>Dashboard Widgets</h3>
      <div className="widget-container">
        {widgetData.map((widget) => (
          <div key={widget.id} className="widget">
            <h4>{widget.title}</h4>
            <p>
              {widget.value} {widget.unit}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Widgets;
