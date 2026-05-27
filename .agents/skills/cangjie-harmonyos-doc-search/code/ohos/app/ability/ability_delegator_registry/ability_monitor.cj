/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// The Cangjie API is in Beta. For details on its capabilities and limitations, please refer to the README file.

package ohos.app.ability.ability_delegator_registry

import ohos.ffi.{FFIData, FFIDataManager}
import ohos.app.ability.ui_ability.UIAbility
import ohos.labels.APILevel
import ohos.business_exception.BusinessException

func executeFunc(optFunc: ?(UIAbility) -> Unit, ability: UIAbility): Unit {
    match (optFunc) {
        case Some(actFunc) => actFunc(ability)
        case _ => return
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func monitorOnAbilityCreate(monitorId: Int64, abilityId: Int64): Unit {
    let optPara = (FFIDataManager.getInstance().getData<AbilityMonitor>(monitorId),
        FFIDataManager.getInstance().getData<UIAbility>(abilityId))
    match (optPara) {
        case (None, _) | (_, None) => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case (Some(monitor), Some(ability)) => executeFunc(monitor.onAbilityCreate, ability)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func monitorOnAbilityForeground(monitorId: Int64, abilityId: Int64): Unit {
    let optPara = (FFIDataManager.getInstance().getData<AbilityMonitor>(monitorId),
        FFIDataManager.getInstance().getData<UIAbility>(abilityId))
    match (optPara) {
        case (None, _) | (_, None) => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case (Some(monitor), Some(ability)) => executeFunc(monitor.onAbilityForeground, ability)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func monitorOnAbilityBackground(monitorId: Int64, abilityId: Int64): Unit {
    let optPara = (FFIDataManager.getInstance().getData<AbilityMonitor>(monitorId),
        FFIDataManager.getInstance().getData<UIAbility>(abilityId))
    match (optPara) {
        case (None, _) | (_, None) => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case (Some(monitor), Some(ability)) => executeFunc(monitor.onAbilityBackground, ability)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func monitorOnAbilityDestroy(monitorId: Int64, abilityId: Int64): Unit {
    let optPara = (FFIDataManager.getInstance().getData<AbilityMonitor>(monitorId),
        FFIDataManager.getInstance().getData<UIAbility>(abilityId))
    match (optPara) {
        case (None, _) | (_, None) => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case (Some(monitor), Some(ability)) => executeFunc(monitor.onAbilityDestroy, ability)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func monitorOnWindowStageCreate(monitorId: Int64, abilityId: Int64): Unit {
    let optPara = (FFIDataManager.getInstance().getData<AbilityMonitor>(monitorId),
        FFIDataManager.getInstance().getData<UIAbility>(abilityId))
    match (optPara) {
        case (None, _) | (_, None) => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case (Some(monitor), Some(ability)) => executeFunc(monitor.onWindowStageCreate, ability)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func monitorOnWindowStageRestore(monitorId: Int64, abilityId: Int64): Unit {
    let optPara = (FFIDataManager.getInstance().getData<AbilityMonitor>(monitorId),
        FFIDataManager.getInstance().getData<UIAbility>(abilityId))
    match (optPara) {
        case (None, _) | (_, None) => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case (Some(monitor), Some(ability)) => executeFunc(monitor.onWindowStageRestore, ability)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func monitorOnWindowStageDestroy(monitorId: Int64, abilityId: Int64): Unit {
    let optPara = (FFIDataManager.getInstance().getData<AbilityMonitor>(monitorId),
        FFIDataManager.getInstance().getData<UIAbility>(abilityId))
    match (optPara) {
        case (None, _) | (_, None) => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case (Some(monitor), Some(ability)) => executeFunc(monitor.onWindowStageDestroy, ability)
    }
}

/**
 * Provide methods for matching monitored Ability objects that meet specified conditions.
 * The most recently matched Ability objects will be saved in the AbilityMonitor object.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class AbilityMonitor <: FFIData {
    /**
     * The name of the ability to monitor.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var abilityName: String
    /**
     * The name of the module to monitor.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var moduleName: String
    /**
     * Called back when the ability is created for initialization.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onAbilityCreate: ?(UIAbility) -> Unit
    /**
     * Called back when the state of the ability changes to foreground.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onAbilityForeground: ?(UIAbility) -> Unit
    /**
     * Called back when the state of the ability changes to background.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onAbilityBackground: ?(UIAbility) -> Unit
    /**
     * Called back before the ability is destroyed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onAbilityDestroy: ?(UIAbility) -> Unit
    /**
     * Called back when an ability window stage is created.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onWindowStageCreate: ?(UIAbility) -> Unit
    /**
     * Called back when an ability window stage is restored.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onWindowStageRestore: ?(UIAbility) -> Unit
    /**
     * Called back when an ability window stage is destroyed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onWindowStageDestroy: ?(UIAbility) -> Unit

    /**
     * AbilityMonitor constructor.
     *
     * @param { String } abilityName - The name of the ability to monitor.
     * @param { String } [moduleName] - The name of the module to monitor. The default value is "".
     * @param { ?(UIAbility) -> Unit } [onAbilityCreate] - Called back when the ability is created for initialization.
     * The default value is None.
     * @param { ?(UIAbility) -> Unit } [onAbilityForeground] - Called back when the state of the ability changes to
     * foreground. The default value is None.
     * @param { ?(UIAbility) -> Unit } [onAbilityBackground] - Called back when the state of the ability changes to
     * background. The default value is None.
     * @param { ?(UIAbility) -> Unit } [onAbilityDestroy] - Called back before the ability is destroyed. The default
     * value is None.
     * @param { ?(UIAbility) -> Unit } [onWindowStageCreate] - Called back when an ability window stage is created. The
     * default value is None.
     * @param { ?(UIAbility) -> Unit } [onWindowStageRestore] - Called back when an ability window stage is restored. The
     * default value is None.
     * @param { ?(UIAbility) -> Unit } [onWindowStageDestroy] - Called back when an ability window stage is destroyed.
     * The default value is None.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public init(
        abilityName: String,
        moduleName!: String = "",
        onAbilityCreate!: ?(UIAbility) -> Unit = None,
        onAbilityForeground!: ?(UIAbility) -> Unit = None,
        onAbilityBackground!: ?(UIAbility) -> Unit = None,
        onAbilityDestroy!: ?(UIAbility) -> Unit = None,
        onWindowStageCreate!: ?(UIAbility) -> Unit = None,
        onWindowStageRestore!: ?(UIAbility) -> Unit = None,
        onWindowStageDestroy!: ?(UIAbility) -> Unit = None
    ) {
        registerSelf()
        this.abilityName = abilityName
        this.moduleName = moduleName
        this.onAbilityCreate = onAbilityCreate
        this.onAbilityForeground = onAbilityForeground
        this.onAbilityBackground = onAbilityBackground
        this.onAbilityDestroy = onAbilityDestroy
        this.onWindowStageCreate = onWindowStageCreate
        this.onWindowStageRestore = onWindowStageRestore
        this.onWindowStageDestroy = onWindowStageDestroy
    }

    ~init() {
        FFIDataManager.getInstance().releaseData(id_)
    }
}

@C
struct CJMonitorFuncs {
    CJMonitorFuncs(
        let onAbilityCreate: CFunc<(Int64, Int64) -> Unit>,
        let onAbilityForeground: CFunc<(Int64, Int64) -> Unit>,
        let onAbilityBackground: CFunc<(Int64, Int64) -> Unit>,
        let onAbilityDestroy: CFunc<(Int64, Int64) -> Unit>,
        let onWindowStageCreate: CFunc<(Int64, Int64) -> Unit>,
        let onWindowStageRestore: CFunc<(Int64, Int64) -> Unit>,
        let onWindowStageDestroy: CFunc<(Int64, Int64) -> Unit>
    ) {}
}

@C
func monitorCjFuncsRegister(result: CPointer<CJMonitorFuncs>): Unit {
    let atCFuncs = CJMonitorFuncs(
        monitorOnAbilityCreate,
        monitorOnAbilityForeground,
        monitorOnAbilityBackground,
        monitorOnAbilityDestroy,
        monitorOnWindowStageCreate,
        monitorOnWindowStageRestore,
        monitorOnWindowStageDestroy
    )
    unsafe { result.write(atCFuncs) }
}

foreign func RegisterCJMonitorFuncs(funcs: CFunc<(CPointer<CJMonitorFuncs>) -> Unit>): Unit

let REGISTER_MONITOR = unsafe { RegisterCJMonitorFuncs(monitorCjFuncsRegister) }
