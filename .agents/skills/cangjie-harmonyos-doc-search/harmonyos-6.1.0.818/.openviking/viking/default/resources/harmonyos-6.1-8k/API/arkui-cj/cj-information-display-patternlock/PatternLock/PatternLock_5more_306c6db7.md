# PatternLock

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

图案密码锁组件，以九宫格图案的方式输入密码，用于密码验证场景。手指在PatternLock组件区域按下时开始进入输入状态，手指离开屏幕时结束输入状态完成密码输入。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?PatternLockController)

```cangjie
public init(controller!: ?PatternLockController = None)
```

**功能：** 创建一个PatternLock组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|controller|?[PatternLockController](#class-patternlockcontroller)|否|None|**命名参数。** 设置PatternLock组件控制器，可用于控制组件状态重置。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。