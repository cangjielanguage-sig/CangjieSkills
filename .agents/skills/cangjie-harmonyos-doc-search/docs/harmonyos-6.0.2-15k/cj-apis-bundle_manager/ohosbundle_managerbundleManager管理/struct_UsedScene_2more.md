## struct UsedScene

```cangjie
public struct UsedScene {
    public var abilities: Array<String>
    public var when: String
    public init(abilities: Array<String>, when: String)
}
```

**功能：** 描述权限使用的场景和时机。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### var abilities

```cangjie
public var abilities: Array<String>
```

**功能：** 使用到该权限的Ability集合。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var when

```cangjie
public var when: String
```

**功能：** 使用该权限的时机。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### init(Array\<String>, String)

```cangjie
public init(abilities: Array<String>, when: String)
```

**功能：** 创建描述权限使用的场景和时机的对象。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilities|Array\<String>|是|-|使用到该权限的Ability集合。|
|when|String|是|-|使用该权限的时机。|

## struct WindowSize

```cangjie
public struct WindowSize {
    public let maxWindowRatio: Float64
    public let minWindowRatio: Float64
    public let maxWindowWidth: UInt32
    public let minWindowWidth: UInt32
    public let maxWindowHeight: UInt32
    public let minWindowHeight: UInt32
}
```

**功能：** 描述窗口尺寸。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let maxWindowHeight

```cangjie
public let maxWindowHeight: UInt32
```

**功能：** 表示自由窗口状态下窗口的最大高度，宽度单位为vp。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let maxWindowRatio

```cangjie
public let maxWindowRatio: Float64
```

**功能：** 表示自由窗口状态下窗口的最大宽高比，取值范围0-1。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let maxWindowWidth

```cangjie
public let maxWindowWidth: UInt32
```

**功能：** 表示自由窗口状态下窗口的最大宽度，宽度单位为vp。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let minWindowHeight

```cangjie
public let minWindowHeight: UInt32
```

**功能：** 表示自由窗口状态下窗口的最小高度，宽度单位为vp。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let minWindowRatio

```cangjie
public let minWindowRatio: Float64
```

**功能：** 表示自由窗口状态下窗口的最小宽高比，取值范围0-1。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let minWindowWidth

```cangjie
public let minWindowWidth: UInt32
```

**功能：** 表示自由窗口状态下窗口的最小宽度，宽度单位为vp。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12