// 这个文件用于创建一个count组件服务的reducer，redecer本质是一个函数
// redecer会接到两个参数，分别为action， preState

import {INCREMENT, DECREMENT} from './constant'

const initState = 0

export default function countReducer(preState = initState, action){
    const {type, data} = action
    console.log(type, data)

    switch (type) {
        // 加
        case INCREMENT:
            return preState + data
        
        // 减
        case DECREMENT:
            return preState - data

        default:
            return preState
    }
}