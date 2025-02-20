pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/goshipra/Algoritms.git'
            }
        }

        stage('Run Script') {
            steps {
                script {
                    sh 'python3 commaoncodingquestions/Revision/mathematicsandnumbers.py'  // Change to your script filename
                }
            }
        }
    }
}
