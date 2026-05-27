## class ChangeData

```cangjie
public class ChangeData {}
```

**功能：** 监听器回调函数的值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### let \`type\`

```cangjie
public let `type`: NotifyType
```

**功能：** ChangeData的通知类型。

**类型：** [NotifyType](#enum-notifytype)

**读写能力：** 只读

**起始版本：** 19

### let extraUris

```cangjie
public let extraUris: Array<String>
```

**功能：** 相册中变动文件的uri数组。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### let uris

```cangjie
public let uris: Array<String>
```

**功能：** 相同[NotifyType](#enum-notifytype)的所有uri，可以是PhotoAsset或Album。。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

## class FetchOptions

```cangjie
public class FetchOptions {
    public FetchOptions(
        public var fetchColumns!: Array<String> = [],
        public var predicates!: DataSharePredicates = DataSharePredicates()
    )
}
```

**功能：** 检索条件。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### var fetchColumns

```cangjie
public var fetchColumns: Array<String> = []
```

**功能：** 检索条件。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var predicates

```cangjie
public var predicates: DataSharePredicates = DataSharePredicates()
```

**功能：** 谓词查询。

**类型：** [DataSharePredicates](../ArkData/cj-apis-data_share_predicates.md#class-datasharepredicates)

**读写能力：** 可读写

**起始版本：** 19

### FetchOptions(Array\<String>, DataSharePredicates)

```cangjie
public FetchOptions(
    public var fetchColumns!: Array<String> = [],
    public var predicates!: DataSharePredicates = DataSharePredicates()
)
```

**功能：** 构造FetchOptions对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fetchColumns|Array\<String>|否|\[]| **命名参数。** 检索条件，指定列名查询。<br>对于照片，如果该参数为空，默认查询'uri'、'media_type'、'subtype'和'display_name'，使用[get](#func-getstring)接口获取当前对象的其他属性时将会报错。示例：fetchColumns: ['uri', 'title']。<br>对于相册，如果该参数为空，默认查询'uri'和'album_name'。|
|predicates|[DataSharePredicates](../ArkData/cj-apis-data_share_predicates.md#class-datasharepredicates)|否|DataSharePredicates()| **命名参数。** 谓词查询，显示过滤条件。|