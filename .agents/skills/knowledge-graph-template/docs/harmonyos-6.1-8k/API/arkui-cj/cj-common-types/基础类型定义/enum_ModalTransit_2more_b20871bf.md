## enum ModalTransition

```cangjie
public enum ModalTransition <: Equatable<ModalTransition> {
    | Default
    | None
    | Alpha
    | ...
}
```

**功能：** 全屏模态切换动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ModalTransition](#enum-modaltransition)>

### Default

```cangjie
Default
```

**功能：** 全屏模态上下切换动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 全屏模态无转场动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Alpha

```cangjie
Alpha
```

**功能：** 全屏模态透明度渐变动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ModalTransition)

```cangjie
public operator func ==(other: ModalTransition): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ModalTransition](#enum-modaltransition)|是|-|要比较的另一个ModalTransition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ModalTransition)

```cangjie
public operator func !=(other: ModalTransition): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ModalTransition](#enum-modaltransition)|是|-|要比较的另一个ModalTransition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum SheetSize

```cangjie
public enum SheetSize <: Equatable<SheetSize> {
    | Medium
    | Large
    | FitContent
    | ...
}
```

**功能：** 设置半模态页面的切换高度档位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SheetSize](#enum-sheetsize)>

### Medium

```cangjie
Medium
```

**功能：** 指定半模态高度为屏幕高度一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Large

```cangjie
Large
```

**功能：** 指定半模态高度几乎为屏幕高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### FitContent

```cangjie
FitContent
```

**功能：** 指定半模态高度为适应内容的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SheetSize)

```cangjie
public operator func ==(other: SheetSize): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SheetSize](#enum-sheetsize)|是|-|要比较的另一个SheetSize枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SheetSize)

```cangjie
public operator func !=(other: SheetSize): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SheetSize](#enum-sheetsize)|是|-|要比较的另一个SheetSize枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|