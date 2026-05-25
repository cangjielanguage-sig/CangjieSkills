## type VoidCallback

```cangjie
public type VoidCallback = () -> Unit
```

**功能：** [VoidCallback](#type-voidcallback)是[() -> Unit](#type-voidcallback)类型的别名。

**类型：** () -> Unit

## type Callback\<T, V>

```cangjie
public type Callback<T, V> = (T) -> V
```

**功能：** Callback\<T, V>是(T) -> V类型的别名。

**类型：** (T) -> V

## type CustomBuilder

```cangjie
public type CustomBuilder = () -> Unit
```

**功能：** CustomBuilder是() -> Unit类型的别名。

**类型：** () -> Unit

## type TransitionFinishCallback

```cangjie
public type TransitionFinishCallback = (Bool) -> Unit
```

**功能：** [TransitionFinishCallback](#type-transitionfinishcallback)是(Bool) -> Unit类型的别名。

**类型：** (Bool) -> Unit

## type ItemGeneratorFunc\<T>

```cangjie
public type ItemGeneratorFunc<T> = (T, Int64) -> Unit
```

**功能：** 定义Item生成器函数。

**类型：** (T, Int64) -> Unit

## type KeyGeneratorFunc\<T>

```cangjie
public type KeyGeneratorFunc<T> = (T, Int64) -> String
```

**功能：** 定义键生成器函数。

**类型：** (T, Int64) -> String