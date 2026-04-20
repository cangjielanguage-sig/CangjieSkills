### func equalTo(String, VBValueType)

```cangjie
public func equalTo(field: String, value: VBValueType): DataSharePredicates
```

**功能：** 该接口用于配置谓词以匹配值等于指定值的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。</br>当field为空字符串""时，调用接口配置的谓词无效。|
|value|[VBValueType](./cj-apis-values_bucket.md#enum-vbvaluetype)|是|-|指示要与谓词匹配的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataSharePredicates](#class-datasharepredicates)|返回与指定字段匹配的谓词。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14800000 | Internal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let predicates = DataSharePredicates()
    predicates.equalTo("NAME", VBValueType.StringValue("Rose"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func limit(Int32, Int32)

```cangjie
public func limit(total: Int32, offset: Int32): DataSharePredicates
```

**功能：** 该接口用于配置谓词以指定结果数和起始位置。目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|total|Int32|是|-|最大数据记录数。</br>当使用关系型数据库时，取值范围参考[关系型数据库limitAs接口](./cj-apis-relational_store.md#func-limitasint32)中的value参数说明。|
|offset|Int32|是|-|指定查询结果的起始位置。</br>当使用关系型数据库时，取值范围参考[关系型数据库offsetAs接口](./cj-apis-relational_store.md#func-offsetasint32)中的rowOffset参数说明。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataSharePredicates](#class-datasharepredicates)|返回与指定字段匹配的谓词。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14800000 | Internal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let predicates = DataSharePredicates()
    predicates.equalTo("NAME", VBValueType.StringValue("Rose")).limit(10, 3)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```