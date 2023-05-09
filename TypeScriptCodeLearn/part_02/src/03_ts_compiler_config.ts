// tsc xxx.ts -w 监视改动，自动编译xxx.ts

// tsc + tsconfig.json 全局自动监视

console.log("Hello TS")

// noImplicitAny : 用于控制编译器是否允许未明确声明类型的参数和变量使用 "any" 类型
function test_1(a:number, b: number){
    return a + b;
}

// noImplicitThis : 用于控制编译器是否允许在类成员函数中使用未明确声明 "this" 的情况
function test_2(this: Window){
    alert(this);
}

// strictNullChecks : 用于控制编译器是否允许使用 null 和 undefined 类型，以及如何检查它们的使用
// 加上 ？
let box1 = document.getElementById('box1')
box1?.addEventListener('click', function(){
    alert('Hello')
})