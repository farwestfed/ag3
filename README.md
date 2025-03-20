# ASA(IE&E) Weather Event Dashboard

## Overview
This dashboard provides decision support for infrastructure investment decisions at US Army bases, based on historical weather damage data. It visualizes weather-related damages and costs to help prioritize infrastructure investments and mitigation strategies.

## Features
- Interactive dashboard showing weather damage costs across Army installations
- Comprehensive data analysis through multiple views:
  - Damage Forecast
  - Event Analysis
  - Geographic Analysis
  - Budget Planning & Mitigation Strategy

### Key Visualizations
- Cost distribution by weather event type (pie chart)
- Top weather events by cost impact (horizontal bar chart)
- Geographic distribution of damages (map visualization)
- Scenario modeling for mitigation strategies
- Cost-benefit analysis for infrastructure improvements

### Budget Planning Features
- Interactive mitigation scenario modeling
- Real-time cost-benefit analysis
- ROI calculations for different mitigation strategies
- Implementation cost tracking
- Projected damage reduction estimates

## Data
The dashboard uses historical weather damage data stored in CSV format (`ag3_data_v7.csv`), which includes:
- Weather event details
- Damage costs
- Installation locations
- Event dates and types

## Getting Started

### Prerequisites
- Node.js (v14 or later)
- npm

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/farwestfed/ag3.git
   cd ag3
   ```
2. Install dependencies:
   ```
   npm install
   ```

### Running the Application
To start the development server:
```
npm start
```

The application will be available at [http://localhost:3001](http://localhost:3001).

### Building for Production
To build the application for production:
```
npm run build
```

## Technologies Used
- React.js - Frontend framework
- Recharts - Data visualization library
- PapaParse - CSV parsing
- Tailwind CSS - Styling

## Project Purpose
This application helps decision-makers:

1. Identify high-risk installations based on historical weather damage
2. Evaluate cost-effective mitigation strategies
3. Plan infrastructure investments based on:
   - Historical damage patterns
   - Cost-benefit analysis
   - ROI calculations
4. Make data-driven decisions for weather resilience improvements

## Contributing
To contribute to this project:
1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License
This project is proprietary and confidential.
Copyright © 2024 ASA(IE&E). All rights reserved.
