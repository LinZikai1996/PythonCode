import React, { Component } from 'react'
import './index.css'

export default class List extends Component {
  render() {
    const {users, isFirstOpenLink, isLoadingOrNo, errorInfo} = this.props
    return (
        <div className="row">
            {
                isFirstOpenLink? <h1>欢迎使用，输入关键字，随后点击搜索</h1> : 
                isLoadingOrNo? <h1>数据正在加载 .... </h1> : 
                errorInfo? <h1>{errorInfo}</h1> : 
                users.map((user) => {
                    return (
                        <div key={user.id} className="card">
                            <a href={user.html_url} target="_blank" rel='noreferrer'>
                                <img alt='head_portrait' src={user.avatar_url} style={{width:'100px'}}/>
                            </a>
                            <p className="card-text">{user.login}</p>
                        </div>
                    )
                })
            }
        </div>
    )
  }
}
