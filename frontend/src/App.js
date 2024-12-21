import React, { useEffect, useState } from "react";
import "./App.css";
import Dashboard from "./components/Dashboard";
import { initializeSocket, subscribeToEvent } from "./services/socket";

/**
 * App Component
 * Main entry point for the application with real-time WebSocket integration.
 */
const App = () => {
  const [notifications, setNotifications] = useState([]);
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const socketInstance = initializeSocket();
    setSocket(socketInstance);

    subscribeToEvent(socketInstance, "notification", (data) => {
      setNotifications((prev) => [...prev, data]);
    });

    return () => {
      if (socketInstance) {
        socketInstance.disconnect();
      }
    };
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to EcoCode Dashboard</h1>
      </header>
      <main>
        <Dashboard />
        {notifications.length > 0 && (
          <div className="notifications">
            <h3>Real-Time Notifications</h3>
            <ul>
              {notifications.map((notif, index) => (
                <li key={index}>{notif.message}</li>
              ))}
            </ul>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
