// 获取对象的id
    static func getDataId(context: JSContext, callInfo: JSCallInfo): JSValue {
        let thisArg = callInfo.thisArg
        let thisObject = thisArg.asObject()
        let jsExternal = thisObject.getAttachInfo().getOrThrow()
        let data = jsExternal.cast<Data>().getOrThrow()

        let result = context.number(Float64(data.id)).toJSValue()
        return result
    }
}
```

仓颉侧代码对应的 ArkTS 接口声明：

```javascript
export declare interface Data {
    setId(value: number): void;
    getId(): number;
}

export declare function createData(): Data;
```

ArkTS 侧代码：

```javascript
import { createData } from "libohos_app_cangjie_entry.so";

// 创建共享对象
let data = createData();
// 操作对象属性
data.setId(3);
let id = data.getId();

console.log("id is " + id);
```