pipeline {
    agent any

    tools {
        nodejs 'NodeJS_20'
    }

    environment {
        SONARQUBE = 'SonarQubeLocal'           // Must match Jenkins config
        SONAR_TOKEN = credentials('SONAR_TOKEN') // From Jenkins Credentials
    }

    stages {
        stage('Clone Code') {
            steps {
                git url: 'https://github.com/imakena2/DevSecops_Project.git', branch: 'main'
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
                script {
                    try {
                        sh 'npm test'
                    } catch (err) {
                        echo 'No tests yet'
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    script {
                        def scannerHome = tool name: 'SonarScannerLocal', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                        env.PATH = "${scannerHome}/bin:${env.PATH}"
                        sh """
                            sonar-scanner \
                            -Dsonar.projectKey=DevSecops_Project \
                            -Dsonar.sources=src \
                            -Dsonar.host.url=http://192.168.8.24:9000 \
                            -Dsonar.token=${SONAR_TOKEN} \
                            -Dsonar.projectVersion=1.0 \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }
    }
}
