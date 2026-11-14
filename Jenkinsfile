pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Train model') {
            steps {
                bat 'python train.py'
            }
        }
        stage('Run tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }
        stage('Data monitoring') {
            steps {
                bat 'python scripts/monitor.py'
            }
        }
    }
}
