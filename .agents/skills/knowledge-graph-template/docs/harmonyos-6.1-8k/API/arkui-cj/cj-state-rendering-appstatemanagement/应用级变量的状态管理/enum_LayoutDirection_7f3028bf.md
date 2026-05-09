## enum LayoutDirection

```cangjie
public enum LayoutDirection <: Equatable<LayoutDirection> {
    | Ltr
    | Rtl
    | Auto
    | ...
}
```

**功能：** 定义设备的布局方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[LayoutDirection](#enum-layoutdirection)>

### Ltr

```cangjie
Ltr
```

**功能：** 从左到右布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Rtl

```cangjie
Rtl
```

**功能：** 从右到左布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Auto

```cangjie
Auto
```

**功能：** 自动布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(LayoutDirection)

```cangjie
public operator func !=(other: LayoutDirection): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LayoutDirection](#enum-layoutdirection)|是|-|要比较的另一个LayoutDirection实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(LayoutDirection)

```cangjie
public operator func ==(other: LayoutDirection): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LayoutDirection](#enum-layoutdirection)|是|-|要比较的另一个LayoutDirection实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|