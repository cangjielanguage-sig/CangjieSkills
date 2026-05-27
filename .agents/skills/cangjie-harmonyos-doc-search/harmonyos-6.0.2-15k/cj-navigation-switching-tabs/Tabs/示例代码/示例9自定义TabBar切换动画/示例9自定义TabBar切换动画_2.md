func getCurrentIndicatorInfo(index: Int32, event: TabsAnimationEvent): HashMap<String, Float64> {
        var nextIndex: Int32 = index
        if (index > 0 && (event.currentOffset < 0.0 || event.currentOffset > 0.0)) {
            nextIndex--
        } else if (index < 3 && (event.currentOffset > 0.0 || event.currentOffset < 0.0)) {
            nextIndex++
        }
        let indexInfo = this.textInfos[Int64(index)]
        let nextIndexInfo = this.textInfos[Int64(nextIndex)]
        let swipeRatio: Float64 = abs(Float64(event.currentOffset) / this.tabsWidth)
        // 页面滑动超过一半，tabBar切换到下一页。
        let currentIndexTmp = if (swipeRatio > 0.5) {
            index
        } else {
            nextIndex
        }

        let currentLeft = indexInfo[0] + (nextIndexInfo[0] - indexInfo[0]) * swipeRatio
        let currentWidth = indexInfo[1] + (nextIndexInfo[1] - indexInfo[1]) * swipeRatio
        return HashMap<String, Float64>(
            [("index", Float64(currentIndexTmp)), ("left", currentLeft), ("width", currentWidth)])
    }

    func startAnimateTo(duration: Int32, leftMargin: Float64, width: Float64) {
        this.isStartAnimateTo = true
        animateTo(
            AnimateParam(
                duration: duration, // 动画时长
                curve: Curve.Linear, // 动画曲线
                iterations: 1, // 播放次数
                playMode: PlayMode.Normal, // 动画模式
                onFinish: {=> this.isStartAnimateTo = false}
            ),
            {=> this.setIndicatorAttr(leftMargin, width)}
        )
    }

    func setIndicatorAttr(leftMargin: Float64, width: Float64) {
        this.indicatorWidth = width
        this.indicatorLeftMargin = leftMargin
    }
}
```

![tab](figures/tabsExample9.gif)