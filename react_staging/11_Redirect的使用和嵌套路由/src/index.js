// 引入React 核心库
import React from 'react';
// 引入ReactDOM
import ReactDOM from 'react-dom/client';
// 引入路由
import { BrowserRouter} from 'react-router-dom'

// 引入App
import App from './App';

// 渲染 App 到页面
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);