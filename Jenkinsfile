pipeline {
  agent any

  environment {
    SONAR_TOKEN = 'squ_639d70dfa9637c77f5fbdcc4dfcd3acf5c60d858'
    SONAR_HOST_URL = 'http://192.168.8.24:9000'
  }

  tools {
    nodejs 'NodeJS16' // This is valid
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

    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('SonarQubeLocal') {
          script {
            def scannerHome = tool name: 'SonarScannerLocal', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
            env.PATH = "${scannerHome}/bin:${env.PATH}"
            sh """
              sonar-scanner \
                -Dsonar.projectKey=DevSecops_Project \
                -Dsonar.sources=src \
                -Dsonar.host.url=${SONAR_HOST_URL} \
                -Dsonar.token=${SONAR_TOKEN} \
                -Dsonar.projectVersion=1.0 \
                -Dsonar.sourceEncoding=UTF-8 \
                -Dsonar.language=js
            """
          }
        }
      }
    }
  }
}
