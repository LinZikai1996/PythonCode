// 该文件为count组生成action对象

import {INCREMENT, DECREMENT} from './constant'

// 同步action，就是指action值为对象
export const createIncrementAction = data => ({type: INCREMENT, data})

export const createDecrementAction = data => ({type: DECREMENT, data})

// 异步action，就是指action值为函数, 一般都会调用同步 action
export const createIncrementAsyncAction = (data, time) => {
    return (dispatch) => {
        setTimeout(() =>{
            dispatch(createIncrementAction(data))
        }, time)
      }
}
