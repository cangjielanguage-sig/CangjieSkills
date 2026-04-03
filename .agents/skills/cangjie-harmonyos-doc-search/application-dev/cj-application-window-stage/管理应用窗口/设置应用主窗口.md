## 设置应用主窗口

在`Stage`模型下，应用主窗口由[UIAbility](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)创建并维护生命周期。在[UIAbility](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)的[onWindowStageCreate](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#func-onwindowstagecreatewindowstage)回调中，通过`WindowStage`获取应用主窗口，即可对其进行属性设置等操作。还可以在应用配置文件中设置应用主窗口的属性，如最大窗口宽度maxWindowWidth等，详见[module.json5配置文件中的abilities标签](../cj-start/basic-knowledge/cj-module-configuration-file.md#abilities标签)。

### 开发步骤

1. 获取应用主窗口。

   通过[getMainWindow](../reference/arkui-cj/cj-apis-window.md#func-getmainwindow)接口获取应用主窗口。

2. 设置主窗口属性。

   可设置主窗口的背景色、亮度值、是否可触等多个属性，开发者可根据需要选择对应的接口。本示例以设置“是否可触”属性为例。

3. 为主窗口加载对应的目标页面。

   通过[loadContent](../reference/arkui-cj/cj-apis-window.md#func-loadcontentstring)接口加载主窗口的目标页面。

```cangjie
package ohos_app_cangjie_entry

internal import kit.AbilityKit.*
internal import kit.ArkUI.*

class MainAbility <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        // 1.获取应用主窗口。
        let mainWindow: Window = windowStage.getMainWindow()
        // 2.设置主窗口属性。以设置"是否可触"属性为例。
        mainWindow.setWindowTouchable(false)
        // 3.为主窗口加载对应的目标页面。
        windowStage.loadContent("EntryView")
    }
}
```