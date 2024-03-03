import React from 'react';

const IntroPage = () => {
  return (
    <div className="intro-container">
      <h1>Welcome to the Heart Disease Prediction System</h1>
      <div className="infographics">
        {/* Heart Health Statistics */}
        <div className="infographic">
          {/* Display relevant statistics using charts/graphs */}
          <h2>Heart Health Statistics</h2>
          {/* Add your chart/graph components here */}
        </div>

        {/* Risk Factors Wheel */}
        <div className="infographic">
          {/* Create a wheel diagram for risk factors */}
          <h2>Risk Factors Wheel</h2>
          {/* Add your wheel diagram components here */}
        </div>

        {/* Lifestyle Impact */}
        <div className="infographic">
          {/* Use icons to depict lifestyle impact */}
          <h2>Lifestyle Impact</h2>
          {/* Add your lifestyle impact components here */}
        </div>

        {/* Add more infographics as needed */}
      </div>
    </div>
  );
};

export default IntroPage;
