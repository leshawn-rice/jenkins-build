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
                  extraVars: [
                      ansible_become_pass: "${sh(cat /tmp/become_pass)}"
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

