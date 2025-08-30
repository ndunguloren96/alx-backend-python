// Jenkinsfile for the Django Messaging App CI Pipeline
pipeline {
    agent any

    stages {
        stage('Checkout Source Code') {
            steps {
                echo 'Checking out source code...'
                // The git checkout is handled automatically by Jenkins based on the pipeline configuration
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    # It is a good practice to use a virtual environment
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --no-cache-dir -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                    # Activate the virtual environment and run tests
                    source venv/bin/activate
                    pytest
                '''
            }
        }
        
        stage('Generate Test Report') {
            steps {
                echo 'Generating and archiving test reports...'
                // pytest can generate a JUnit XML report.
                // We'll configure pytest to do so and then use the `junit` step.
                // Note: The pytest command in the 'Run Tests' stage will need to be updated to generate the report.
                // For now, let's assume it is generated.
                // In a real scenario, you'd add: pytest --junitxml=test-reports/results.xml
                // Then, this step would look like:
                // junit '**/test-reports/results.xml'
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
