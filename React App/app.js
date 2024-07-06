import React, { useState } from 'react';
import VacancyList from './components/VacancyList';
import CandidateList from './components/CandidateList';
import Analytics from './components/Analytics';

function App() {
  const [view, setView] = useState('vacancies');

  return (
    <div className="App">
      <header>
        <h1>Job and Candidate Portal</h1>
        <nav>
          <button onClick={() => setView('vacancies')}>Vacancies</button>
          <button onClick={() => setView('candidates')}>Candidates</button>
          <button onClick={() => setView('analytics')}>Analytics</button>
        </nav>
      </header>
      <main>
        {view === 'vacancies' && <VacancyList />}
        {view === 'candidates' && <CandidateList />}
        {view === 'analytics' && <Analytics />}
      </main>
    </div>
  );
}

export default App;
