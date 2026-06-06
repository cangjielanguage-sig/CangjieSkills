# 触摸测试控制

设置组件的触摸测试类型。ArkUI开发框架在处理触屏事件时，会在触屏事件触发前，进行按压点和组件区域的触摸测试来收集需要响应触屏事件的组件，然后基于触摸测试结果分发相应的触屏事件。hitTestBehavior属性可以设置不同的触摸测试响应模式，影响组件的触摸测试收集结果，最终影响后续的触屏事件分发，具体影响参考[HitTestMode](./cj-common-types.md#enum-hittestmode)枚举说明。

> **说明：**
>
> 当Stack组件中有多个节点触摸区域重叠时，如两个节点，默认只会对显示在最上层的节点做触摸测试，若需要显示在下层的节点触发触摸测试，请给显示在上层的节点设置hitTestBehavior为HitTestMode.Transparent。

## func hitTestBehavior(HitTestMode)

```cangjie
public func hitTestBehavior(value: HitTestMode): This
```

**功能：** 设置组件的触摸测试类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 名称|类型|必填|默认值|说明|
| :------- | :---------- | :------- | :-------- | :----------|
| value | [HitTestMode](./cj-common-types.md#enum-hittestmode) | 是 | - | 设置当前组件的触摸测试类型。<br/>初始值： HitTestMode.Default |

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    func build() {
        // Outer stack
        Stack() {
            Button('outer button').backgroundColor(Color.RED).width(100.percent).onTouch(
                {
                event => Hilog.info(0, "test", 'outer button touched type: ' + event.eventType.getValue().toString())
            })
            // Inner stack
            Stack() {
                Button('inner button').width(50.percent).onTouch(
                    {
                    event => Hilog.info(0, "test", 'inner button touched type: ' + event.eventType.getValue().toString()
                    )
                })
            }.width(70.percent).height(70.percent).backgroundColor(Color.GRAY).hitTestBehavior(HitTestMode.Block).
                onTouch({
                event => Hilog.info(0, "test", 'stack touched type: ' + event.eventType.getValue().toString())
            })
            Text('Transparent').hitTestBehavior(HitTestMode.Transparent).width(100.percent).height(100.percent).onTouch(
                {
                event => Hilog.info(0, "test", 'text touched type: ' + event.eventType.getValue().toString())
            })
        }.backgroundColor(Color.BLACK).width(300.vp).height(300.vp)
    }
}
```

![uni_response_region](figures/hittestmode.png)
