

function test1(a: number): number{
    return a;
}

// 泛型
function test2<T>(a: T): T{
    return a;
}

test2(10)
test2<string>("Hello")

// 多个
function test3<T, K>(a:T, b:K): T{
    console.log(b)
    return a;
}

test3<number, string>(123, "Hello")

interface C{
    length: number;
}

// 继承
function test4<T extends C>(a: T): number{
    return a.length
}

class myClass1<T>{
    name: T;

    constructor(name:T){
        this.name = name
    }
}