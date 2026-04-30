# 获取应用异常退出原因

当应用异常退出后再次启动时，开发者往往需要获取上次异常退出的具体原因和当时的应用状态信息，比如应用内存占用的rss、pss值、上次应用退出的时间等等。通过UIAbility和UIExtensionAbility的OnCreate生命周期函数中的launchParam参数，开发者可以获取到相关信息，并将其应用于应用体验的分析改进，从而调整业务逻辑、提高应用的存活率。

## 约束限制

仅[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)和[UIExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiextensionability)支持获取上次的退出原因。

## 接口说明

接口详情参见[API参考](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md)。

| **接口名**  | **描述** |
| -------- | -------- |
| [LaunchParam](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-launchparam)       | 启动参数。此接口的lastExitReason、lastExitMessage成员记录UIAbility上次异常退出的信息。  |

## 开发步骤

1. 获取UIAbility上次退出的原因。

    在UIAbility类的OnCreate成员函数的launchParam参数中读取UIAbility上次退出的信息。

    ```cangjie
    import kit.AbilityKit.{UIAbility, Want, LaunchParam}
    import kit.UIKit.AppLog

    func doSomeing() {
        AppLog.info("do something")
    }

    func doAnotherThing() {
        AppLog.info("do another thing")
    }

    class MainAbility <: UIAbility {
        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            let reason = launchParam.launchReason
            let exitMsg = launchParam.lastExitMessage
        }
    }
    ```

2. 根据上次退出的信息做相应的业务处理。

    对于不同的退出原因，开发者可以增加不同的处理逻辑，例如：

    ```cangjie
    match (reason) {
        case LastExitReason.APP_FREEZE =>
            // UIAbility上次因无响应而退出，此处可增加处理逻辑。
            doSomething()
        case LastExitReason.RESOURCE_CONTROL =>
            // UIAbility上次因rss管控而退出，此处可实现处理逻辑，最简单的就是打印出来。
            AppLog.info(
            "The ability has exit last because the rss control, lastExitMessage is" + exitMsg)
        case _ => doAnotherThing()
    }
    ```
