properties([pipelineTriggers([githubPush()])])

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
              echo 'Building...'
              sh -c '/home/jenkins/build.sh'
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

