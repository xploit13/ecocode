import React, { useState } from "react";

/**
 * Widgets Component
 * Displays a dynamic set of widgets with real-time updates.
 */
const Widgets = () => {
  const [widgetData, setWidgetData] = useState([
    { id: 1, title: "Total Energy Usage", value: 350, unit: "J" },
    { id: 2, title: "Active Processes", value: 5, unit: "" },
    { id: 3, title: "Eco Efficiency", value: 85, unit: "%" },
  ]);

  const refreshWidgets = () => {
    // Simulate fetching updated data
    setWidgetData((prevData) =>
      prevData.map((widget) => ({
        ...widget,
        value: widget.value + Math.floor(Math.random() * 10) - 5, // Simulated fluctuation
      }))
    );
  };

  return (
    <div className="widgets">
      <h3>Dashboard Widgets</h3>
      <button
        onClick={refreshWidgets}
        style={{
          padding: "10px",
          marginBottom: "10px",
          backgroundColor: "#007bff",
          color: "#fff",
          border: "none",
          cursor: "pointer",
        }}
      >
        Refresh Widgets
      </button>
      <div
        className="widget-container"
        style={{ display: "flex", gap: "10px" }}
      >
        {widgetData.map((widget) => (
          <div
            key={widget.id}
            className="widget"
            style={{
              border: "1px solid #ccc",
              padding: "10px",
              borderRadius: "5px",
              textAlign: "center",
              flex: "1",
            }}
          >
            <h4>{widget.title}</h4>
            <p style={{ fontSize: "20px", fontWeight: "bold" }}>
              {widget.value} {widget.unit}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Widgets;
