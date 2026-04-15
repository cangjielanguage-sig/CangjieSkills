## enum ToggleType

```cangjie
public enum ToggleType <: Equatable<ToggleType> {
    | Checkbox
    | Switch
    | Button
    | ...
}
```

**功能：** 开关组件类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ToggleType](#enum-toggletype)>

### Checkbox

```cangjie
Checkbox
```

**功能：** 提供单选框样式。
Checkbox默认样式为圆形。
通用属性margin的默认值为：top 14.px, right 14.px, bottom 14.px, left 14.px。
默认尺寸为：宽为20.vp, 高为20.vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Switch

```cangjie
Switch
```

**功能：** 提供开关样式。
通用属性margin的默认值为：top 6.px, right 14.px, bottom 6.px, left 14.px。
默认尺寸为：宽为36.vp, 高为20.vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Button

```cangjie
Button
```

**功能：** 提供状态按钮样式，如果子组件有文本设置，则相应的文本内容会显示在按钮内部。
初始尺寸为：高为28.vp，宽无初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ToggleType)

```cangjie
public operator func ==(other: ToggleType): Bool
```

**功能：** 判断两个ToggleType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ToggleType](#enum-toggletype)|是|-|要比较的另一个ToggleType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ToggleType)

```cangjie
public operator func !=(other: ToggleType): Bool
```

**功能：** 判断两个ToggleType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ToggleType](#enum-toggletype)|是|-|要比较的另一个ToggleType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|