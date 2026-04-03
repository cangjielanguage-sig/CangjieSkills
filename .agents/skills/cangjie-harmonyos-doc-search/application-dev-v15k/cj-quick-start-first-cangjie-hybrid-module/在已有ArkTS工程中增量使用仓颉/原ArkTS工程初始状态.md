## 原ArkTS工程初始状态

开发者可参照示例创建原始ArkTS工程，作为示例的原ArkTS应用工程目录结构如下所示：

```text
Project_name
├── .hvigor
├── .idea
├── AppScope
├── entry
├── hvigor
│    └── hvigor-config.json5
├── my_module
├── oh_modules
├── build-profile.json5
├── code-linter.json5
├── hvigorfile.ts
├── local.properties
├── oh-package.json5
└── oh-package-lock.json5
```

其中：

- **entry** 是通过 **Empty Ability** 工程模板创建的ArkTS模块，该模块会被编译为HAP包，可参照[创建HarmonyOS工程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-create-new-project#section11644183711342)创建。
- **my_module** 是通过 **Static Library** 工程模块创建的ArkTS静态库模块，该模块会被编译为HAR包，被**entry**模块依赖，可参照[创建库模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har#section643521083015)创建。

**entry**和**my_module**模块内各有一个页面，通过Navigation进行页面路由。

1. **entry**模块的目录结构如下所示：

   ```text
   entry
   ├── build
   ├── oh_modules
   ├── src
   │    ├── main
   │    │    ├── ets
   │    │    │    ├── entryability
   │    │    │    ├── entrybackupability
   │    │    │    └── pages
   │    │    │         └── Index.ets  
   │    │    ├── resources
   │    │    └── module.json5
   │    ├── mock
   │    ├── ohosTest
   │    └── test
   ├── build-profile.json5
   ├── hvigorfile.ts
   ├── obfuscation-rules.txt
   ├── oh-package.json5
   └── oh-package-lock.json5
   ```

    - **entry > src > main > ets > pages > Index.ets** 文件的示例如下：

   ```typescript
   // Index.ets
   @Entry
   @Component
   struct Index {
     pathStack: NavPathStack = new NavPathStack()
     @State message: string = 'Hello World';

     build() {
       Navigation(this.pathStack) {
         Column() {
           Button('路由到：MyModulePage')
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               this.pathStack.pushPathByName('MyModulePage', null)
             })
         }
         .width('100%')
         .height('100%')
       }
       .title("首页")
       .mode(NavigationMode.Stack)
     }
   }
   ```

    - 模块的**oh-package.json5**文件中，添加my_module作为依赖：

   ```json
   "dependencies": {
     "my_module": "file:../my_module"
   }
   ```

2. **my_module**模块的目录结构如下：

   ```text
   entry
   ├── build
   ├── src
   │    ├── main
   │    │    ├── ets
   │    │    │    └── pages
   │    │    │         └── MyModulePage.ets  
   │    │    ├── resources
   │    │    │    └── base
   │    │    │         ├── element
   │    │    │         └── profile
   │    │    │              └──router_map.json
   │    │    └── module.json5
   │    ├── ohosTest
   │    └── test
   ├── build-profile.json5
   ├── BuildProfile.ets
   ├── consumer-rules.txt
   ├── hvigorfile.ts
   ├── Index.ets
   ├── obfuscation-rules.txt
   └── oh-package.json5
   ```

    - **my_module > src > main > ets > pages > MyModulePage.ets**文件的示例如下：

   ```typescript
   // MyModulePage.ets

   @Builder
   export function MyModulePageBuilder() {
     MyModulePage()
   }

   @Component
   export struct MyModulePage {
     pathStack: NavPathStack = new NavPathStack()

     build() {
       NavDestination() {
         Column() {
           Button('回到首页')
             .type(ButtonType.Capsule)
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               this.pathStack.clear()
             })
         }
         .width('100%')
         .height('100%')
       }
       .title('MyModulePage')
       .onReady((context: NavDestinationContext) => {
         this.pathStack = context.pathStack
       })
     }
   }
   ```

    - **my_module > src > main > resources > base > profile > route_map.json**需要配置子页的路由信息，示例如下：

   ```json
   // route_map.json
   {
     "routerMap": [
       {
         "name": "MyModulePage",
         "pageSourceFile": "src/main/ets/pages/MyModulePage.ets",
         "buildFunction": "MyModulePageBuilder",
         "data": {
           "description": "this is MyModulePage"
         }
       }
     ]
   }
   ```

    - **my_module > src > main > module.json5**配置文件的module标签中定义routerMap字段，指向定义的本模块路由表配置文件route_map.json。示例如下：

   ```json5
   // module.json5
   "routerMap": "$profile:route_map"
   ```

   > **注意：**
   >
   >module标签中如果原有"pages": "$profile:main_pages"这行配置，则必须删除，否则上架后运行，路由跳转会出现异常导致白屏。