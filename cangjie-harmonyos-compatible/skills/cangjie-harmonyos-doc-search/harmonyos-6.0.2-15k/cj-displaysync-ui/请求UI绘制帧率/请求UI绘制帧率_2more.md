# 请求UI绘制帧率

如果开发者需要以独立的帧率绘制更新操作UI界面时，可以通过DisplaySync来实现。应用中绘制内容的帧率可以使用DisplaySync实例来控制，具体请参见[@ohos.displaySync(可变帧率)](../../API_Reference/source_zh_cn/apis/ArkGraphics2D/cj-apis-displaySync.md)。

## 开发步骤

此处以不同帧率改变文件组件字体大小为例，来模拟不同UI绘制帧率的效果。

1. 导入模块。

    ```cangjie
    import kit.ArkGraphics2D.*
    ```

2. 定义和构建DisplaySync对象。

    ```cangjie
    @Entry
    @Component
    class EntryView {
        // 定义两个DisplaySync变量，未初始化
        private var backDisplaySyncSlow: DisplaySync = DisplaySync.create()
        private var backDisplaySyncFast: DisplaySync = DisplaySync.create()
    }
    ```

3. 定义两个文本组件。

    ```cangjie
    @State
    var drawFirstSize: Int64 = 25

    @State
    var drawSecondSize: Int64 = 25

    @Builder
    func doSomeRenderFirst() {
        Text('30').fontSize(this.drawFirstSize)
    }

    @Builder
    func doSomeRenderSecond() {
        Text('60').fontSize(this.drawSecondSize)
    }
    ```

4. 通过DisplaySync实例设置帧率和注册订阅函数。

    > **说明：**
    >
    > 订阅函数运行于UI主线程，故涉及UI线程的耗时操作不应运行于订阅函数中，以免影响性能。

    ```cangjie
    func CreateDisplaySyncSlow() {
        // 定义期望绘制帧率
        let range: ExpectedFrameRateRange = ExpectedFrameRateRange( // 创建 和配置帧率参数
            expected: 30,
            min: 0,
            max: 120
        )
        let draw30 = Callback1()
        backDisplaySyncSlow = DisplaySync.create() // 创建DisplaySync实例
        backDisplaySyncSlow.getOrThrow().setExpectedFrameRateRange(range) // 设置帧率
        backDisplaySyncSlow.getOrThrow().on(OnOffType.FRAME, draw30) // 订阅frame事件和注册订阅函数

    }
    ```

5. 开始每帧回调。

    ```cangjie
    Button('Start')
        .id('CustomDrawStart')
        .fontSize(14)
        .fontWeight(FontWeight.W500)
        .margin(bottom: 10, left: 5)
        .fontColor(UIColor.WHITE)
        .onClick(
            {
                evt =>
                if (backDisplaySyncSlow.isNone()) {
                    CreateDisplaySyncSlow()
                }
                if (backDisplaySyncFast.isNone()) {
                    CreateDisplaySyncFast()
                }
                if (!backDisplaySyncSlow.isNone()) {
                    backDisplaySyncSlow
                        .getOrThrow()
                        .start() // DisplaySync使能开启
                }
                if (!backDisplaySyncFast.isNone()) {
                    backDisplaySyncFast
                        .getOrThrow()
                        .start() // DisplaySync使能开启
                }
            }
        )
        .width(20.percent)
        .height(40)
        .shadow(radius: 10, color: UIColor(0x909399), offsetX: 1, offsetY: 1)
    ```

    > **说明：**
    >
    > 创建的DisplaySync实例在start使能后需要aboutToDisappear函数中进行stop操作 并置空，避免内存泄漏问题。

    ```cangjie
    protected func aboutToDisappear() {
        if (!backDisplaySyncSlow.isNone()) {
            backDisplaySyncSlow.getOrThrow().stop() // DisplaySync失能关闭
            backDisplaySyncSlow = None // 实例置空
        }
        if (!backDisplaySyncFast.isNone()) {
            backDisplaySyncFast.getOrThrow().stop() // DisplaySync失能关闭
            backDisplaySyncFast = None // 实例置空
        }
    }
    ```

6. 结束每帧回调。

    ```cangjie
    Button('Stop')
        .id('CustomDrawStop')
        .fontSize(14)
        .fontWeight(FontWeight.W500)
        .margin(bottom: 10, left: 5)
        .fontColor(UIColor.WHITE)
        .onClick(
            {
                evt =>
                if (!backDisplaySyncSlow.isNone()) {
                    backDisplaySyncSlow
                        .getOrThrow()
                        .stop() // DisplaySync失能关闭
                }
                if (!backDisplaySyncFast.isNone()) {
                    backDisplaySyncFast
                        .getOrThrow()
                        .stop() // DisplaySync失能关闭
                }
            }
        )
        .width(20.percent)
        .height(40)
        .shadow(radius: 10, color: UIColor(0x909399), offsetX: 1, offsetY: 1)
    ```