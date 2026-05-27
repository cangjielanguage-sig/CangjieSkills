## type ClassRegister

```cangjie
public type ClassRegister = (JSContext) -> JSClass
```

**功能：** ClassRegister 是 ([JSContext](#class-jscontext)) -> [JSClass](#class-jsclass) 类型的别名。

## type FuncRegister

```cangjie
public type FuncRegister = (JSContext) -> JSFunction
```

**功能：** FuncRegister 是 ([JSContext](#class-jscontext)) -> [JSFunction](#class-jsfunction) 类型的别名。

## type JSBufferFinalizer

```cangjie
public type JSBufferFinalizer = (CPointer<Byte>) -> Unit
```

**功能：** JSBufferFinalizer 是 (CPointer\<Byte>) -> Unit 类型的别名。

## type JSLambda

```cangjie
public type JSLambda = (JSContext, JSCallInfo) -> JSValue
```

**功能：** JSLambda 是 ([JSContext](#class-jscontext), [JSCallInfo](#struct-jscallinfo)) -> [JSValue](#struct-jsvalue) 类型的别名。

## type ModuleRegister

```cangjie
public type ModuleRegister = (JSContext, JSObject) -> Unit
```

**功能：** ModuleRegister 是 ([JSContext](#class-jscontext), [JSObject](#class-jsobject)) -> Unit 类型的别名。

## type napi_env

```cangjie
public type napi_env = CPointer<Unit>
```

**功能：** napi_env 是 CPointer\<Unit> 类型的别名。

## type napi_value

```cangjie
public type napi_value = CPointer<Unit>
```

**功能：** napi_value 是 CPointer\<Unit> 类型的别名。