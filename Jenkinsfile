
pipeline {
    agent any
    options { overrideIndexTriggers(false) }
    environment {
        NAME = "Raakhi"
    }

    stages {
        stage('Running Python stage') {
            steps {
                sh "python3 script.py"
            }
        }
        stage('Running Shell stage') {
            steps {
                sh "./script.sh"
            }
        }
        
        
    }
   
}
