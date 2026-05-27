# 元能力仓颉封装（beta特性）

## 简介

元能力仓颉封装实现对Ability的运行及生命周期进行统一的调度和管理，应用进程能够支撑多个Ability，Ability具有跨应用进程间和同一进程内调用的能力。Ability管理服务统一调度和管理应用中各Ability，并对Ability的生命周期变更进行管理。当前开放的元能力仓颉接口仅支持standard设备。

## 系统架构

**图 1** 元能力仓颉架构图

![元能力仓颉架构图](figures/ability_cangjie_wrapper_architecture_zh.png)

如架构图所示：

接口层：

- UIAbility：面向开发者提供的UIAbility的API能力。UIAbility是包含UI界面的应用组件，提供UIAbility组件创建、销毁、前后台切换等生命周期回调的能力。开发者可通过继承此类来实现对UIAbility组件的监控能力。应用上下文提供了获取组件信息的能力。
- 应用上下文：面向开发者提供的应用上下文的API能力。应用上下文提供了Ability或Application的上下文的基础能力，包括访问特定应用程序的资源等。UIAbility组件的上下文提供了拉起其他UIAbility、销毁UIAbility的能力。开发者可通过UIAbilityContext获取相关信息或拉起其他UIAbility。
- 组件管理器：面向开发者提供的组件管理器的API能力。一个Module级别的组件管理器，用于进行Module级别的资源预加载、线程创建等初始化操作，以及维护Module下的应用状态。
- 错误观测管理：面向开发者提供的错误观测管理的API能力。提供了对错误观察器的注册和注销能力。当开发者需要注册或注销错误观察器时，可以使用其提供的接口。
- 自动化测试框架管理：面向开发者提供的自动化测试框架管理API能力。开发者可通过此模块来监视指定的Ability的生命周期状态更改和获取测试参数。

框架层：

- UIAbility封装：基于底层元能力运行时部件提供的元能力基础功能封装，提供用户可继承的UIAbility类。
- 应用上下文封装：基于底层元能力运行时部件提供的元能力基础功能封装，通过Context及其子类提供不同的上下文能力。
- 组件管理器封装：基于底层元能力运行时部件提供的元能力基础功能封装，通过AbilityStage类提供组件管理器能力。
- 错误观测管理封装：基于底层元能力运行时部件提供的元能力基础功能封装，通过ErrorManager类提供错误观测管理能力。
- 自动化测试框架管理封装：基于底层元能力运行时部件提供的元能力基础功能封装，通过AbilityDelegator类及TestRunner类提供自动化测试框架管理能力。

架构图中的依赖部件引入说明：

- 元能力运行时部件：元能力仓颉封装依赖元能力运行时部件提供的元能力基础功能。
- 访问控制部件：应用上下文依赖访问控制部件提供的鉴权能力。
- cangjie_ark_interop：负责提供仓颉注解类定义和BusinessException异常类定义。元能力仓颉封装依赖此部件用于对API进行标注，及在错误分支向用户抛出异常。
- arkui_cangjie_wrapper：负责提供仓颉UI组件接口及基础类型。应用上下文依赖其中的基础类型的定义和解析。
- hiviewdfx_cangjie_wrapper：负责提供日志接口。元能力仓颉封装依赖此部件用于在关键路径处打印日志。
- global_cangjie_wrapper：提供应用资源获取的能力。用户可通过应用上下文实例获取ResourceManager实例。
- bundlemanager_cangjie_wrapper：提供获取应用包信息的定义。用户可通过应用上下文获取ApplicationInfo和HapModuleInfo。
- communication_cangjie_wrapper：提供基础类型及数组、IPC对象、接口描述符和自定义序列化对象等用来通信的数据格式。应用上下文依赖其中的IRemoteObject进行通信。
- multimedia_cangjie_wrapper：提供使用媒体资源的能力。应用上下文依赖其中的PixelMap以设置任务图标。
- window_cangjie_wrapper：提供窗口实例管理能力。UIAbility依赖其中的WindowStage以加载UI组件。
- accesscontrol_cangjie_wrapper：提供应用程序的权限校验、申请和管理能力。元能力仓颉封装中定义的AbilityKit包含此模块。
- testfwk_cangjie_wrapper：提供单元测试框架以及UI测试框架。自动化测试框架管理封装依赖其中的UI测试框架。

## 目录

