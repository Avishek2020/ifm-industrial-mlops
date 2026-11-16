# 🏭 Industrial Predictive Maintenance – MLOps Pipeline

An end-to-end Industrial IoT and MLOps prototype demonstrating predictive maintenance using simulated machine sensor data, machine learning, automated testing, CI/CD pipelines, and Docker.

## 📌 Project Overview

This project simulates an industrial motor monitoring system that analyzes temperature and vibration measurements to identify potential machine anomalies.

A Random Forest machine learning model classifies machine conditions into two categories:

- **Normal:** Machine operating under normal conditions.
- **Maintenance Required:** Abnormal sensor measurements detected.

The project also implements an automated MLOps workflow using GitHub Actions, Pytest, and Docker to demonstrate model training, testing, and deployment preparation.

## 🎯 Objectives

- Simulate industrial IoT sensor data.
- Develop a machine learning model for anomaly classification.
- Implement automated model training.
- Validate model functionality using Pytest.
- Build a CI/CD pipeline using GitHub Actions.
- Package the application using Docker.
- Provide an interactive monitoring dashboard using Streamlit.

## 🏗️ Architecture

```text
Industrial Motor
       |
       v
Temperature & Vibration Data
       |
       v
Data Processing (Python)
       |
       v
Machine Learning
(Random Forest Classifier)
       |
       v
Automated Testing (Pytest)
       |
       v
GitHub Actions CI/CD
       |
       v
Model Artifact (model.joblib)
       |
       v
Docker Image
       |
       v
Streamlit Monitoring Dashboard
```

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| NumPy | Sensor data generation |
| Scikit-learn | Machine learning |
| Joblib | Model serialization |
| Pytest | Automated testing |
| Git & GitHub | Version control |
| GitHub Actions | CI/CD automation |
| Docker | Containerization |
| Streamlit | Interactive dashboard |

## 📂 Project Structure

```text
ifm-industrial-mlops/
│
├── .github/
│   └── workflows/
│       └── mlops.yml
│
├── tests/
│   └── test_model.py
│
├── train.py
├── app.py
├── model.joblib
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ifm-industrial-mlops
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / WSL2:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install streamlit
```

### 4. Train the machine learning model

```bash
python train.py
```

The training process:

1. Generates simulated industrial sensor data.
2. Prepares temperature and vibration features.
3. Trains a Random Forest classifier.
4. Evaluates model accuracy.
5. Saves the trained model as `model.joblib`.

### 5. Run automated tests

```bash
pytest -v
```

The tests validate model training and prediction functionality.

### 6. Launch the monitoring dashboard

```bash
streamlit run app.py
```

Open your browser:

http://localhost:8501

## 📊 Dashboard Features

The Streamlit dashboard provides:

- Interactive temperature input.
- Interactive vibration input.
- AI-based machine condition classification.
- Normal and maintenance-required status indicators.
- Sensor measurement visualization.

## 🧪 Example Test Scenarios

| Temperature | Vibration | Expected Classification |
|---|---|---|
| 60°C | 2.0 mm/s | Normal |
| 90°C | 2.0 mm/s | Maintenance Required |
| 60°C | 5.0 mm/s | Maintenance Required |

These are illustrative test scenarios based on the simulated training rules, not validated industrial operating thresholds.

## ⚙️ CI/CD Pipeline

The GitHub Actions workflow is triggered automatically when code is pushed to the main branch or a pull request targets main.

Pipeline stages:

1. Checkout source code.
2. Configure Python environment.
3. Install dependencies.
4. Execute automated tests.
5. Train the machine learning model.
6. Upload the trained model as a GitHub Actions artifact.
7. Build a Docker image.

Workflow configuration:

`.github/workflows/mlops.yml`

## 🐳 Docker Deployment

Build the Docker image:

```bash
docker build -t ifm-industrial-mlops:latest .
```

Run the container:

```bash
docker run --rm ifm-industrial-mlops:latest
```

Note: The current Dockerfile packages the training application. The Streamlit dashboard can be containerized separately as a future extension.

## 🔮 Future Improvements

- Integrate real industrial sensor data.
- Implement MQTT-based sensor communication.
- Integrate Azure IoT Hub.
- Introduce MLflow for model tracking and versioning.
- Implement model drift monitoring.
- Add REST APIs using FastAPI.
- Deploy the application using Kubernetes.
- Implement automated model deployment and rollback.
- Integrate Prometheus and Grafana for monitoring.

## 💡 Business Value

This prototype demonstrates how DevOps and MLOps practices can support industrial digitalization by:

- Automating machine learning workflows.
- Improving software delivery reliability.
- Standardizing model testing and deployment.
- Supporting scalable industrial AI applications.
- Establishing a foundation for predictive maintenance solutions.

## ⚠️ Disclaimer

This is an educational proof of concept using synthetic sensor data. It is not validated for real industrial machinery or safety-critical maintenance decisions.

## 👨‍💻 Author

Developed as an Industrial IoT and MLOps demonstration project, showcasing Python-based machine learning, DevOps automation, CI/CD, automated testing, and containerization.

**Focus Areas:** Industrial AI | DevOps | MLOps | Predictive Maintenance | CI/CD | Docker
