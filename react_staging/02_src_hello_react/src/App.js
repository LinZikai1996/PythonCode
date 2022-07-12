// 创建外壳组件
import React from "react"

import Hello from "./component/Hello/Hello"
import Welcome from "./component/Welcome/Welcome"

// 暴露并暴露 App 组件
export default class App extends React.Component{
  render(){
    return (
      <div>
        <Hello />
        <Welcome />
      </div>
    )
  }
}
