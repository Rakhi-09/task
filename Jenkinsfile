
pipeline {
    agent any
    environment {
        NAME = "Raakhi"
    }
    
    stages {
        stage('Running Python stage') {
            steps {
                sh "python3 script.py"
            }
        }
        stage('Running Shell scripting') {
            steps {
                sh "./script.sh"
            }
        }
    }
}
