// 引入一个包

const path = require('path')

const htmlWebpackPlugin = require('html-webpack-plugin')

// webpack 中所有配置信息都应该写在 module.exports 中
module.exports = {
    // 指定入口文件
    entry: './src/index.ts',

    // 指定打包输出目录
    output: {
        // 指定目录
        path: path.resolve(__dirname, 'dist'),
        // 打包后文件名字
        filename: 'boudle.js'
    },

    // 指定webpack要打包时使用模块
    module:{
        // 指定加载规则
        rules:[
            {
                // test 指定规则生效的文件
                test: /\.ts$/,
                // 指定使用的loader
                use: 'ts-loader',
                // 指定要排除的文件
                exclude: /node-modules/
            }
        ]
    },
    plugins:{
        new htmlWebpackPlugin({
            titile: "我是自定义title"
        })
    }
};