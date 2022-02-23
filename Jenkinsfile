pipeline {
    agent any

    stages {
        stage('Build') {
        when { anyOf { branch "master" ; branch "dev"}}
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}