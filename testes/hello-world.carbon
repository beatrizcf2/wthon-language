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
funktion HalloWelt(int printe){
    int x;
    x = 0;
    
    solange ((x < printe)){
        drucken("Hallo Welt: ");
        drucken(x);
        x = x + 1;
    }
}

--english;
function HelloWorld(int n){
    int x;
    x = 0;
    while (not(x < n)){
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