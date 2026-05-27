## struct CArrInt32

```cangjie
public struct CArrInt32 {
    public CArrInt32(
        public let head: CPointer<Int32>,
        public let size: Int64
    )
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let head

```cangjie
public let head: CPointer<Int32>
```

**功能：** UI框架使用。

**类型：** CPointer\<Int32>

**读写能力：** 只读

**起始版本：** 12

### let size

```cangjie
public let size: Int64
```

**功能：** UI框架使用。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### CArrInt32(CPointer\<Int32>, Int64)

```cangjie
public CArrInt32(
    public let head: CPointer<Int32>,
    public let size: Int64
)
```

**功能：** 创建CArrInt32类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|head|CPointer\<Int32>|是|-|数组头指针。|
|size|Int64|是|-|数组长度。|

## struct CJTouchTestInfo<sup>(deprecated)</sup>

```cangjie
public struct CJTouchTestInfo {}
```

**功能：** 当前按压点所在组件的坐标系、id和尺寸相关信息。

> **注意：**
>
> 即将弃用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## struct CTouchResult<sup>(deprecated)</sup>

```cangjie
public struct CTouchResult {}
```

**功能：** 自定义事件分发结果，开发者通过返回结果来影响事件分发。

> **注意：**
>
> 即将弃用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## struct ExternalString

```cangjie
public struct ExternalString {
    public init(value: String)
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(String)

```cangjie
public init(value: String)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|字符串值。|

### func free()

```cangjie
public unsafe func free(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func isNull()

```cangjie
public func isNull(): Bool
```

**功能：** 判断字符串对象是否为null。UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|判断结果。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|字符串值。|