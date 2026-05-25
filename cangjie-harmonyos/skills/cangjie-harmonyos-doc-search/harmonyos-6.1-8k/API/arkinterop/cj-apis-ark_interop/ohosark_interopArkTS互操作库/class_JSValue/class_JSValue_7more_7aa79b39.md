## class JSValue

```cangjie
public class JSValue {}
```

**功能：** 一个ArkTS变量（弱类型，短生命周期）。

JSValue是ArkTS运行时统一类型，也是直接与ArkTS运行时交互的数据类型。

只有互操作接口可以创建JSValue，其生命周期在出栈（被创建时的栈）时结束，不能拷贝、捕获以及在非互操作函数返回。如果需要传递该变量，需要先转换，再以仓颉类型或是安全引用的形式传递。

**起始版本：** 22

### func asArray()

```cangjie
public func asArray(): JSArray
```

**功能：** 把一个 JSValue 转换为 JSArray。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSArray](#class-jsarray)|一个 ArkTS 数组的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asArrayBuffer()

```cangjie
public func asArrayBuffer(): JSArrayBuffer
```

**功能：** 把一个 JSValue 转换为 JSArrayBuffer。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|一个ArkTS ArrayBuffer的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asBigInt()

```cangjie
public func asBigInt(): JSBigInt
```

**功能：** 把一个 JSValue 转换为 JSBigInt。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSBigInt](#class-jsbigint)|ArkTS bigint的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asBoolean()

```cangjie
public func asBoolean(): JSBoolean
```

**功能：** 把一个 JSValue 转换为 JSBoolean。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSBoolean](#class-jsboolean)|一个 ArkTS boolean。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asClass()

```cangjie
public func asClass(): JSClass
```

**功能：** 把一个 JSValue 转换为 JSClass。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSClass](#class-jsclass)|一个ArkTS 类的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asExternal()

```cangjie
public func asExternal(): JSExternal
```

**功能：** 把一个 JSValue 转换为 JSExternal。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSExternal](#class-jsexternal)|一个 ArkTS 对仓颉对象引用的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |