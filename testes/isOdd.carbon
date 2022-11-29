--portugues;

funcao éPositivo(int n){
    se (n > 0) {
        imprime("Número Positivo");
    }
    senao {
        se (n == 0){
            imprime("Zero");
        } senao {
            imprime("Número Negativo");
        }
    }
}


funcao Principal(){
    int n;
    n = leia();
    éPositivo(n);
}