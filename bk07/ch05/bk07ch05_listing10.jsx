import React from 'react';
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      location: 'Chicago',
      current_condition: {
        temp_C: 0,
        windspeedKmph: 0,
        precipMM: 0,
      },
    };
  }
  componentDidMount() {
    const getWeatherData = async (city) => {
      const response = await fetch(`https://wttr.in/${city}?format=j1`);
      const weatherData = await response.json();
      this.setState({ current_condition: weatherData.current_condition[0] });
    };
    getWeatherData(this.state.location);
  }
  render() {
    return (
      <div>
        <h1>Today's weather for {this.state.location}</h1>
        <ul>
          <li>temp: {this.state.current_condition.temp_C} C</li>
          <li>wind: {this.state.current_condition.windspeedKmph} km/h</li>
          <li>precip amt: {this.state.current_condition.precipMM} mm</li>
        </ul>
      </div>
    );
  }
}
export default App;
