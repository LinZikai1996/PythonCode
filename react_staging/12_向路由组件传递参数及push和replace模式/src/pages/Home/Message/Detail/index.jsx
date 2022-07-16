import React, { Component } from 'react'
// 接收 search 参数
// import qs from 'query-string'

const detaiInfo = [
    {id:'001', content: 'I\'m is message-Detail-001'},
    {id:'002', content: 'I\'m is message-Detail-002'},
    {id:'003', content: 'I\'m is message-Detail-003'},
    {id:'004', content: 'I\'m is message-Detail-004'},
    {id:'005', content: 'I\'m is message-Detail-005'},
]

export default class Detail extends Component {
  render() {
    // 接收 params 参数
    // const {id, title} = this.props.match.params

    // 接收 search 参数
    // const {search} = this.props.location
    // const {id, title} = qs.parse(search.slice(1))

    // 接收 state 参数
    const {id, title} = this.props.location.state || {}

    const findResultFromDetailInfo = detaiInfo.find((detail) =>{
        return detail.id === id 
    }) || {}
    return (
        <div>
            <hr />
            <ul>
                <li>id: {id}</li>
                <li>title: {title}</li>
                <li>message content: {findResultFromDetailInfo.content}</li>
            </ul>
        </div>

    )
  }
}
