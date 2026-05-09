## class DataSharePredicates

```cangjie
public class DataSharePredicates {
    public init()
}
```

**功能：** 提供用于不同实现不同查询方法的数据共享谓词。

> **说明：**
>
> 该类不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 22

### init()

```cangjie
public init()
```

**功能：** DataSharePredicates的初始化构造函数。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 22

### func inValues(String, Array\<VBValueType>)

```cangjie
public func inValues(field: String, value: Array<VBValueType>): DataSharePredicates
```

**功能：** 该接口用于配置谓词以匹配值在指定范围内的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。</br>当field为空字符串""时，调用接口配置的谓词无效。|
|value|Array\<[VBValueType](cj-apis-values_bucket.md#enum-vbvaluetype)>|是|-|以VBValueType数组形式指定的要匹配的值。|

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
    predicates.inValues("AGE", [VBValueType.Integer(18), VBValueType.Integer(20)])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func and()

```cangjie
public func and(): DataSharePredicates
```

**功能：** 该接口用于将和条件添加到谓词中。目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 22

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
    predicates.equalTo("NAME", VBValueType.StringValue("lisi"))
            .and()
            .equalTo("SALARY", VBValueType.Double(200.5))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```