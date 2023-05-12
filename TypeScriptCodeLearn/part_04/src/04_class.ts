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

// 抽象类，可以添加抽象方法，不能 new
abstract class Animal{
    name: string;
    age: number;
    constructor(name:string, age: number){
        this.age = age
        this.name = name
    }

    // 抽象方法
    abstract sayHello(): void;
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
        console.log("嘎嘎嘎")
    }
}

// 接口，接口中所有方法都是抽象方法
type myType = {
    name: string;
    age: number;
}

interface myInterface{
    name: string;
}

interface myInterface{
    age: number;

    sayHello():void
}

// 接口实现
class myClass implements myInterface{
    
    name: string
    age: number

    constructor(name:string, age: number){
        this.age = age
        this.name = name
    }

    sayHello(): void {
        throw new Error("Method not implemented.")
    }
    
}


// 属性封装
class A{
    // 默认public，子类也可以访问
    private _name: string;
    private _age: number;
    
    constructor(name:string, age: number){
        this._age = age
        this._name = name
    }

    getAge(){
        return this._age
    }

    setAge(value: number){
        if (value >= 0 ){
            this._age = value
        } else{
            this._age = 0
        }   
    }

    get name(){
        return this._name
    }

    set name(value: string){
        this._name = value
    }
}

//语法糖
class B{
    constructor(public name:string, public age:number){

    }
}