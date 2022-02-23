pipeline {
    agent any

    stages {
        stage('Build') {
//         when { anyOf { branch "master" ; branch "dev"}}
            steps {
                echo 'Building..'
                aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 352708296901.dkr.ecr.us-east-1.amazonaws.com
                docker build ./basic_webserver
                docker tag ji-b-asic-webserver:latest 352708296901.dkr.ecr.us-east-1.amazonaws.com/ji-b-asic-webserver:latest
                docker push 352708296901.dkr.ecr.us-east-1.amazonaws.com/ji-b-asic-webserver:latest
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy - Dev') {
            steps {
                echo 'Dev Deploying....'
            }
        }
        stage('Deploy - Prod') {
            steps {
                echo 'Prod Deploying....'
            }
        }
    }
}