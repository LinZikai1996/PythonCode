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