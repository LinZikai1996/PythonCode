// 定义 score panel class
class ScorePanel{

    score:number = 0;
    level:number = 0;
    // 限制等级
    maxLevel: number;
    // 限制升级分数
    upgradeScore: number;

    scoreElement: HTMLElement;
    levelElement: HTMLElement;
    
    constructor(maxLevel: number = 15, upgradeScore: number = 10){
        this.scoreElement = document.getElementById("score")!;
        this.levelElement = document.getElementById("level")!;
        this.maxLevel = maxLevel;
        this.upgradeScore = upgradeScore
    }
    
    // 加分方法
    addScore(){
        // 分数自增
        this.scoreElement.innerHTML = (++this.score).toString();

        // 判断一下分数多少, 然后升级
        if(this.score % this.upgradeScore === 0){
            this.levelUp();
        }
    }

    // 升级方法
    levelUp(){
        if (this.level < this.maxLevel){
            // 等级自增
            this.levelElement.innerHTML = (++this.level).toString();
        }
    }
}
export default ScorePanel;