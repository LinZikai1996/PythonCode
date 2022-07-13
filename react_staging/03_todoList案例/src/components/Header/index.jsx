import React, { Component } from 'react'
import PropsTypes from 'prop-types'
import {nanoid} from 'nanoid'
import './index.css'

export default class Header extends Component {

  // 对接收对象 props进行：类型、必要行的限制
  static propsTypes ={
    addTodo: PropsTypes.func.isRequired
  }

  // 键盘事件的回调函数
  handleKeyUp = (event) =>{
    // 解构，赋值获取keyCode, target数值
    const {keyCode, target} = event
    // 判断是否有回车按键
    if (keyCode !== 13) return
    if (target.value === ''){
      alert('输入不能为空')
      return
    }
    // 准备对象
    const todoObj = {id:nanoid(), name: target.value, done: false}
    // 将todoObj传递给App
    this.props.addTodo(todoObj)
    // 清空输入
    target.value = ''
  }

  render() {
    return (
      <div className="todo-header">
        <input onKeyUp={this.handleKeyUp} type="text" placeholder="请输入你的任务名称，按回车键确认"/>
      </div>
    )
  }
}
