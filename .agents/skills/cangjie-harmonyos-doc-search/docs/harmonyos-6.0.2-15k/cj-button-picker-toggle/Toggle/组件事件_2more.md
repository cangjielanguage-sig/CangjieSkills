## 组件事件

### func onChange((Bool) -> Unit)

```cangjie
public func onChange(callback: (Bool) -> Unit): This
```

**功能：** 开关状态切换时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Bool)->Unit|是|-|为true时，代表状态从关切换为开。false时，代表状态从开切换为关。|

## 基础类型定义

### enum ToggleType

```cangjie
public enum ToggleType {
    | CheckboxType
    | SwitchType
    | ButtonType
}
```

**功能：** 开关组件类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### CheckboxType

```cangjie
CheckboxType
```

**功能：** 提供单选框样式。
Checkbox默认样式为圆形。
通用属性margin的默认值为：top 14.px, right 14.px, bottom 14.px, left 14.px。
默认尺寸为：宽为20.vp, 高为20.vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### SwitchType

```cangjie
SwitchType
```

**功能：** 提供开关样式。
通用属性margin的默认值为：top 6.px, right 14.px, bottom 6.px, left 14.px。
默认尺寸为：宽为36.vp, 高为20.vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### ButtonType

```cangjie
ButtonType
```

**功能：** 提供状态按钮样式，如果子组件有文本设置，则相应的文本内容会显示在按钮内部。
初始尺寸为：高为28.vp，宽无初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12