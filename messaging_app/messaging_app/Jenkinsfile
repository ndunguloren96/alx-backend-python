// Jenkinsfile for the Django Messaging App CI Pipeline
pipeline {
    // This tells Jenkins to run the pipeline inside a Docker container
    // using the official Python 3.10 image.
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                // Since the agent is already a Python container, we can directly use pip.
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                // Run pytest directly inside the Python container.
                sh 'pytest'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Pipeline succeeded! 🎉'
        }
        failure {
            echo 'Pipeline failed! 😢'
        }
    }
}
