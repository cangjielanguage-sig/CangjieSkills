## class Callback1ArgumentWithReturn

```cangjie
public abstract class Callback1ArgumentWithReturn<A, B> <: CallbackObject {}
```

**功能：** 单参数且有返回值的回调函数抽象类。

**系统能力：** SystemCapability.Base

**起始版本：** 19

**父类型：**

- [CallbackObject](#class-callbackobject)

### func invoke(A)

```cangjie
public open func invoke(arg1: A): B
```

**功能：** 抽象类约束需要实现单参数回调方法。

**系统能力：** SystemCapability.Base

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1| A |是|-| 回调函数需要的参数。|

**返回值：**

|类型|说明|
|:----|:----|
| B | 回调函数的返回值。|

## class Callback2Argument

```cangjie
public abstract class Callback2Argument<A, B> <: CallbackObject {}
```

**功能：** 两个参数的回调函数抽象类。

**系统能力：** SystemCapability.Base

**起始版本：** 12

**父类型：**

- [CallbackObject](#class-callbackobject)

### func invoke(A, B)

```cangjie
public open func invoke(arg1: A, arg2: B): Unit
```

**功能：** 抽象类约束需要实现两个参数的回调方法。

**系统能力：** SystemCapability.Base

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1| A |是|-| 回调函数所需的第一个参数。|
|arg2| B |是|-| 回调函数所需的第二个参数。|

## class Callback3ArgumentWithReturn

```cangjie
public abstract class Callback3ArgumentWithReturn<A, B, C, D> <: CallbackObject {}
```

**功能：** 三个参数且有返回值的回调函数抽象类。

**系统能力：** SystemCapability.Base

**起始版本：** 19

**父类型：**

- [CallbackObject](#class-callbackobject)

### func invoke(A, B, C)

```cangjie
public open func invoke(arg1: A, arg2: B, arg3: C): D
```

**功能：** 抽象类约束需要实现三个参数的回调方法。

**系统能力：** SystemCapability.Base

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1| A |是|-|回调函数所需的第一个参数。|
|arg2| B |是|-|回调函数所需的第二个参数。|
|arg3| B |是|-|回调函数所需的第三个参数。|

**返回值：**

|类型|说明|
|:----|:----|
| D | 回调函数的返回值。|

## class CallbackObject

```cangjie
public abstract class CallbackObject {}
```

**功能：** 回调函数抽象基类。

**系统能力：** SystemCapability.Base

**起始版本：** 12

## class CallbackWithReturn

```cangjie
public abstract class CallbackWithReturn<A> <: CallbackObject {}
```

**功能：** 有返回值的回调函数抽象类。

**系统能力：** SystemCapability.Base

**起始版本：** 19

**父类型：**

- [CallbackObject](#class-callbackobject)

### func invoke()

```cangjie
public open func invoke(): A
```

**功能：** 抽象类约束需要实现回调方法。

**系统能力：** SystemCapability.Base

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
| A | 回调函数的返回值。|

## type AsyncCallback

```cangjie
public type AsyncCallback<T> = (Option<AsyncError>, Option<T>) -> Unit
```

**功能：** 定义的异步回调函数类型。

**系统能力：** SystemCapability.Base

**起始版本：** 12

## type Callback

```cangjie
public type Callback<T> = (T) -> Unit
```

**功能：** 回调函数类型。

**系统能力：** SystemCapability.Base

**起始版本：** 12