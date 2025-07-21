pipeline {
  agent any

  environment {
    SONARQUBE_SERVER = 'SonarQubeLocal' // Must match the SonarQube server name in Jenkins
  }

  stages {
    stage('Clone Code') {
      steps {
        git branch: 'main', url: 'https://github.com/imakena2/DevSecops_Project.git'
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

    stage('Static Code Analysis - SonarQube') {
      steps {
        withSonarQubeEnv("${SONARQUBE_SERVER}") {
          tool name: 'SonarScannerLocal', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
          sh 'sonar-scanner'
        }
      }
    }
  }
}