```
foundation/ability/ability_cangjie_wrapper                
├── figures                                 # 存放README中的架构图
├── kit                                     # 仓颉AbilityKit的kit化代码
│   └── AbilityKit
├── ohos                                    # 仓颉元能力接口实现   
│   ├── ability                             # 仓颉元能力依赖类型的定义 
│   ├── app
│   │   └── ability
│   │       ├── ability_delegator_registry  # 仓颉自动化测试框架管理封装
│   │       ├── ability_stage               # 仓颉组件管理器封装 
│   │       ├── error_manager               # 仓颉错误观测管理封装
│   │       └── ui_ability                  # 仓颉UIAbility及应用上下文封装
│   └── application
│       └── test_runner                     # 仓颉测试框架封装
└── test                                    # 仓颉测试代码
    ├── ability_delegator                   # 仓颉自动化测试框架管理接口测试用例
    ├── ability_delegator_registry          # 仓颉自动化测试框架管理接口测试用例
    ├── ability_stage                       # 仓颉组件管理器测试用例  
    ├── app_recovery                        # 仓颉应用恢复测试用例  
    ├── base_context                        # 仓颉应用上下文测试用例  
    ├── error_manager                       # 仓颉错误管理测试用例
    └── ui_ability_context                  # 仓颉UI能力上下文测试用例
```


## 使用说明

元能力仓颉接口提供了以下功能，开发者可以根据诉求使用：

  - UIAbility是包含UI界面的应用组件，提供UIAbility组件创建、销毁、前后台切换等生命周期回调的能力。
  - 应用上下文提供了获取组件信息、拉起其他UIAbility、销毁UIAbility的能力。
  - 组件管理器用于进行Module级别的资源预加载、线程创建等初始化操作。
  - 错误观测管理模块提供了对错误观察器的注册和注销能力。
  - 自动化测试框架使用指南模块可用于监视指定的Ability的生命周期状态更改和获取测试参数。
  - 框架测试模块可用于运行测试用例。


元能力相关API请参见[仓颉元能力API文档](https://gitcode.com/openharmony-sig/arkcompiler_cangjie_ark_interop/tree/master/doc/API_Reference/source_zh_cn/apis/AbilityKit)，相关指导请参见[程序框架服务开发指南](https://gitcode.com/openharmony-sig/arkcompiler_cangjie_ark_interop/blob/master/doc/Dev_Guide/source_zh_cn/application-models/cj-abilitykit-overview.md)。

## 约束

与ArkTS提供的API能力相比，暂不支持以下功能：

  - 支持特定场景拓展能力的ExtensionAbility。
  - 对接端侧意图框架的意图执行基类。
  - 应用启动框架AppStartup的相关能力。

## 参与贡献

欢迎广大开发者代码，文档等，具体的贡献流程和方式请参见[参与贡献](https://gitcode.com/openharmony/docs/blob/master/zh-cn/contribute/%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE.md)。

## 相关仓

[ability_ability_runtime](https://gitcode.com/openharmony/ability_ability_runtime)

[security_access_token](https://gitcode.com/openharmony/security_access_token)

[arkcompiler_cangjie_ark_interop](https://gitcode.com/openharmony-sig/arkcompiler_cangjie_ark_interop)

[arkui_arkui_cangjie_wrapper](https://gitcode.com/openharmony-sig/arkui_arkui_cangjie_wrapper)

[hiviewdfx_hiviewdfx_cangjie_wrapper](https://gitcode.com/openharmony-sig/hiviewdfx_hiviewdfx_cangjie_wrapper)

[accesscontrol_accesscontrol_cangjie_wrapper](https://gitcode.com/openharmony-sig/accesscontrol_accesscontrol_cangjie_wrapper)

[global_global_cangjie_wrapper](https://gitcode.com/openharmony-sig/global_global_cangjie_wrapper)

[bundlemanager_bundlemanager_cangjie_wrapper](https://gitcode.com/openharmony-sig/bundlemanager_bundlemanager_cangjie_wrapper)

[communication_communication_cangjie_wrapper](https://gitcode.com/openharmony-sig/communication_communication_cangjie_wrapper)

[multimedia_multimedia_cangjie_wrapper](https://gitcode.com/openharmony-sig/multimedia_multimedia_cangjie_wrapper)

[window_window_cangjie_wrapper](https://gitcode.com/openharmony-sig/window_window_cangjie_wrapper)

[testfwk_testfwk_cangjie_wrapper](https://gitcode.com/openharmony-sig/testfwk_testfwk_cangjie_wrapper)
