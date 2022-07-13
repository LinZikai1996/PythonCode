import React, { Component } from 'react'
import './index.css'

export default class Footer extends Component {

  // 全选的回调函数
  handleChangeAll = (event) => {
    this.props.checkAllTodo(event.target.checked)
  }

  handleClearAllDone = () =>{
    this.props.clearAllDone()
  }

  render() {

    const {todoList} = this.props

    // 完成的总数
    const doneCount = todoList.reduce((pre, todo) =>{
      return pre + (todo.done? 1: 0)
    }, 0)

    // 总数
    const total = todoList.length

    return (
      <div className="todo-footer">
        <label>
          <input type="checkbox" onChange={this.handleChangeAll} checked={doneCount === total && total !== 0? true : false}/>
        </label>
        <span>
          <span>已完成 {doneCount}</span> / 全部 {total}
        </span>
        <button onClick={this.handleClearAllDone} className="btn btn-danger">清除已完成任务</button>
      </div>
    )
  }
}
