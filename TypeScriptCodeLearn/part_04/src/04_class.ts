// 使用 class 关键字定义一个类
class Person{

    // 实例属性，定义对象实例访问
    // const person = new Person();
    // person.name
    name: string = "小明"

    // 表示只读属性, 无法修改
    readonly familayName: string = "林"

    // 静态属性，通过类访问
    // Person.age
    static age: number = 18

    // 定义方法
    sayHello(){
        console.log("Hello 大家好! ")
    }

    static sayBye(){
        console.log("Bye! ")
    }

}

class Dog{

    name: string;
    
    age: number;

    //构造函数
    constructor(name:string, age: number){
        // 构造函数会在对象创建时候调用
        console.log("构造函数执行了")
        // this 表当前实例,通过 this 添加属性
        this.age = age
        this.name = name
    }

    bark(){
        alert("汪汪汪")
    }
}

class Animal{
    name: string;
    age: number;
    constructor(name:string, age: number){
        this.age = age
        this.name = name
    }
    sayHello(): void{
        console.log("动物在叫")
    }
}


// 继承
class Cat extends Animal{
    run(){
        console.log("在跑~")
    }

    // 重写
    sayHello(): void {
        console.log("喵喵喵")
    }
}

class Duck extends Animal{

    sex: string

    constructor(name:string, age: number, sex: string){
        // 调用父类构造函数
        super(name, age);
        this.sex = sex
    }

    sayHello(): void {
        super.sayHello();
    }
}

