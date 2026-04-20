## class CallbackWithReturn\<A>

```cangjie
public abstract class CallbackWithReturn<A> <: CallbackObject {}
```

**功能：** 带返回值的回调函数抽象类。

**起始版本：** 22

**父类型：**

- [CallbackObject](#class-callbackobject)

### func invoke(?BusinessException)

```cangjie
public open func invoke(err: ?BusinessException): A
```

**功能：** 要求实现回调方法的抽象类约束。

**起始版本：** 22

**参数：**

| 参数  | 类型 | 必填 | 说明    |
|:----|:---|:---|:------|
| err | ?BusinessException  | 是 | 异常信息。 |

**返回值：**

|类型| 说明        |
|:----|:----------|
| A | 回调函数的返回值。|

## type Callback\<T>

```cangjie
public type Callback<T> = (arg: T) -> Unit
```

**功能：** 回调函数类型。