import React, { Component } from 'react'
import axios from 'axios'

export default class Search extends Component {

    search = () => {
        // 获取用户输入
        console.log(this.keyWorkElement.value)
        const keyWorkElement = this.keyWorkElement.value

        // 发送请求前, 通知 App 跟新状态
        this.props.updateAppState({
            isFirstOpenLink: false,
            isLoadingOrNo: true,
        })

        // 发送网络请求
        axios.get(`https://api.github.com/search/users?q=${keyWorkElement}`).then(
            response =>{
                console.log('成功', response.data)
                // 发送请求成功后, 通知 App 跟新状态
                this.props.updateAppState({
                    isLoadingOrNo: false,
                    users: response.data.items,
                })
            },
            error => {
                // 发送请求失败后, 通知 App 跟新状态
                console.log('失败', error)
                this.props.updateAppState({
                    isLoadingOrNo: false,
                    errorInfo: error.message,
                })
            }
        )
    }

    // 键盘事件的回调函数
    handleKeyUp = (event) =>{
        // 解构，赋值获取keyCode, target数值
        const {keyCode, target} = event
        // 判断是否有回车按键
        if (keyCode !== 13) return
        if (target.value === ''){
            alert('输入不能为空')
            return
        }
        this.search()
        target.value = ''
    }


    render() {
        return (
            <section className="jumbotron">
                <h3 className="jumbotron-heading">Search Github Users</h3>
                <div>
                    <input ref={c => this.keyWorkElement = c} onKeyUp={this.handleKeyUp} type="text" placeholder="enter the name you search"/>&nbsp;
                    <button onClick={this.search}>Search</button>
                </div>
            </section>
        )
    }
}
