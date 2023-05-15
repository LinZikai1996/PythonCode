class Snake{

    // 蛇元素
    element: HTMLElement
    // 蛇头元素
    headElement: HTMLElement;
    // 蛇身体（包含蛇头）
    bodies: HTMLCollection;

    constructor(){
        this.element = document.getElementById('snake')!;
        this.headElement = document.querySelector('#snake > div') as HTMLElement;
        this.bodies = this.element.getElementsByTagName('div');
    }

    // 获取水平坐标
    get x(): number{
        return this.headElement.offsetLeft;
    }

    // 设置水平坐标
    set x(value: number){
        if(this.x !== value){
            if (value < 0 || value >290){
                // 蛇撞墙了
                throw new Error("蛇撞墙了")
            }
            this.headElement.style.left = value + 'px';
        }
    }

    // 获取竖直坐标
    get y(): number{
        return this.headElement.offsetTop;
    }

    // 设置竖直坐标
    set y(value: number){
        if(this.y !== value){
            if (value < 0 || value >290){
                // 蛇撞墙了
                throw new Error("蛇撞墙了")
            }
            this.headElement.style.top = value + 'px';
        }
    }

    // 获取坐标信息
    get position(): [number, number]{
        return [this.x, this.y];
    }

    // 增加身体
    addBody(){
        this.element.insertAdjacentElement("beforeend", document.createElement('div'));
    }

}

export default Snake;