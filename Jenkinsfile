// Jenkins env var reference https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#working-with-your-jenkinsfile

pipeline {
    agent { label 'ec2-fleet' }
    environment {
        My_Docker_URL = '352708296901.dkr.ecr.us-east-1.amazonaws.com'

    }

    stages {
        stage('Build Simple WebServer') {
            when { anyOf { branch "master"; branch "dev" }}
            steps {
                echo 'Building..'
               sh '''
                My_IMAGE=ji-b-asic-webserver:${BRANCH_NAME}.${BUILD_ID}
                cd basic_webserver
                aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${My_Docker_URL}
                docker build -t ${My_IMAGE} .
                docker tag ${My_IMAGE} ${My_Docker_URL}/${My_IMAGE}
                docker push ${My_Docker_URL}/${My_IMAGE}
                   '''
            }
        }
        /* stage('Test') {
            when { changeRequest() }
            steps {
                echo 'Testing..'

                sh '''
                pip3 install -r basic_webserver/requirements.txt
                python3 -m unittest basic_webserver/tests/test_flask_web.py
                   '''
            }
        } */
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
         when { allOf { branch "Dev" ; changeset "infra/**/*.tf" } }
            steps {
            echo 'Provisioning...'
            sh '''
            cd infra/Dev
            terraform init
            terraform plan
            terraform apply -auto-approve
               '''
                // copyArtifacts filter: 'infra/dev/terraform.tfstate', projectName: '${JOB_NAME}'
               // archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', onlyIfSuccessful: true
            }
        }
        stage('Publish - fantastic_ascii') {
         when {  changeset "package_demo/setup.py" }
            steps {
        sh '''
        cd  package_demo
        pip3 install wheel twine
        python3 setup.py sdist bdist_wheel
        aws codeartifact login --tool twine --repository JiB-Artifactory --domain jib-artifactory --domain-owner 352708296901 --region us-east-1
        python3 -m twine upload dist/* --repository codeartifact

        '''
            }
        }
    }

}