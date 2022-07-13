// 创建外壳组件
import React from "react"

import Header from "./components/Header"
import List from './components/List'
import Footer from './components/Footer'
import './App.css'

/*
一、todoList案例相关知识点
		1.拆分组件、实现静态组件，注意：className、style的写法
		2.动态初始化列表，如何确定将数据放在哪个组件的state中？
					——某个组件使用：放在其自身的state中
					——某些组件使用：放在他们共同的父组件state中（官方称此操作为：状态提升）
		3.关于父子之间通信：
				1.【父组件】给【子组件】传递数据：通过props传递
				2.【子组件】给【父组件】传递数据：通过props传递，要求父提前给子传递一个函数
		4.注意defaultChecked 和 checked的区别，类似的还有：defaultValue 和 value
		5.状态在哪里，操作状态的方法就在哪里
*/

// 暴露并暴露 App 组件
export default class App extends React.Component{

  // 初始化状态
  // 状态在哪里，操作状态的方法就在那里
  state = { todoList:[
    {
      id:'001', name:'吃饭', done: true
    },
    {
      id:'002', name:'睡觉', done: false
    },
    {
      id:'003', name:'学习', done: false
    },
    {
      id:'004', name:'玩耍', done: true
    },]
  }

  // addTodo用于添加一个todo对象，接受的参数是todo对象
  addTodo = (todoObj) =>{
    // 获取todo
    const {todoList} = this.state
    // 追加
    const newTodoList = [todoObj, ...todoList]
    // 更新状态
    this.setState({todoList:newTodoList})
  }

  // updateTodo用于更新一个todo对象
  updateTodo = (id, done) =>{
    // 获取todo
    const {todoList} = this.state
    //匹配处理数据
    const newTodoList = todoList.map((todo) => {
      if (id === todo.id) return {...todo, done:done}
      else return todo
    })
    // 更新状态
    this.setState({todoList:newTodoList})
  }
  
  // deleteTodo用于删除一个todo对象
  deleteTodo = (id) =>{
    // 获取todo
    const {todoList} = this.state
    // 过滤数据
    const newTodoList = todoList.filter((todo) => {
      return todo.id !== id
    })
    // 更新状态
    this.setState({todoList:newTodoList})
  }

  // checkAllTodo用于全选
  checkAllTodo = (done) =>{
    // 获取todo
    const {todoList} = this.state

    const newTodoList = todoList.map((todo) => {
      return {...todo, done:done}
    })
    // 更新状态
    this.setState({todoList:newTodoList})
  }

  //clearAllDone用于清除所有已完成的todo
  clearAllDone = () =>{
    // 获取todo
    const {todoList} = this.state
    // 过滤数据
    const newTodoList = todoList.filter((todo) => {
      return !todo.done
    })
    // 更新状态
    this.setState({todoList:newTodoList})
  }


  render(){
    return (
      <div className="todo-container">
        <div className="todo-wrap">
          <Header addTodo={this.addTodo}/>
          <List todoList={this.state.todoList} updateTodo={this.updateTodo} deleteTodo={this.deleteTodo}/>
          <Footer todoList={this.state.todoList} checkAllTodo={this.checkAllTodo} clearAllDone={this.clearAllDone}/>
        </div>
      </div>
    )
  }
}
