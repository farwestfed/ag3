import './App.css';
import WeatherDamageDashboard from './components/WeatherDamageDashboard';

function App() {
  return (
    <div className="App">
      <div className="army-header">
        <img src="/army_header_banner.png" alt="U.S. Army" className="army-logo" />
      </div>
      <div className="yellow-bar"></div>
      <div className="asa-header">
        <div className="asa-logo-container">
          <img src="/asa_ie_logo.png" alt="ASA(IE&E)" className="asa-logo" />
          <span className="asa-text">ASA(IE&E)</span>
        </div>
      </div>
      <WeatherDamageDashboard />
    </div>
  );
}

export default App;
