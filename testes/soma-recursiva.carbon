fn soma_recursiva(x: i32) -> i32 {
    if (x < 2) {
        return x;
    } else {
        return x+soma_recursiva(x-1);
    }
}

fn Main(){
    var a: i32;
    a = soma_recursiva(2);
    Print(a);
}