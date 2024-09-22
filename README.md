# Vibration Analysis Dashboard

This project implements a real-time vibration analysis dashboard using React for the frontend and Flask for the backend. It's designed to process and visualize vibration data for mechanical engineering applications.

## Project Structure

```
vibration-analysis-project/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── VibrationDashboard.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json
│   └── tailwind.config.js
└── backend/
    ├── app.py
    └── requirements.txt
```

## Setup and Installation

### Frontend

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

The frontend will be available at `http://localhost:3000`.

### Backend

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Start the Flask server:
   ```
   python app.py
   ```

The backend API will be available at `http://localhost:5000`.

## Usage

Once both the frontend and backend are running, open your web browser and go to `http://localhost:3000`. You should see the vibration analysis dashboard with real-time updates of amplitude and frequency data.

## Features

- Real-time data visualization
- Amplitude and frequency charts
- Simulated data generation (replace with actual sensor data in production)
- Basic machine learning analysis using PCA

## Technologies Used

- Frontend: React, Recharts, Tailwind CSS
- Backend: Flask, NumPy, scikit-learn

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
