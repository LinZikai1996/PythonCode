// 定义 food class

class Food{
    // 元素
    element: HTMLElement;

    constructor(){
        // 获取页面中 food 元素
        this.element = document.getElementById('food')!;
    }

    // 获取一个食物水平坐标
    get x(): number{
        return this.element.offsetLeft;
    }

    // 获取一个食物竖直坐标
    get y(): number{
        return this.element.offsetTop;
    }

    // 获取坐标信息
    get position(): [number, number]{
        return [this.x, this.y];
    }

    // 修改位置
    changePosition() {
        let top: number;
        let left: number;
        do {
            // 随机位置
            // 食物 最小位置0, 最大290
            // 蛇一步 10px, 一格就是 10px，要求食物位置为整十
            top = Math.round(Math.random() * 29) * 10;
            left = Math.round(Math.random() * 29) * 10;
        } while (top === parseInt(this.element.style.top) && left === parseInt(this.element.style.left));

        this.element.style.left = left + 'px';
        this.element.style.top = top + 'px';
    }
}
export default Food;