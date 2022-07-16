import React, { Component } from 'react'
import { Button } from 'antd';
import {WechatOutlined} from '@ant-design/icons'

export default class App extends Component {
  render() {
    return (
      <div>
        <Button type="primary">Primary Button</Button>
        <Button type="ghost">Primary Button</Button>
        <Button type="dashed">Primary Button</Button>
        <Button type="link">Primary Button</Button>
        <Button type="text">Primary Button</Button>
        <Button type="default">Primary Button</Button>
        <WechatOutlined />
      </div>
    )
  }
}
