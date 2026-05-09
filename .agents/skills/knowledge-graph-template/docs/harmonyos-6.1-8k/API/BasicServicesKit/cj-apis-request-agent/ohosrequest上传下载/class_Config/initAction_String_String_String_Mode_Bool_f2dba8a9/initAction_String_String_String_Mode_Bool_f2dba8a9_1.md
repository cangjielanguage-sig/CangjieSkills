### init(Action, String, ?String, String, Mode, Bool, ?String, HashMap\<String,String>, ?ConfigData, String, Network, Bool, Bool, Bool, Bool, UInt32, Int64, Int64, Bool, Bool, ?String, UInt32, HashMap\<String,String>)

```cangjie
public init(action: Action, url: String, title!: ?String = None, description!: String = "",
    mode!: Mode = Mode.Background, overwrite!: Bool = false, method!: ?String = None,
    headers!: HashMap<String, String> = HashMap<String, String>(), data!: ?ConfigData = None, saveas!: String = "./",
    network!: Network = Network.AnyType, metered!: Bool = false, roaming!: Bool = true, retry!: Bool = true,
    redirect!: Bool = true, index!: UInt32 = 0, begins!: Int64 = 0, ends!: Int64 = -1, gauge!: Bool = false,
    precise!: Bool = false, token!: ?String = None, priority!: UInt32 = 0,extras!: HashMap<String, String> = HashMap<String, String>()
)
```

**功能：** 创建Config对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**