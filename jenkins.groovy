
pipeline {
    
    agent any;
    
    stages{
    
        stage('preparacao'){

            steps {
                echo "Preparando a máquina ..."
                sleep 10
            }    
        }
    
        stage('build'){
    
            steps {
                echo "Buildando a aplicação ..."
                sleep 10
            }    
        }
    
        stage('result'){

            steps {
                echo "Aplicação deployada com sucesso !"
                sleep 10
            }    
        }
    }
}