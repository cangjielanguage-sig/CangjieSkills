## struct Asset

```cangjie
public struct Asset {
    public let name: String
    public let uri: String
    public let path: String
    public let createTime: String
    public let modifyTime: String
    public let size: String
    public let status: AssetStatus
    public init(name: String, uri: String, path: String, createTime: String, modifyTime: String,
    size: String, status!: AssetStatus = AssetStatus.ASSET_NORMAL)
}
```

**功能：** 记录资产附件（文件、图片、视频等类型文件）的相关信息。资产类型的相关接口暂不支持Datashare。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### let createTime

```cangjie
public let createTime: String
```

**功能：** 资产被创建出来的时间。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let modifyTime

```cangjie
public let modifyTime: String
```

**功能：** 资产最后一次被修改的时间。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 资产的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let path

```cangjie
public let path: String
```

**功能：** 资产在应用沙箱里的路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let size

```cangjie
public let size: String
```

**功能：** 资产占用空间的大小。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let status

```cangjie
public let status: AssetStatus
```

**功能：** 资产的状态，默认值为ASSET_NORMAL。

**类型：** [AssetStatus](#enum-assetstatus)

**读写能力：** 只读

**起始版本：** 12

### let uri

```cangjie
public let uri: String
```

**功能：** 资产的uri，在系统里的绝对路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### init(String, String, String, String, String, String, AssetStatus)

```cangjie
public init(name: String, uri: String, path: String, createTime: String, modifyTime: String, size: String, status!: AssetStatus = AssetStatus.ASSET_NORMAL)
```

**功能：** 构建Asset。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|资产的名称。|
|uri|String|是|-|资产的uri，在系统里的绝对路径。|
|path|String|是|-|资产在应用沙箱里的路径。|
|createTime|String|是|-|资产被创建出来的时间。|
|modifyTime|String|是|-|资产最后一次被修改的时间。|
|size|String|是|-|资产占用空间的大小。|
|status|[AssetStatus](#enum-assetstatus)|否|AssetStatus.ASSET_NORMAL| **命名参数。** 资产的状态，默认值为ASSET_NORMAL。|