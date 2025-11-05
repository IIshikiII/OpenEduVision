# OpenEduVision

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![React 18+](https://img.shields.io/badge/react-18+-61dafb.svg)](https://reactjs.org/)

Web application for analyzing the effectiveness of educational courses using AI. OpenEduVision leverages machine learning and modern web technologies to provide insights into course quality, engagement metrics, and student performance patterns.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Installation](#installation)
  - [Backend Setup](#backend-setup)
  - [ML Module Setup](#ml-module-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

OpenEduVision is an open-source platform designed to help educators and course creators analyze the effectiveness of their educational content. Using AI-powered analysis, the system can:

- **Analyze Course Content**: Extract key metrics from educational materials
- **Track Student Engagement**: Monitor student interaction patterns and progress
- **Generate Insights**: Provide actionable recommendations for course improvement
- **Predict Performance**: Use ML models to forecast student outcomes
- **Visualize Data**: Interactive dashboards for easy understanding of complex metrics

## Architecture

OpenEduVision follows a modern three-tier architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (React)                         │
│         Interactive Dashboard & User Interface              │
│  - Course Analysis Dashboards                               │
│  - Real-time Metrics Visualization                          │
│  - Student Performance Charts                               │
└────────────────────────┬────────────────────────────────────┘
                         │ REST API
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                Backend (FastAPI)                            │
│              REST API & Business Logic                      │
│  - Authentication & Authorization                           │
│  - Data Processing & Aggregation                            │
│  - Course Management                                        │
│  - Student Analytics                                        │
└────────────────────────┬────────────────────────────────────┘
                         │ Calls
                         ▼
┌─────────────────────────────────────────────────────────────┐
│            ML Module (Jupyter + HuggingFace)               │
│              Machine Learning Pipeline                      │
│  - NLP Models for Content Analysis                          │
│  - Predictive Analytics Models                              │
│  - Performance Classification                               │
│  - Recommendation Engine                                    │
└─────────────────────────────────────────────────────────────┘
```

## Installation

### Prerequisites

- Python 3.9+
- Node.js 16+
- pip
- npm or yarn
- Git

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/IIshikiII/OpenEduVision.git
   cd OpenEduVision/backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the backend server:**
   ```bash
   python main.py
   # Server will start at http://localhost:8000
   # API docs available at http://localhost:8000/docs
   ```

### ML Module Setup

1. **Navigate to ML directory:**
   ```bash
   cd OpenEduVision/ml
   ```

2. **Create virtual environment (optional, separate from backend):**
   ```bash
   python -m venv ml_env
   source ml_env/bin/activate
   ```

3. **Install ML dependencies:**
   ```bash
   pip install -r requirements.txt
   # Installs: torch, transformers, scikit-learn, jupyter, pandas, numpy
   ```

4. **Run Jupyter Notebook:**
   ```bash
   jupyter notebook notebook.ipynb
   ```

5. **Use ML Models in Backend:**
   The backend imports models from `model.py` for predictions:
   ```python
   from ml.model import CourseAnalyzer, PerformancePredictor
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd OpenEduVision/frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Create environment configuration:**
   ```bash
   cp .env.example .env.local
   # Edit .env.local with API endpoint: REACT_APP_API_URL=http://localhost:8000
   ```

4. **Start development server:**
   ```bash
   npm start
   # Application will open at http://localhost:3000
   ```

5. **Build for production:**
   ```bash
   npm run build
   # Build output in build/ directory
   ```

## Usage

### Quick Start

1. **Start all services:**
   ```bash
   # Terminal 1: Backend
   cd backend && python main.py

   # Terminal 2: Frontend
   cd frontend && npm start

   # Terminal 3: ML Module (if running experiments)
   cd ml && jupyter notebook
   ```

2. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api
   - API Documentation: http://localhost:8000/docs

### API Endpoints

#### Course Management
- `POST /api/courses` - Create new course
- `GET /api/courses/{course_id}` - Get course details
- `PUT /api/courses/{course_id}` - Update course
- `DELETE /api/courses/{course_id}` - Delete course

#### Analytics
- `GET /api/courses/{course_id}/analytics` - Get course analytics
- `POST /api/courses/{course_id}/analyze` - Run analysis
- `GET /api/courses/{course_id}/predictions` - Get performance predictions

#### Students
- `POST /api/courses/{course_id}/students` - Enroll student
- `GET /api/courses/{course_id}/students` - List enrolled students
- `GET /api/students/{student_id}/progress` - Get student progress

## Project Structure

```
OpenEduVision/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example            # Environment variables template
│   ├── app/
│   │   ├── api/
│   │   │   ├── courses.py      # Course endpoints
│   │   │   ├── analytics.py    # Analytics endpoints
│   │   │   └── students.py     # Student endpoints
│   │   ├── models/
│   │   │   ├── course.py       # Course data model
│   │   │   ├── student.py      # Student data model
│   │   │   └── analytics.py    # Analytics data model
│   │   ├── services/
│   │   │   ├── course_service.py
│   │   │   ├── ml_service.py
│   │   │   └── analytics_service.py
│   │   └── db/
│   │       └── database.py     # Database configuration
│   └── README.md
│
├── ml/
│   ├── notebook.ipynb          # Jupyter notebook for ML experiments
│   ├── model.py                # ML model definitions and functions
│   ├── requirements.txt         # ML dependencies
│   ├── data/
│   │   ├── sample_courses.csv  # Sample course data
│   │   └── training_data.csv   # Training dataset
│   ├── models/
│   │   ├── course_analyzer.pkl # Serialized models
│   │   └── predictor.pkl
│   └── README.md
│
├── frontend/
│   ├── package.json            # Node dependencies
│   ├── .env.example            # Environment variables template
│   ├── public/
│   │   └── index.html          # HTML template
│   ├── src/
│   │   ├── index.js            # React entry point
│   │   ├── App.js              # Main App component
│   │   ├── components/
│   │   │   ├── Dashboard.js    # Main dashboard component
│   │   │   ├── CourseCard.js   # Course display component
│   │   │   ├── AnalyticsChart.js
│   │   │   ├── Header.js       # Application header
│   │   │   └── Navigation.js   # Navigation component
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── CourseDetails.js
│   │   │   └── Analytics.js
│   │   ├── services/
│   │   │   └── api.js          # API client
│   │   ├── styles/
│   │   │   └── App.css
│   │   └── utils/
│   │       └── constants.js
│   └── README.md
│
├── docs/
│   ├── API.md                  # API documentation
│   ├── ARCHITECTURE.md         # Architecture details
│   └── DEPLOYMENT.md           # Deployment guide
│
├── .gitignore
├── LICENSE
└── README.md                   # This file
```

## Technologies

### Backend
- **Framework**: FastAPI - Modern Python web framework
- **Database**: PostgreSQL / SQLite
- **Authentication**: JWT tokens
- **Async**: AsyncIO

### ML & Data Science
- **Frameworks**: PyTorch, TensorFlow
- **NLP**: Hugging Face Transformers
- **Data Processing**: Pandas, NumPy, Scikit-learn
- **Notebooks**: Jupyter

### Frontend
- **Framework**: React 18+
- **State Management**: Redux or Context API
- **UI Components**: Material-UI or Tailwind CSS
- **Charts**: Chart.js or Recharts
- **HTTP Client**: Axios

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

### Development Guidelines

- Write clean, well-documented code
- Follow PEP 8 for Python code
- Write unit tests for new features
- Update documentation accordingly
- Run tests before submitting PR: `pytest`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/IIshikiII/OpenEduVision/issues)
- Start a [Discussion](https://github.com/IIshikiII/OpenEduVision/discussions)
- Contact: [email protected]

## Acknowledgments

- Hugging Face for pre-trained NLP models
- FastAPI community for excellent documentation
- React community for amazing tools and libraries

---

**Happy analyzing! 📊✨**
