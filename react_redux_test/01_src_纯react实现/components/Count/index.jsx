import React, { Component } from 'react'

export default class index extends Component {

    state = {
        count: 0
    }


    // 加法
    increment = () => {

        const {value} = this.selectNumber
        const {count} = this.state

        this.setState({count: count + value * 1})
    }

    // 减法
    decrement = () => {

        const {value} = this.selectNumber
        const {count} = this.state
  
        this.setState({count: count - value * 1})
    }

    incrementIfOdd = () => {
        const {value} = this.selectNumber
        const {count} = this.state

        if (count % 2 !== 0){
            this.setState({count: count + value * 1})
        }        
    }

    incrementAsYnc = () => {
        const {value} = this.selectNumber
        const {count} = this.state

        setTimeout(() => {
            this.setState({count: count + value * 1})
        }, 500)
    }

    render() {
        return (
        <div>
            <h1>当前求和为： {this.state.count} </h1>
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
