## enum SheetType

```cangjie
public enum SheetType <: Equatable<SheetType> {
    | Bottom
    | Center
    | Popup
    | ...
}
```

**功能：** 设置半模态弹窗的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SheetType](#enum-sheettype)>

### Bottom

```cangjie
Bottom
```

**功能：** 底部弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 居中弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Popup

```cangjie
Popup
```

**功能：** 跟手弹窗。跟手弹窗面板不支持跟手滑动，下滑面板不关闭。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SheetType)

```cangjie
public operator func ==(other: SheetType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SheetType](#enum-sheettype)|是|-|要比较的另一个SheetType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SheetType)

```cangjie
public operator func !=(other: SheetType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SheetType](#enum-sheettype)|是|-|要比较的另一个SheetType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum SheetMode

```cangjie
public enum SheetMode <: Equatable<SheetMode> {
    | Overlay
    | Embedded
    | ...
}
```

**功能：** 设置半模态页面的显示层级。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SheetMode](#enum-sheetmode)>

### Overlay

```cangjie
Overlay
```

**功能：** 设置半模态面板在当前UIContext内顶层显示，在所有页面之上。和弹窗类组件显示在一个层级。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Embedded

```cangjie
Embedded
```

**功能：** 设置半模态面板在当前页面内的顶层显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SheetMode)

```cangjie
public operator func ==(other: SheetMode): Bool
```

**功能：** 判断两个SheetMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SheetMode](#enum-sheetmode)|是|-|要比较的另一个SheetMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SheetMode)

```cangjie
public operator func !=(other: SheetMode): Bool
```

**功能：** 判断两个SheetMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SheetMode](#enum-sheetmode)|是|-|要比较的另一个SheetMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|