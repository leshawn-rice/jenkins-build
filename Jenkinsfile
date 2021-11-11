properties([pipelineTriggers([githubPush()])])

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
              echo 'Building...'
              sh '/home/ld-admin/build.sh 4.2.0 -rc5'
            }
        }
        stage('Upgrade') {
            steps {
              echo 'Upgrading...'
              ansiblePlaybook(
                  playbook: '/home/ld-admin/ansible/test/playbook.yml', 
                  inventory: 'inventory.ini',
                  extras: '-vvv',
                  extraVars: [
                      ansible_become_pass: "Uplevel2016-ServerPass"
                  ]
              )
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
    }
}

