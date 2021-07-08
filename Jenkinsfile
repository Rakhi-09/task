
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
        post {
        success {
            echo 'Run 2nd pipeline!'
            build job: '2nd pipeline', parameters: [string(name: 'MY_STR_PARAM', value: 'value from 1st pipeline')]
        }
    }
    }
}
