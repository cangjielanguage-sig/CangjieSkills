### operator func \[](Int64, T)

```cangjie
public operator func [](index: Int64, value!: T): Unit
```

**功能：** 修改数组中下标 index 对应的值。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|需要修改的值的下标，取值范围为 [0..this.size]。|
|value|T|是|-| **命名参数。** 修改的目标值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 1     | The accessing index is out of range.  |
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func setIndexOperator(context: JSContext): JSValue {
    let array: Array<Int64> = [1, 2, 3, 4]
    let jsArrayEx = JSArrayEx<Int64>(array)

    // 设置索引为1的元素为100
    jsArrayEx[1] = 100
    Hilog.info(0, "test", "Set value at index 1 to 100")

    return jsArrayEx.toJSValue(context)
}
```