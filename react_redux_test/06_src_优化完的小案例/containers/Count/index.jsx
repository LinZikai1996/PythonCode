// 引入connect用于连接UI与redux
import {connect} from 'react-redux'
import {createIncrementAction} from '../../redux/count_action'

import React, { Component } from 'react'

// 定义UI组件
class Count extends Component {

    // 加1
    addOne = () => {
        this.props.addOne(1)
    }

    render() {
        return (
        <div>
            <h1>当前求和为： {this.props.count} </h1>
            <button onClick={this.addOne}>+</button>&nbsp;&nbsp;&nbsp;
        </div>
        )
    }
}
    

// 使用connect()()创建并且暴露一个Count的容器组件
export default connect(
    state =>({count: state}),
    {
        addOne: createIncrementAction,
    }
)(Count)

