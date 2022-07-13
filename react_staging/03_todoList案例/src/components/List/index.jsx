import React, { Component } from 'react'
import PropsTypes from 'prop-types'
import Item from '../Item'
import './index.css'

export default class List extends Component {

  // 对接收对象 props进行：类型、必要行的限制
  static propsTypes ={
    todoList: PropsTypes.array.isRequired,
    updateTodo: PropsTypes.func.isRequired,
    deleteTodo: PropsTypes.func.isRequired,
  }

  render() {
    const {todoList, updateTodo, deleteTodo} = this.props
    return (
        <ul className="todo-main">
          {
            todoList.map((todo) => {
              return <Item key={todo.id} {...todo} updateTodo={updateTodo} deleteTodo={deleteTodo}/>
            }
            )
          }
        </ul>
    )
  }
}
