import React, { Component } from 'react'
import {Link, Route} from 'react-router-dom'
// 路由组件
import Detail from './Detail'

export default class Message extends Component {

    state = {
        messageList:[
            {id:'001', title: 'message001'},
            {id:'002', title: 'message002'},
            {id:'003', title: 'message003'},
            {id:'004', title: 'message004'},
            {id:'005', title: 'message005'},
        ]
    }

    relaceShowDatailInfo = (id, title) => {
        //replace跳转+携带params参数
        // return () =>{
        //     this.props.history.replace(`/home/message/detail/${id}/${title}`)
        // }
        //replace跳转+携带search参数
        // return () =>{
        //     this.props.history.replace(`/home/message/detail?id=${id}&title=${title}`)
        // }

		//replace跳转+携带state参数
        return () =>{
            this.props.history.replace(`/home/message/detail`,{id,title})
        }
        
    }

    pushShowDatailInfo = (id, title) => {
        //replace跳转+携带params参数
        // return () =>{
        //     this.props.history.push(`/home/message/detail/${id}/${title}`)
        // }

        //push跳转+携带search参数
        // return () =>{
        //     this.props.history.push(`/home/message/detail?id=${id}&title=${title}`)
        // }

        //push跳转+携带state参数
        return () =>{
            this.props.history.push(`/home/message/detail`,{id,title})
        }	
    }

    back = () => {
        this.props.history.goBack()
    }

    forward = () =>{
        this.props.history.goForward()
    }

    go = () =>{
        this.props.history.go(2)
    }

    render() {
        const messageList = this.state.messageList
        return (
            <div>
                <ul>
                    {
                        messageList.map((message) =>{
                            return (
                                <li key={message.id}>
                                    {/* 向路由组件传递 params 参数 */}
                                    {/* <Link to={`/home/message/detail/${message.id}/${message.title}`}>{message.title}</Link>&nbsp;&nbsp; */}

                                    {/* 向路由组件传递 search 参数 */}
                                    {/* <Link to={`/home/message/detail/?id=${message.id}&title=${message.title}`}>{message.title}</Link>&nbsp;&nbsp; */}

                                    {/* 向路由组件传递 state 参数 */}
                                    <Link to={{pathname:'/home/message/detail', state:{id:message.id, title: message.title}}}>{message.title}</Link>&nbsp;&nbsp;
                                    <button onClick={this.pushShowDatailInfo(message.id, message.title)}>push 查看消息</button>&nbsp;&nbsp;
                                    <button onClick={this.relaceShowDatailInfo(message.id, message.title)}>replace 查看消息</button>
                                </li>
                            )
                        })
                    }
                </ul>
                {/* 声明接受 params 参数 */}
                {/* <Route path="/home/message/detail/:id/:title" component={Detail}/> */}

                {/* 声明接受 search 参数, 无需声明接收, 正常路由声明 */}
                {/* <Route path="/home/message/detail" component={Detail}/> */}

                {/* 声明接受 state 参数, 无需声明接收, 正常路由声明 */}
                <Route path="/home/message/detail" component={Detail}/>

                <button onClick={this.back}>回退</button>
                <button onClick={this.forward}>前进</button>
                <button onClick={this.go}>go</button>
            </div>
            
        )
  }
}
