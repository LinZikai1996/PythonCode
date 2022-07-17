// 引入connect用于连接UI与redux
import {connect} from 'react-redux'
import {
    createIncrementAction, 
    createDecrementAction, 
    createIncrementAsyncAction} from '../../redux/count_action'

import React, { Component } from 'react'

// 定义UI组件
class Count extends Component {

    // 加法
    increment = () => {

        const {value} = this.selectNumber
        this.props.jia(value * 1)
    }

    // 减法
    decrement = () => {

        const {value} = this.selectNumber
        this.props.jian(value * 1)

    }

    incrementIfOdd = () => {
        const {value} = this.selectNumber
        if(this.props.count % 2 !== 0){
            this.props.jia(value * 1)
        }
    
    }

    incrementAsync = () => {
        const {value} = this.selectNumber
        this.props.jiaAsync(value * 1, 500)
    }

    render() {
        return (
        <div>
            <h1>当前求和为： {this.props.count} </h1>
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
            <button onClick={this.incrementAsync}>异步加</button>
        </div>
        )
    }
}
    

// 使用connect()()创建并且暴露一个Count的容器组件
export default connect(
    state =>({count: state}),

    // mapDispatchTopProps函数返回对象
    // dispatch => (
    //     {
    //         jia : (number) => dispatch(createIncrementAction(number)),
    //         jian : (number) => dispatch(createDecrementAction(number)),
    //         jiaAsync : (number, time) => dispatch(createIncrementAsyncAction(number, time))
    //     }
    // )
    
    // mapDispatchTopProps简写
    {
        jia: createIncrementAction,
        jian: createDecrementAction,
        jiaAsync: createIncrementAsyncAction
    }
)(Count)

