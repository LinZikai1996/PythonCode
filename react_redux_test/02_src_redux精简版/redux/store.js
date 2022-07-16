// 该文件专门用于暴露一个store对象，整个应用只有一个store对象

// 引入createStore， 专门用于创建redux核心对象store对象
import { legacy_createStore as createStore} from 'redux'
// 引入count组件
import countReducer from './count_reducer'
// 暴露 store
export default createStore(countReducer)
