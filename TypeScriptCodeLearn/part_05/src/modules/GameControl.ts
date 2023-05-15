
import Food from "./Food";
import ScorePanel from "./ScorePanel";
import Snake from "./Snake";

// 游戏控制器，控制其他的所有类
class GameControl {
    // 定义三个属性
    snake: Snake;
    food: Food;
    scorePanel: ScorePanel;

    // 存储蛇的移动方向
    direction: string = '';

    isLive: boolean = true;
    private timerId: number | null = null;

    constructor(){
        this.food = new Food;
        this.snake = new Snake;
        this.scorePanel = new ScorePanel;

        this.init()
    }

    // 初始化
    init(){
        document.addEventListener('keydown', this.keyDownHandler.bind(this))
    }

    // 键盘响应函数
    keyDownHandler(event: KeyboardEvent){
        console.log("输入值是 " + event.key)
        if (['ArrowUp', 'ArrowDown', "ArrowLeft", "ArrowRight", 'Up', 'Down', 'Left', 'Right'].includes(event.key)) {
            this.direction = event.key
        }
        console.log("蛇移动");
        this.run();
    }

    // 移动方法
    run(){
        // 根据 this.direction 修改方法
        let snakeX:number = this.snake.x;
        let snakeY:number = this.snake.y;
        
        switch (this.direction) {
            case "ArrowUp":
            case "Up":
                // 向上移动
                console.log("蛇向上移动");
                snakeY = snakeY - 10;
                break;
            case "ArrowDown":
            case "Down":
                // 向下移动
                console.log("蛇向下移动");
                snakeY = snakeY + 10;
                break;
            case "ArrowLeft":
            case "Left":                
                // 向左移动
                console.log("蛇向左移动");
                snakeX = snakeX - 10;
                break;
            case "ArrowRight":
            case "Right":
                // 向右移动
                console.log("蛇向右移动");
                snakeX = snakeX + 10;
                break;
        }

        // 检查蛇是否吃到了食物
        this.checkEat(snakeX, snakeY);

        try{
            this.snake.x = snakeX;
            this.snake.y = snakeY;
        } catch(e){
            // 出现异常
            if (e instanceof Error) {
                alert(e.message + ' GAME OVER!');
                this.isLive = false;
            }
        }
        if (this.timerId) {
            clearTimeout(this.timerId);
        }

        this.isLive && setTimeout(this.run.bind(this), 300 - (this.scorePanel.level - 1) * 30);
    }

    // 用来检查蛇是否吃到食物
    checkEat(x: number, y: number): void {
        if (x === this.food.x && y === this.food.y) {
            // 食物的位置要进行重置
            this.food.changePosition();
            // 分数增加
            this.scorePanel.addScore();
            // 蛇要增加一节
            this.snake.addBody();
        }
    }
}

export default GameControl;