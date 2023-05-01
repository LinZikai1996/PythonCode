// 声明一个变量a, 同时指定类型为number
// a 的类型设置为number, 在以后的使用a只能是数字
let a : number
a = 10;
// a = 'hello' 报错，类型不对


let b: string;
b = 'hello'


// 声明完变量，就赋值
// 变量声明和赋值时同事进行的，TS自动检测类型
let c = false


// 函数的类型声明
function sum(a: number, b: number): number{
    return a + b
}


// 直接使用字面量进行类型申明
let d: 10;
d = 10;
// d = 11; 报错


// let f: boolean | string 可以这样
// 可是使用 | 连接多个类型
let f : "male" | "female"
f = "male"
f = "female"
// 但是，f = "hello" 报错


// any 表示任意类型，一个变量设置为any，表示对于该变量关闭了TS类型检测
// 声明变量不指定类型，TS自动判定为any(隐式any)
// 不建议使用
// b = e 连带影响 b 成为 any
let e : any
e = 10;
e = "hello";
e = true


// unknown 表示未知类型
// b = g 报错，unknown 类型的变量，不能直接赋值给其他变量
// if (typeof g === "string"){
//     b = g
// } 就不会报错了
let g: unknown;
g = "hello"


// 类型断言，可以用来告诉解析器变成实际类型, 两种用法
b = g as string;
b = <string> g;


// function test_function(num: any): true | 123 返回值类型自动改了
function test_function(num: number){
    if (num > 100){
        return true
    } else {
        return 123
    }
}


// void 表示没有返回值，never 表示永远不会有返回结果
function test_void(): void{

}

function test_never(): never{
    throw new Error("error");
    
}


// object 表示一个js 对象
let h: object;
h = {};
h = function (){}

// {}用来指定对象中可以包含哪些属性，语法：{属性名： 属性值, 属性名?： 属性值}，其中问号，表示属性可选
let i: {name: string, age?: number};
i = {name: "zikai"}

// [propName: string]: any 表示任意类型的属性
let j: {name: string, [propName: string]: any};
j = {
    name: "zikai",
    age: 18,
    sex: "man"
}

// 设置函数结构的类型声明
// 语法： (形参： 类型，形参： 类型 ...) => 返回值
let k: (k1: number, k2: number) => number;

k = function(n1, n2): number{
    return n1 + n2
}


// l, m字符串数组, 两种方式
let l: string[];
l = ['a', 'b'];
let m: Array<string>