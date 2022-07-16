import React, { Component } from 'react'
import {Route, Switch, Redirect} from 'react-router-dom'
// 路由组件
import News from './News'
import Message from './Message'
// 一般组件
import MyNavLink from '../../component/MyNavlink'

export default class Home extends Component {
  render() {
    return (
      <div>
        <h1>
            我是Home的内容
        </h1>
        <div>
          <ul className="nav nav-tabs">
            <li>
              <MyNavLink to='/home/news'>News</MyNavLink>
            </li>
            <li>
              <MyNavLink to='/home/message'>Message</MyNavLink>
            </li>
          </ul>
          {/* 注册路由 */}
          <Switch>
            <Route path='/home/news' component={News}/>
            <Route path='/home/message' component={Message}/>
            <Redirect to='/home/news'></Redirect>
          </Switch>
        </div>
      </div>
        
    )
  }
}
