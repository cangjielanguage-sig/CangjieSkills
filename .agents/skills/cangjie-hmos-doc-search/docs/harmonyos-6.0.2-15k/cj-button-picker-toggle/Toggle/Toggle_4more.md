# Toggle

组件提供勾选框样式、状态按钮样式及开关样式。

## 子组件

仅当ToggleType为ButtonType时可包含子组件。

## 创建组件

### init(ToggleType, Bool)

```cangjie
public init(toggleType: ToggleType, isOn!: Bool = false)
```

**功能：** 创建一个Toggle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|toggleType|[ToggleType](#enum-toggletype)|是|-|开关类型。<br>初始值：ToggleType.Switch。|
|isOn|Bool|否|false| **命名参数。** 开关是否打开。true：打开，false：关闭。<br>初始值：false。|

### init(ToggleType, Bool, () -> Unit)

```cangjie
public init(toggleType: ToggleType, isOn: Bool, subcomponent: () -> Unit)
```

**功能：** 创建一个Toggle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|toggleType|[ToggleType](#enum-toggletype)|是|-|开关类型。<br>初始值：ToggleType.Switch。|
|isOn|Bool|是|-|开关是否打开。true：打开，false：关闭。<br>初始值：false。|
|subcomponent|()->Unit|是|-|声明子组件。|

## 通用属性/通用事件

通用属性：全部支持

通用事件：全部支持。