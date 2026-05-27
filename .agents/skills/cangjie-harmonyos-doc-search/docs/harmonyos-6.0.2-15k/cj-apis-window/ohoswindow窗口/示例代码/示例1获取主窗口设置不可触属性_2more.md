### 示例1（获取主窗口设置不可触属性）

设置主窗口属性为不可触后，点击页面中的按钮将不会有弹窗。

<!-- run -example1 -->

```cangjie
// main_ability.cj

package ohos_app_cangjie_entry

internal import kit.UIKit.*
internal import kit.AbilityKit.*
internal import kit.ArkUI.*

class MainAbility <: Ability {
    public init() {
        super()
        registerSelf()
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        // 1.获取应用主窗口。
        var window: Window = windowStage.getMainWindow()

        // 2.设置窗口主属性。以设置 ”是否可触“ 属性为例。
        window.setWindowTouchable(false)

        // 3. 为主窗口加载对应的目标页面
        windowStage.loadContent("newPage")
    }
}
```

<!-- run -example1 -->

```cangjie
// newPage.cj

package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class newPage {
    func build() {
        Flex(FlexParams(justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center)) {
            Column {
                Text("New Page")
                Button("Untouchable").onClick {
                    => AlertDialog.show(AlertDialogParamWithConfirm("Unreachable"))
                }.margin(10.vp)
            }.margin(10.vp)
        }
    }
}
```

![img1](figures/window_touchable_is_false.png)

### 示例2（主窗口监听键盘高度变化事件）

<!-- run -example2 -->

```cangjie
// main_ability.cj

package ohos_app_cangjie_entry

internal import kit.AbilityKit.*
internal import kit.UIKit.*

class MainAbility <: Ability {
    public init() {
        super()
        registerSelf()
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        windowStage.loadContent("newPage")
        // 将该Ability的窗口管理器传入AppStorage中
        AppStorage.setOrCreate("windowStage", windowStage)
    }
}
```

<!-- run -example2 -->

```cangjie
//newPage.cj

package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.ArkUI.*
import ohos.hilog.*
import ohos.state_macro_manage.*

@Entry
@Component
class newPage {
    public override func onPageShow() {
        let windowStage: WindowStage = AppStorage.get<WindowStage>("windowStage").getOrThrow()
        let mainWindow: Window = windowStage.getMainWindow()

        // 开启监听
        var tmp: Unit = mainWindow.on("keyboardHeightChange", TestCallback(0))
    }

    func build() {
        Flex(FlexParams(justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center)) {
            Column {
                TextInput(placeholder: 'input some words here... ').margin(10.vp)
            }.margin(10.vp)
        }
    }
}

public class TestCallback <: Callback1Argument<UInt32> {
    var count: Int64

    public init(count: Int64) {
        this.count = count
    }

    public func invoke(value: UInt32): Unit {
        count++
        // 拉起或隐藏键盘时，会触发日志打印总计的键盘高度变化计数
        Hilog.info(0, "", "KeyboardHeightChangeCount: ${this.count}")
    }
}
```

运行后点击文本框触发回调，在日志中查看效果，打印日志如下。

```text
KeyboardHeightChangeCount: 1
KeyboardHeightChangeCount: 2
KeyboardHeightChangeCount: 3
```