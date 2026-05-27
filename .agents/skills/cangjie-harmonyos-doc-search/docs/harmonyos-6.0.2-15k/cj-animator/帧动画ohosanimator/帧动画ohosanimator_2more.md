# 帧动画（ohos.animator）

帧动画具备逐帧回调的特性，便于开发者在每一帧中处理需调整的属性。通过向应用提供onFrame逐帧回调，帧动画使开发者能够在应用的每一帧设置属性值，从而实现组件属性值变化的自然过渡，营造出动画效果。帧动画接口详情请参见[ohos.animator (动画)](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-animator.md)。

与属性动画相比，帧动画能让开发者实时感知动画进程，即时调整UI值，具备事件即时响应和可暂停的优势，但在性能上略逊于属性动画。当属性动画能满足需求时，建议优先采用属性动画接口实现。属性动画接口请参见[实现属性动画](cj-attribute-animation-apis.md)。

|名称|实现方式|事件响应方式|可暂停|性能|
|:---|:---|:---|:---|:---|
|帧动画（ohos.animator）|开发者可每帧修改UI侧属性值，UI侧属性实时更新|实时响应|是|较差|
|属性动画|UI侧只计算动画最终状态，动画过程为渲染值在改变，UI侧一直为动画最终状态，不感知实时渲染值|按最终状态响应|否|较好|

如图所示，帧动画在动画过程中即可实时响应，而属性动画按最终状态响应。

![animator](figures/animator1.gif)

![animator](figures/animator2.gif)

## 使用帧动画实现动画效果

使用如下步骤可以创建一个简单的animator，并且在每个帧回调中打印当前插值。

1. 引入相关依赖。

    ```cangjie
    import kit.UIKit.*
    ```

2. 创建执行动画的对象。

    ```cangjie
    // 创建动画的初始参数
    this.backAnimator = AnimatorResult(AnimatorOptions(
        duration: 1500,
        easing: "friction",
        delay: 0,
        fill: AnimatorFill.Forwards,
        direction: AnimatorDirection.Normal,
        iterations: 2,
        // 动画onFrame 插值首帧值
        begin: 200.0,
        // 动画onFrame 插值尾帧值
        end: 400.0
    ))
    var animatorOptions: AnimatorResult = AnimatorResult(AnimatorOptions(duration: 0))
    // 设置接收到帧时回调，动画播放过程中每帧会调用onFrame回调
    this.backAnimator?.onFrame =  {  progress: Float64 =>
        AppLog.info("current value is :" + progress.toString())
    }
    ```

3. 播放动画。

    ```cangjie
    // 播放动画
    this.backAnimator?.play()
    ```

4. 动画执行完成后手动释放AnimatorResult对象。

    ```cangjie
    // 释放动画对象
    this.backAnimator = None
    ```