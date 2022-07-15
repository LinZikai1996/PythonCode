import React, { Component } from 'react'
import {Route, Switch} from 'react-router-dom'
// Home, About 是路由组件
import Home from './pages/Home'
import About from './pages/About'
// Header 是一般组件
import Header from './component/Header'
import MyNavLink from './component/MyNavlink'

export default class App extends Component {
  render() {
    return (
      <div>
        <div className="row">
          <div className="col-xs-offset-2 col-xs-8">
            <div className="page-header">
              <Header />
            </div>
          </div>
        </div>

        <div className="row">
          <div className="col-xs-2 col-xs-offset-2">
            <div className="list-group">
              {/* 在原生html中，靠<a>跳转不同页面 */}
              {/* <a className="list-group-item" href="./about.html">About</a>
              <a className="list-group-item active" href="./home.html">Home</a> */}

              {/* 在React中靠路由链接实现切换组件 -- 编写路由连接 */}
              <MyNavLink to='/about'>About</MyNavLink>
              <MyNavLink to='/home'>Home</MyNavLink>
            </div>
          </div>
          <div className="col-xs-6">
            <div className="panel">
              <div className="panel-body">
                {/* 注册路由 */}
                <Switch>
                  <Route path='/about' component={About}/>
                  <Route path='/home' component={Home}/>
                </Switch>  
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
