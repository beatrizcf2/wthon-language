--portugues;
funcao OlaMundo(int n){
    int x;
    x = 0;
    enquanto (x < n){
        imprime("Ola Mundo: ");
        imprime(x);
        x = x + 1;
    }
}

--deutsch;
funktion HalloWelt(int n){
    int x;
    x = 0;
    solange (nicht(x < n)){
        drucke("Hallo Welt: ");
        drucke(x);
        x = x + 1;
    }
}

--english;
function HelloWorld(int n){
    int x;
    x = 0;
    while (x < n){
        print("Hello World: ");
        print(x);
        x = x + 1;
    }
}

function Main(){
    HelloWorld(1);
    OlaMundo(1);
    HalloWelt(1);
}