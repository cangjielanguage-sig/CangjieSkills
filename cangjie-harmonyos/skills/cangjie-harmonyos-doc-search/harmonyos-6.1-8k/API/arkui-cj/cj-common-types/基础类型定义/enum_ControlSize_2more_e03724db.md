## enum ControlSize

```cangjie
public enum ControlSize <: Equatable<ControlSize> {
    | Small
    | Normal
    | ...
}
```

**功能：** 控制尺寸大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ControlSize](#enum-controlsize)>

### Small

```cangjie
Small
```

**功能：** 小尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Normal

```cangjie
Normal
```

**功能：** 正常尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ControlSize)

```cangjie
public operator func ==(other: ControlSize): Bool
```

**功能：** 判断两个ControlSize枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ControlSize](#enum-controlsize)|是|-|要比较的另一个ControlSize枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ControlSize)

```cangjie
public operator func !=(other: ControlSize): Bool
```

**功能：** 判断两个ControlSize枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ControlSize](#enum-controlsize)|是|-|要比较的另一个ControlSize枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum OptionWidthMode

```cangjie
public enum OptionWidthMode <: Equatable<OptionWidthMode> {
    | FitContent
    | FitTrigger
    | ...
}
```

**功能：** 下拉菜单宽度设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[OptionWidthMode](#enum-optionwidthmode)>

### FitContent

```cangjie
FitContent
```

**功能：** 设置该值时，下拉菜单宽度按默认2栅格显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### FitTrigger

```cangjie
FitTrigger
```

**功能：** 设置下拉菜单继承下拉按钮宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(OptionWidthMode)

```cangjie
public operator func ==(other: OptionWidthMode): Bool
```

**功能：** 判断两个OptionWidthMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OptionWidthMode](#enum-optionwidthmode)|是|-|要比较的另一个OptionWidthMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(OptionWidthMode)

```cangjie
public operator func !=(other: OptionWidthMode): Bool
```

**功能：** 判断两个OptionWidthMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OptionWidthMode](#enum-optionwidthmode)|是|-|要比较的另一个OptionWidthMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|