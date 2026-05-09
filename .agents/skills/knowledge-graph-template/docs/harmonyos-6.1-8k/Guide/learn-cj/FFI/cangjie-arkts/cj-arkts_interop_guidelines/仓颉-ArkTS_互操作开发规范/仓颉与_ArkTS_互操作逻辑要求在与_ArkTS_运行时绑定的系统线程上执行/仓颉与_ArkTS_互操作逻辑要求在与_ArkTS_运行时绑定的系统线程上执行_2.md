let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports => exports["addNumberAsync"] = runtime.function(addNumberAsync).toJSValue()
}
```