# PatternLock

图案密码锁组件，以九宫格图案的方式输入密码，用于密码验证场景。手指在PatternLock组件区域按下时开始进入输入状态，手指离开屏幕时结束输入状态完成密码输入。

## 子组件

无

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建一个PatternLock组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(PatternLockController)

```cangjie
public init(controller: PatternLockController)
```

**功能：** 创建一个PatternLock组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|controller|[PatternLockController](#class-patternlockcontroller)|是|-|设置PatternLock组件控制器，可用于控制组件状态重置。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。