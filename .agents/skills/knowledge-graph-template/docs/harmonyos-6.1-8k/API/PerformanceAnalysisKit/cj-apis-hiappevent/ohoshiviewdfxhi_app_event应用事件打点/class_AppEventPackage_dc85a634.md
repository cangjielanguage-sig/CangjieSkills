## class AppEventPackage

```cangjie
public class AppEventPackage {
    public var packageId: Int32
    public var row: Int32
    public var size: Int32
    public var data: Array<String>
}
```

**功能：** 提供订阅返回的事件包的参数定义。可用于获取事件包的详细信息，事件包由[takeNext](#func-takenext)接口获得。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var data

```cangjie
public var data: Array<String>
```

**功能：** 事件包的事件信息。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var packageId

```cangjie
public var packageId: Int32
```

**功能：** 事件包ID，从0开始自动递增。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var row

```cangjie
public var row: Int32
```

**功能：** 事件包的事件数量。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var size

```cangjie
public var size: Int32
```

**功能：** 事件包的事件大小，单位为byte。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22