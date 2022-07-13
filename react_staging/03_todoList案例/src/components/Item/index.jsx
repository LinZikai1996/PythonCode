import React, { Component } from 'react'
import './index.css'

export default class Item extends Component {

  // 初始化，表示鼠标移入，移出
  state = {
    mouse:false
  }

  // 鼠标移入，移出的回调函数
  handleMouse = (flag) =>{
    return () => {
        this.setState({mouse:flag})
    }
  }

  //勾选回调函数
  handleCheck = (id) =>{
    return (event) => {
      this.props.updateTodo(id, event.target.checked)
    }
  }

  // 删除回调函数
  handleDelete = (id)=>{
    return () =>{
      if (window.confirm('确定删除吗？')){
        this.props.deleteTodo(id)
      }
    }
  }


  render() {
    const {id, name, done} = this.props
    return (
      <li style={{backgroundColor:this.state.mouse? '#ddd': 'white'}} onMouseEnter={this.handleMouse(true)} onMouseLeave={this.handleMouse(false)}>
        <label>
          <input type="checkbox" checked={done} onChange={this.handleCheck(id)}/>
          <span>{name}</span>
        </label>
        <button onClick={this.handleDelete(id)} className="btn btn-danger" style={{display:this.state.mouse? 'block': 'none'}}>删除</button>
      </li>
    )
  }
}
