pipeline {
    agent any
      environment {
        My_Docker_URL = '352708296901.dkr.ecr.us-east-1.amazonaws.com'

    }

    stages {
        stage('Build') {
//         when { anyOf { branch "master" ; branch "dev"}}

            steps {
                echo 'Building..'
                sh ''''
                My_IMAGE=ji-b-asic-webserver:${BRANCH_NAME}.${BUILD_ID}s
                cd basic_webserver
                aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${My_Docker_URL}
                docker build ./basic_webserver
                docker tag ${My_IMAGE} ${My_Docker_URL}/${My_IMAGE}
                docker push ${My_Docker_URL}/${My_IMAGE}
                  ''''
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