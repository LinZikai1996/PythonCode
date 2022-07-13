import proxy from 'http-proxy-middleware'

export default function(app){
	app.use(
		//遇见/api1前缀的请求，就会触发该代理配置
		proxy('/api1',{
			//请求转发给谁
			target:'http://127.0.0.1:5000/', 
			//控制服务器收到的请求头中Host的值
			changeOrigin:true,
			//重写请求路径(必须)
			pathRewrite:{'^/api1':''} 
		})
	)
}