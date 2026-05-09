### func orderByAsc(String)

```cangjie
public func orderByAsc(field: String): DataSharePredicates
```

**功能：** 该接口用于配置谓词以匹配其值按升序排序的列。目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。 </br>当field为空字符串""时，调用接口配置的谓词无效。|

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
    predicates.orderByAsc("AGE")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func orderByDesc(String)

```cangjie
public func orderByDesc(field: String): DataSharePredicates
```

**功能：** 该接口用于配置谓词以匹配其值按降序排序的列。目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。</br>当field为空字符串""时，调用接口配置的谓词无效。|

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
    predicates.orderByDesc("AGE")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```