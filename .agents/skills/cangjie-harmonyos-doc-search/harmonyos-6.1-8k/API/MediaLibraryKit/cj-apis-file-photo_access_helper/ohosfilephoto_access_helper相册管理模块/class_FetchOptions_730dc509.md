## class FetchOptions

```cangjie
public class FetchOptions {
    public var fetchColumns: Array<String>
    public var predicates: DataSharePredicates
    public init(fetchColumns: Array<String>, predicates: DataSharePredicates)
}
```

**功能：** 检索条件。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var fetchColumns

```cangjie
public var fetchColumns: Array<String>
```

**功能：** 检索条件，指定列名查询。

对于照片，如果该参数为空，默认查询'uri'、'media_type'、'subtype'和'display_name'，使用[get](#func-getstring)接口获取当前对象的其他属性时将会报错。示例：fetchColumns: ['uri', 'title']。

对于相册，如果该参数为空，默认查询'uri'和'album_name'。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var predicates

```cangjie
public var predicates: DataSharePredicates
```

**功能：** 谓词查询，指定过滤条件。

**类型：** [DataSharePredicates](../ArkData/cj-apis-data_share_predicates.md#class-datasharepredicates)

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### init(Array\<String>, DataSharePredicates)

```cangjie
public init(fetchColumns: Array<String>, predicates: DataSharePredicates)
```

**功能：** 构造FetchOptions对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fetchColumns|Array\<String>|是|-| 检索条件，指定列名查询。|
|predicates|[DataSharePredicates](../ArkData/cj-apis-data_share_predicates.md#class-datasharepredicates)|是|-| 谓词查询，指定过滤条件。|