import React from 'react';
import './App.css';
import LoginButton from './components/LoginButton';
import LogoutButton from './components/LogoutButton';
import Start_section from './components/Start_section';


function App() {
  
  return (
    <div className="App">
      <h1>Job Application Tracker</h1>
        <LoginButton />
        <LogoutButton />
        <Start_section />
    </div>
  );
}

export default App;
