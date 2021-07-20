
pipeline {
    agent any
    options { overrideIndexTriggers(false) }
    environment {
        NAME = "Raakhi"
    }

    stages {
        stage('Running Python stage') {
            steps {
                echo "Hello World"
                sh "python3 script.py"
            }
        }
        
        
    }
   
}
