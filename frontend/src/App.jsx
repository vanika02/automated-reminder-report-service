import { useEffect, useState } from "react";

function App() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/analytics/")
    .then(res => res.json())
    .then(data => setStats(data))
  }, []);

  if (!stats) return <p>Loading...</p>;

  return (
    <div>
      <h1>Reminder Analytics</h1>
      <p>Total: {stats.total}</p>
      <p>Total: {stats.active}</p>
      <p>Total: {stats.inactive}</p>
      <p>Total: {stats.today}</p>
    </div>
  );
}

export default App;