// 引入count UI组件
import CountUI from '../../components/Count'
// 引入connect用于连接UI与redux
import {connect} from 'react-redux'
import {
    createIncrementAction, 
    createDecrementAction, 
    createIncrementAsyncAction} from '../../redux/count_action'

// mapStateToProps函数返回对象,
// 其中的key作为传递给 组件props的key, value就作为传递给组件props的value --用于传递状态
function mapStateToProps(state){
    return {count: state}
}

// mapDispatchTopProps函数返回对象,
// 其中的key作为传递给 组件props的key, value就作为传递给组件props的value --用于传递操作状态的方法
function mapDispatchTopProps(dispatch){
    return {
        jia : (number) => {
            // 通知 redux 执行加法
            dispatch(createIncrementAction(number))
        },
        jian : (number) => {
            // 通知 redux 执行减法
            dispatch(createDecrementAction(number))
        },
        jiaAsync: (number, time) => {
            // 通知 redux 执行异步加法
            dispatch(createIncrementAsyncAction(number, time))
        }
    }
}

// 使用connect()()创建并且暴露一个Count的容器组件
export default connect(mapStateToProps, mapDispatchTopProps)(CountUI)

