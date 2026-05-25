## class WifiCallback0

```cangjie
public class WifiCallback0 <: Callback0Argument {
    public init(fn: () -> Unit)
}
```

**功能：** 表示没有参数的回调函数。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- [Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)

### init(() -> Unit)

```cangjie
public init(fn: () -> Unit)
```

**功能：** 创建回调函数结构体。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### func invoke()

```cangjie
public func invoke(): Unit
```

**功能：** 调用传入的回调函数，由sdk触发。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

## class WifiCallback1

```cangjie
public class WifiCallback1<T> <: Callback1Argument<T> {
    public init(fn: (T) -> Unit)
}
```

**功能：** 表示单参数的回调函数。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- [Callback1Argument\<T>](../BasicServicesKit/cj-apis-base.md#class-callback1argument)

### init((T) -> Unit)

```cangjie
public init(fn: (T) -> Unit)
```

**功能：** 创建回调函数结构体。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### func invoke(T)

```cangjie
public func invoke(arg: T): Unit
```

**功能：** 调用传入的回调函数，由sdk触发。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19