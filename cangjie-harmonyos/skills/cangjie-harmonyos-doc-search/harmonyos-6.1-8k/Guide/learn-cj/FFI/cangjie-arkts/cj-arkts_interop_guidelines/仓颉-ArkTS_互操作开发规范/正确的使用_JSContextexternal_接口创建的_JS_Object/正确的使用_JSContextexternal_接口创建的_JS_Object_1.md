## 正确的使用 JSContext.external 接口创建的 JS Object

**【规则】** 正确的使用 JSContext.external 接口创建的 JS Object。

通过 JSContext.external 创建的 JSExternal 对象，在 ArkTS 侧类型为 undefined，不应直接作为接口参数使用。建议将 JSExternal 对象绑定到一个 JSObject 上，通过对象封装隐藏内部数据，提升接口的安全性与可维护性。

**错误示例：**

仓颉侧代码：

<!--compile.error-->
```cangjie
// 导入互操作库
import ohos.ark_interop.*

// 定义共享类，SharedObject为互操作库的类
class Data <: SharedObject {
    Data(
        // 定义2个属性
        var id: Int64,
        let name: String
    ) {}

    static init() {
        // 注册导出到ark的函数
        JSModule.registerFunc("createData", createData)
        JSModule.registerFunc("setDataId", setDataId)
        JSModule.registerFunc("getDataId", getDataId)
    }

    // 创建共享对象
    static func createData(context: JSContext, _: JSCallInfo): JSValue {
        // 创建仓颉对象
        let data = Data(1, "abc")
        // 创建js对仓颉对象的引用
        let jsExternal = context.external(data)
        // 返回js对仓颉对象的引用
        return jsExternal.toJSValue()
    }

    // 设置对象的id
    static func setDataId(context: JSContext, callInfo: JSCallInfo): JSValue {
        // 读取参数
        let arg0 = callInfo[0]
        let arg1 = callInfo[1]

        // 把参数0转换为js对仓颉对象的引用
        let jsExternal = arg0.asExternal()
        // 获取仓颉对象
        let data: Data = jsExternal.cast<Data>().getOrThrow()
        // 把参数1转换为Float64
        let value = arg1.toNumber()

        // 仓颉对象修改属性
        data.id = Int64(value)

        // 返回undefined
        let result = context.undefined().toJSValue()
        return result
    }

    // 获取对象的id
    static func getDataId(context: JSContext, callInfo: JSCallInfo): JSValue {
        let arg0 = callInfo[0]

        let jsExternal = arg0.asExternal()

        let data: Data = jsExternal.cast<Data>().getOrThrow()

        let result = context.number(Float64(data.id)).toJSValue()
        return result
    }
}
```

仓颉侧代码对应的 ArkTS 接口声明：

```javascript
export declare function createData(): undefined;
export declare function setDataId(data: undefined, value: number): void;
export declare function getDataId(data: undefined): number;
```

ArkTS 侧代码：

```javascript
import { createData, setDatId, getDataId } from "libohos_app_cangjie_entry.so";

// 创建共享对象
let data = createData();
// 操作对象属性
setDataId(data, 3);
let id = getDataId(data);

console.log("id is " + id);
```

**正确示例：**

仓颉侧代码：

<!--compile-->
```cangjie
// 导入互操作库
import ohos.ark_interop.*

// 定义共享类
class Data <: SharedObject {
    Data(
        // 定义2个属性
        var id: Int64,
        let name: String
    ) {}

    static init() {
        // 注册导出到ark的函数
        JSModule.registerFunc("createData", createData)
    }

    // 创建共享对象
    static func createData(context: JSContext, _: JSCallInfo): JSValue {
        let data = Data(1, "abc")
        let jsExternal = context.external(data)

        // 创建空JSObject
        let object = context.object()
        // 把js对仓颉对象的引用挂在JSObject的隐藏属性上
        object.attachCJObject(jsExternal)

        // 为js对象增加2个方法
        object["setId"] = context.function(setDataId).toJSValue()
        object["getId"] = context.function(getDataId).toJSValue()

        return object.toJSValue()
    }

    // 设置对象的id
    static func setDataId(context: JSContext, callInfo: JSCallInfo): JSValue {
        // 获取this指针
        let thisArg = callInfo.thisArg
        let arg0 = callInfo[0]

        // 把this指针转换为JSObject
        let thisObject = thisArg.asObject()
        // 从JSObject上获取隐藏属性
        let jsExternal = thisObject.getAttachInfo().getOrThrow()
        // 从js对仓颉对象的引用上获取仓颉对象
        let data = jsExternal.cast<Data>().getOrThrow()
        // 把参数0转换为Float64
        let value = arg0.toNumber()

        // 修改仓颉对象的属性
        data.id = Int64(value)

        let result = context.undefined()
        return result.toJSValue()
    }