pipeline {
    agent any
    environment {
        NAME = "Raakhi"
    }
    
    stages {
        stage('Running Python stage') {
            steps {
                echo "python3 script.py"
            }
        }
        stage('Running Shell scripting') {
            steps {
                echo "./script.sh"
            }
        }
    }
}