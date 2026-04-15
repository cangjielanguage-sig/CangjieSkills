### operator func !=(JSStringEx)

```cangjie
public operator func !=(str: JSStringEx): Bool
```

**功能：** 判断两个 JSStringEx 是否不相等。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|str|[JSStringEx](#class-jsstringex)|是|-|待比较的字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|不相等返回 true，相等返回 false。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### operator func ==(JSStringEx)

```cangjie
public operator func ==(str: JSStringEx): Bool
```

**功能：** 功能：判断两个 JSStringEx 是否相等。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|str|[JSStringEx](#class-jsstringex)|是|-|待比较的字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|相等返回 true，不相等返回 false。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |