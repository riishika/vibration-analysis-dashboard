from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import datetime

app = Flask(__name__)
CORS(app)

class VibrationAnalyzer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=2)
     
    def analyze(self, data):
        scaled_data = self.scaler.fit_transform(data)
        pca_result = self.pca.fit_transform(scaled_data)
        return pca_result

analyzer = VibrationAnalyzer()

@app.route('/api/vibration-data')
def get_vibration_data():
    raw_data = np.random.rand(10, 5)  # 10 time points, 5 sensors
    analyzed_data = analyzer.analyze(raw_data)
    amplitude = analyzed_data[0, 0]
    frequency = analyzed_data[0, 1]
 
    return jsonify({
        'timestamp': datetime.datetime.now().isoformat(),
        'amplitude': float(amplitude),
        'frequency': float(frequency)
    })

if __name__ == '__main__':
    app.run(debug=True)