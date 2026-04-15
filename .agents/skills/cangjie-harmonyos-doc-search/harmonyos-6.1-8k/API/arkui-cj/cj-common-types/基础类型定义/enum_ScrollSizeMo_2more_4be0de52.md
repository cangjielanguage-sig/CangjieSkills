## enum ScrollSizeMode

```cangjie
public enum ScrollSizeMode <: Equatable<ScrollSizeMode> {
    | FollowDetent
    | Continuous
    | ...
}
```

**功能：** 设置半模态面板滑动时，内容区域刷新时机。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ScrollSizeMode](#enum-scrollsizemode)>

### FollowDetent

```cangjie
FollowDetent
```

**功能：** 设置半模态面板跟手滑动结束后更新内容显示区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Continuous

```cangjie
Continuous
```

**功能：** 设置半模态面板在滑动过程中持续更新内容显示区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ScrollSizeMode)

```cangjie
public operator func ==(other: ScrollSizeMode): Bool
```

**功能：** 判断两个ScrollSizeMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollSizeMode](./cj-common-types.md#enum-scrollsizemode)|是|-|要比较的另一个ScrollSizeMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ScrollSizeMode)

```cangjie
public operator func !=(other: ScrollSizeMode): Bool
```

**功能：** 判断两个ScrollSizeMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollSizeMode](./cj-common-types.md#enum-scrollsizemode)|是|-|要比较的另一个ScrollSizeMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum KeySource

```cangjie
public enum KeySource <: Equatable<KeySource> {
    | Unknown
    | Keyboard
    | ...
}
```

**功能：** 按键来源。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[KeySource](#enum-keysource)>

### Unknown

```cangjie
Unknown
```

**功能：** 输入设备类型未知。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Keyboard

```cangjie
Keyboard
```

**功能：** 键盘按键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(KeySource)

```cangjie
public operator func ==(other: KeySource): Bool
```

**功能：** 判断两个KeySource枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeySource](#enum-keysource)|是|-|要比较的另一个KeySource枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(KeySource)

```cangjie
public operator func !=(other: KeySource): Bool
```

**功能：** 判断两个KeySource枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeySource](#enum-keysource)|是|-|要比较的另一个KeySource枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|