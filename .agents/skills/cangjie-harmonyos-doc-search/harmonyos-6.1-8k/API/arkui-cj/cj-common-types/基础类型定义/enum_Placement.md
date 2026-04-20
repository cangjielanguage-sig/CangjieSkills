## enum Placement

```cangjie
public enum Placement <: Equatable<Placement> {
    | Left
    | Right
    | Top
    | Bottom
    | TopLeft
    | TopRight
    | BottomLeft
    | BottomRight
    | LeftTop
    | LeftBottom
    | RightTop
    | RightBottom
    | ...
}
```

**功能：** 气泡提示位置设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[Placement](#enum-placement)>

### Left

```cangjie
Left
```

**功能：** 气泡提示位于组件左侧，与组件左侧中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 气泡提示位于组件右侧，与组件右侧中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Top

```cangjie
Top
```

**功能：** 气泡提示位于组件上侧，与组件上侧中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 气泡提示位于组件下侧，与组件下侧中心对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TopLeft

```cangjie
TopLeft
```

**功能：** 气泡提示位于组件上侧，与组件左侧边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TopRight

```cangjie
TopRight
```

**功能：** 气泡提示位于组件上侧，与组件右侧边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomLeft

```cangjie
BottomLeft
```

**功能：** 气泡提示位于组件下侧，与组件左侧边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomRight

```cangjie
BottomRight
```

**功能：** 气泡提示位于组件下侧，与组件右侧边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LeftTop

```cangjie
LeftTop
```

**功能：** 气泡提示位于组件左侧，与组件上侧边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LeftBottom

```cangjie
LeftBottom
```

**功能：** 气泡提示位于组件左侧，与组件下侧边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### RightTop

```cangjie
RightTop
```

**功能：** 气泡提示位于组件右侧，与组件上侧边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### RightBottom

```cangjie
RightBottom
```

**功能：** 气泡提示位于组件右侧，与组件下侧边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(Placement)

```cangjie
public operator func ==(other: Placement): Bool
```

**功能：** 判断两个Placement枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Placement](#enum-placement)|是|-|要比较的另一个Placement枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(Placement)

```cangjie
public operator func !=(other: Placement): Bool
```

**功能：** 判断两个Placement枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Placement](#enum-placement)|是|-|要比较的另一个Placement枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|