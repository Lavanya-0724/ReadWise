pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python app.py'
      }
    }
    stage('Test') {
      steps {
        sh 'python -m unittest tests'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker build -t my-app .'
        sh 'docker run -p 8081:8081 my-app'
      }
    }
  }
}
