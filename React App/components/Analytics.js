import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Analytics() {
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/analytics')
      .then(response => {
        setAnalytics(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <h2>Analytics</h2>
      <p>Vacancies count: {analytics.vacancies_count}</p>
      <p>Candidates count: {analytics.candidates_count}</p>
      <p>Candidates per vacancy: {analytics.candidates_per_vacancy}</p>
    </div>
  );
}

export default Analytics;
