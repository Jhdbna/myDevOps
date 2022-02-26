// Jenkins env var reference https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#working-with-your-jenkinsfile

pipeline {
    agent any

    stages {
        stage('Build Simple WebServer') {
            when { anyOf { branch "master"; branch "dev" }}
            steps {
                echo 'Building..'
                sh '''
                cd basic_webserver
                # docker build
                '''
            }
        }
        stage('Test') {
            when { changeRequest() }
            steps {
                echo 'Testing..'

                sh '''
                pip3 install -r basic_webserver/requirements.txt
                python3 -m unittest basic_webserver/tests/test_flask_web.py
                   '''
            }
        }
        stage('Deploy - Dev') {
        when { branch "Dev" }
            steps {
                echo 'Deploying....'
            }
        }
        stage('Deploy - Prod') {
        when { branch "Prod" }
            steps {
                echo 'Deploying....'
            }
        }
        stage('Provision - Dev') {
         when { allOf { branch "Dev"; changeset "infra/**/*.tf" } }
            steps {
            echo 'Provisioning....'
            sh '''
            cd infra/Dev
            terraform init
            terraform plan
            terraform apply
               '''
                // copyArtifacts filter: 'infra/dev/terraform.tfstate', projectName: '${JOB_NAME}'
               // archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', onlyIfSuccessful: true
            }
        }

    }
}