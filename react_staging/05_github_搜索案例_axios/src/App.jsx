import React, { Component } from 'react'
import Search from './component/Search'
import List from './component/List'

export default class App extends Component {

  state = {
    // 初始化 Users
    users: [],
    // 是否为第一次打开网页
    isFirstOpenLink: true,
    // 是否处于搜索中
    isLoadingOrNo: false,
    // 错误信息
    errorInfo:'',
  }

  // saveUser = (users) => {
  //   this.setState({users:users})
  // }

  updateAppState = (appStateObj) => {
    this.setState(appStateObj)
  }

  render() {
    return (
      <div className="container">
        <Search updateAppState={this.updateAppState}/>
        <List {...this.state}/>
      </div>
    )
  }
}
