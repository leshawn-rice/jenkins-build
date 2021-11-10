properties([pipelineTriggers([githubPush()])])

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
              echo 'Building...'
              sh '''#!/bin/bash
                    cd /home/ld-admin
                    ./build.sh 4.2.0 -rc5
              '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
    }
}

