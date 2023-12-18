import React, { useState, useEffect } from 'react';
import './App.css';

const ChristmasCountdown = () => {
  const christmasDate = new Date('December 25, 2023 00:00:00').getTime();
  const [timeLeft, setTimeLeft] = useState(calculateTimeLeft());

  function calculateTimeLeft() {
    const now = new Date().getTime();
    const difference = christmasDate - now;

    let days = Math.floor(difference / (1000 * 60 * 60 * 24));
    let hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((difference % (1000 * 60)) / 1000);

    return { days, hours, minutes, seconds };
  }

  useEffect(() => {
    const interval = setInterval(() => {
      setTimeLeft(calculateTimeLeft());
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="countdown">
      <h1> Odbrojavanje do Božića</h1>
      <div className="timer">
        <div className="time-box">
          <span>{timeLeft.days}</span>
          <p>Dani</p>
        </div>
        <div className="time-box">
          <span>{timeLeft.hours}</span>
          <p>Sati</p>
        </div>
        <div className="time-box">
          <span>{timeLeft.minutes}</span>
          <p>Minute</p>
        </div>
        <div className="time-box">
          <span>{timeLeft.seconds}</span>
          <p>Sekunde</p>
        </div>
      </div>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <ChristmasCountdown />
    </div>
  );
}

export default App;