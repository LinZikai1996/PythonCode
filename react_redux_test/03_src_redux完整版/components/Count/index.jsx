import React, { Component } from 'react'

// 用于获取 redux中保存的状态
import store from '../../redux/store'
// 引入actionCreator，专门用于action对象
import {createIncrementAction, createDecrementAction} from '../../redux/count_action'

export default class index extends Component {

    componentDidMount(){
        // 检测redux中状态的变化，只要变化就调用render
        store.subscribe(() => {
          this.setState({})
        })
    }

    // 加法
    increment = () => {

        const {value} = this.selectNumber
        // 通知redux 加
        store.dispatch(createIncrementAction(value * 1))
    }

    // 减法
    decrement = () => {

        const {value} = this.selectNumber
        
        store.dispatch(createDecrementAction(value * 1))
    }

    incrementIfOdd = () => {
        const {value} = this.selectNumber
        const count = store.getState()

        if (count % 2 !== 0){
            store.dispatch(createIncrementAction(value * 1))
        }        
    }

    incrementAsYnc = () => {
        const {value} = this.selectNumber

        setTimeout(() => {
            store.dispatch(createIncrementAction(value * 1))
        }, 500)
    }

    render() {
        return (
        <div>
            <h1>当前求和为： {store.getState()} </h1>
            <select ref={c => this.selectNumber = c}>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
            </select>&nbsp;&nbsp;&nbsp;
            <button onClick={this.increment}>+</button>&nbsp;
            <button onClick={this.decrement}>-</button>&nbsp;
            <button onClick={this.incrementIfOdd}>当前和为奇数再加</button>&nbsp;
            <button onClick={this.incrementAsYnc}>异步加</button>
        </div>
        )
    }
}
