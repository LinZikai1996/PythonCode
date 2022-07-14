import React, { Component } from 'react'
import PubSub from 'pubsub-js'

export default class Search extends Component {

    search = async() => {

        // 获取用户输入
        console.log(this.keyWorkElement.value)
        const keyWorkElement = this.keyWorkElement.value

        // 发送请求前, 通知 list 跟新状态
        // this.props.updateAppState({isFirstOpenLink: false,isLoadingOrNo: true,})
        console.log('发送请求前, 通知 list 跟新状态')
        PubSub.publish('listInfo', {isFirstOpenLink: false,isLoadingOrNo: true,})

        // 发送网络请求
        // 未优化
        // fetch(`https://api.github.com/search/users?q=${keyWorkElement}`).then(
        //     response =>{
        //         console.log('联系服务器成功')
        //         return response.json()
        //     },
        //     // error => {
        //     //     console.log('联系服务器失败', error)
        //     //     return new Promise()
        //     // }
        // ).then(
        //     response =>{
        //         console.log('获取数据成功', response)
        //     },
        //     // error => {
        //     //     console.log('获取数据失败', error)
        //     // }
        // ).catch(
        //     (error) => {
        //         console.log(error)
        //     }
        // )
        try{
            const response = await fetch(`https://api.github.com/search/users?q=${keyWorkElement}`)
            const data = response.json()
            console.log(data)
        } catch(error){
            console.log(error)
        }
        

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
