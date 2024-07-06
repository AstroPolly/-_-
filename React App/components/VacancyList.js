import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VacancyList() {
  const [vacancies, setVacancies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/vacancies')
      .then(response => {
        setVacancies(response.data.items);
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
      <h2>Vacancies</h2>
      <ul>
        {vacancies.map(vacancy => (
          <li key={vacancy.id}>
            <h3>{vacancy.title}</h3>
            <p>{vacancy.description}</p>
            <p>Salary: {vacancy.salary_from} - {vacancy.salary_to}</p>
            <p>Format: {vacancy.employment_format}</p>
            <p>Created at: {new Date(vacancy.created_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default VacancyList;
