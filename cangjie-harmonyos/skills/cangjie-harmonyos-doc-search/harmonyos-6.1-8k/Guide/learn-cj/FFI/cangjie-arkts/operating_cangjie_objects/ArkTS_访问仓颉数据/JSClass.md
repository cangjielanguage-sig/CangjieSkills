## JSClass

把所有的对象操作方法直接挂在对象上，一方面占用内存比较大，另一方面创建对象的开销比较大。对于追求性能的场景，可以定义一个 JSClass 来加速对象创建和减小内存占用。示例如下：

1. 定义仓颉函数：

    <!--compile-->
    ```cangjie
    // 导入互操作库
    import ohos.ark_interop.*
    import ohos.ark_interop_macro.*
    // 定义共享类
    class Data <: SharedObject {
        Data(
            // 定义2个属性
            var id: Int64,
            let name: String
        ) {}

        static init() {
            // 注册导出到ark的类
            JSModule.registerClass("Data") { context =>
                // 创建JSClass
                let clazz = context.clazz(jsConstructor)
                // 增加方法
                clazz.addMethod(context.string("setId"), context.function(setDataId))
                clazz.addMethod(context.string("getId"), context.function(getDataId))

                return clazz
            }
        }

        // js构造函数
        static func jsConstructor(context: JSContext, callInfo: JSCallInfo): JSValue {
            // 获取this指针
            let thisArg = callInfo.thisArg
            // 转换为JSObject
            let thisObject = thisArg.asObject()
            // 创建创建对象
            let data = Data(1, "abc")
            // 创建js对仓颉对象的引用
            let jsExternal = context.external(data)
            // 设置JSObject属性
            thisObject.attachCJObject(jsExternal)
            return thisObject.toJSValue()
        }

        // 设置对象的id
        static func setDataId(context: JSContext, callInfo: JSCallInfo): JSValue {
            // 获取this指针
            let thisArg = callInfo.thisArg
            // 把this指针转换为JSObject
            let thisObject = thisArg.asObject()
            // 从JSObject上获取隐藏属性
            let jsExternal = thisObject.getAttachInfo().getOrThrow()
            // 从js对仓颉对象的引用上获取仓颉对象
            let data = jsExternal.cast<Data>().getOrThrow()

            let arg0 = callInfo[0]
            // 把参数0转换为Float64
            let value = arg0.toNumber()

            // 修改仓颉对象的属性
            data.id = Int64(value)

            let result = context.undefined()
            return result.toJSValue()
        }

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

2. 在 Index.d.ts 文件中，提供互操作的接口声明：

    ```typescript
    // libohos_app_cangjie_entry.so对应的Index.d.ts
    export declare class Data {
        setId(value: number): void;
        getId(): number;
        constructor();
    }
    ```

3. ArkTS 调用仓颉函数：

    ```typescript
    // 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
    import cjLib from "libohos_app_cangjie_entry.so";

    // 创建共享对象
    let data = new cjLib.Data();
    // 操作对象属性
    data.setId(3);
    let id = data.getId();

    console.log("id is " + id);
    ```