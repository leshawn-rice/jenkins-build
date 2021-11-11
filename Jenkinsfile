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
              sh 'ansible-playbook /home/ld-admin/ansible/test/playbook.yml -i inventory.ini -e "ansible_become_pass=$(cat /tmp/become_pass)"'
              ansiblePlaybook(
                  playbook: '/home/ld-admin/ansible/test/playbook.yml', 
                  inventory: 'inventory.ini',
                  extras: '-e "ansible_become_pass=$(cat /home/ld-admin/.ssh/become_pass)"'
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

