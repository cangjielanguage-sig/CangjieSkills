### Config(Action, String, ?String, ?String, ?Mode, Bool, ?String, ?HashMap\<String, String>, ?ConfigDataType, ?String, Network, Bool, Bool, Bool, Bool, UInt32, Int64, Int64, Bool, Bool, ?String, UInt32, ?HashMap\<String, String>)

```cangjie
public Config(
    public var action!: Action,
    public var url!: String,
    public var title!: ?String = None,
    public var description!: ?String = None,
    public var mode!: ?Mode = None,
    public var overwrite!: Bool = false,
    public var method!: ?String= None,
    public var headers!: ?HashMap<String, String> = None,
    public var data!: ?ConfigDataType = None,
    public var saveas!: ?String = None,
    public var network!: Network = Network.ANY,
    public var metered!: Bool = false,
    public var roaming!: Bool = true,
    public var retry!: Bool = true,
    public var redirect!: Bool = true,
    public var index!: UInt32 = 0,
    public var begins!: Int64 = 0,
    public var ends!: Int64 = -1,
    public var gauge!: Bool = false,
    public var precise!: Bool = false,
    public var token!: ?String = None,
    public var priority!: UInt32 = 0,
    public var extras!: ?HashMap<String, String> = None
)
```

**功能：** 创建Config对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**参数：**