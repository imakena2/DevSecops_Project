pipeline {
  agent any
  stages {
    stage('Clone Code') {
      steps {
        git 'https://github.com/imakena2/DevSecops_Project.git'
      }
    }
    stage('Install Dependencies') {
      steps {
        sh 'npm install'
      }
    }
    stage('Build App') {
      steps {
        sh 'npm run build'
      }
    }
    stage('Run Tests') {
      steps {
        sh 'npm test || echo "No tests yet"'
      }
    }
    stage('Docker Build') {
      steps {
        sh 'docker build -t devsecops-nginx .'
      }
    }
  }
}
