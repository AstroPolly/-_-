import React, { useState, useEffect } from 'react';
import axios from 'axios';

function CandidateList() {
  const [candidates, setCandidates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/candidates')
      .then(response => {
        setCandidates(response.data.items);
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
      <h2>Candidates</h2>
      <ul>
        {candidates.map(candidate => (
          <li key={candidate.id}>
            <h3>{candidate.full_name}</h3>
            <p>{candidate.position}</p>
            <p>Skills: {candidate.skills}</p>
            <p>Format: {candidate.employment_format}</p>
            <p>Created at: {new Date(candidate.created_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CandidateList;
