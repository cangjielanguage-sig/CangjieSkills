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

package ohos.app.ability.ability_stage

import std.collection.HashMap
import ohos.ffi.{FFIData, FFIDataManager}
import ohos.labels.{APILevel, Hide}
import ohos.app.ability.configuration.{CJConfiguration, CConfiguration}
import ohos.app.ability.want.WantHandle
import ohos.app.ability.ui_ability.AbilityStageContext
import ohos.business_exception.BusinessException

const ERROR_CODE_INNER: Int32 = 16000050

type AbilityStageHandle = UIntNative

foreign func RegisterCJAbilityStageFuncs(registerFunc: CFunc<(CPointer<CJAbilityStageFuncs>) -> Unit>): Unit

foreign func FFIAbilityGetAbilityStageContext(handle: AbilityStageHandle): Int64

const ERR_INVALID_INSTANCE_CODE: Int64 = -1;

@C
struct CJAbilityStageFuncs {
    CJAbilityStageFuncs(
        let loadAbilityStage: CFunc<(CString) -> Int64>,
        let releaseAbilityStage: CFunc<(Int64) -> Unit>,
        let abilityStageOnCreate: CFunc<(Int64) -> Unit>,
        let abilityStageOnAcceptWant: CFunc<(Int64, WantHandle) -> CString>,
        let abilityStageOnConfigurationUpdated: CFunc<(Int64, CJConfiguration) -> Unit>,
        let abilityStageOnMemoryLevel: CFunc<(Int64, Int32) -> Unit>,
        let abilityStageInit: CFunc<(Int64, AbilityStageHandle) -> Unit>,
        let abilityStageOnConfigurationUpdated2: CFunc<(Int64, CConfiguration) -> Unit>,
        let abilityStageOnDestroy: CFunc<(Int64) -> Unit>,
        let abilityStageOnNewProcessRequest: CFunc<(Int64, WantHandle) -> CString>
    ) {}
}

@C
func abilityStageInit(id: Int64, abilityStageHandle: AbilityStageHandle): Unit {
    let optStage = FFIDataManager.getInstance().getData<AbilityStage>(id)
    if (let Some(stage) <- optStage) {
        stage.abilityStageInit(abilityStageHandle)
    }
}

@C
func loadAbilityStage(moduleName: CString): Int64 {
    let optStage = AbilityStage.create(moduleName.toString())
    match (optStage) {
        case None =>
            ABILITY_LOG.error("Failed to load AbilityStage: " + moduleName.toString())
            0
        case Some(stage) =>
            FFIDataManager.getInstance().register(stage)
            stage.getID()
    }
}

@C
func releaseAbilityStage(id: Int64): Unit {
    FFIDataManager.getInstance().releaseData(id)
}

@C
func abilityStageOnCreate(id: Int64): Unit {
    let optStage = FFIDataManager.getInstance().getData<AbilityStage>(id)
    if (let Some(stage) <- optStage) {
        stage.onCreate()
    }
}

@C
func abilityStageOnDestroy(_: Int64): Unit {}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityStageOnAcceptWant(id: Int64, _: WantHandle): CString {
    let optStage = FFIDataManager.getInstance().getData<AbilityStage>(id)
    if (let Some(stage) <- optStage) {
        let result = ""
        unsafe { LibC.mallocCString(result) }
    } else {
        throw BusinessException(ERROR_CODE_INNER, "Internal error.")
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityStageOnNewProcessRequest(id: Int64, _: WantHandle): CString {
    let optStage = FFIDataManager.getInstance().getData<AbilityStage>(id)
    if (let Some(stage) <- optStage) {
        let result = ""
        unsafe { LibC.mallocCString(result) }
    } else {
        throw BusinessException(ERROR_CODE_INNER, "Internal error.")
    }
}

@C
func abilityStageOnConfigurationUpdated(_: Int64, _: CJConfiguration): Unit {
    ()
}

@C
func abilityStageOnConfigurationUpdated2(_: Int64, _: CConfiguration): Unit {}

@C
func abilityStageOnMemoryLevel(_: Int64, _: Int32): Unit {}

class AbilityStageImpl {}

/**
 * AbilityStage is a runtime class for HAP files.
 * AbilityStage notifies you of when you can perform HAP initialization such as resource pre-loading and thread
 * creation during the HAP loading.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public open class AbilityStage <: FFIData {
    // Store methods of creating AbilityStage in different module.
    private static let CREATORS = HashMap<String, () -> AbilityStage>()
    private var abilityStageContext: Option<AbilityStageContext> = Option<AbilityStageContext>.None
    private let impl_: AbilityStageImpl = AbilityStageImpl()
    @!Hide
    protected init() {}
    /**
     * register AbilityStage
     *
     * @param { String } moduleName - Indicates the module name of the AbilityStage.
     * @param { () -> AbilityStage } creator - Indicates the creator of the AbilityStage.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    @!Hide
    public static func registerCreator(moduleName: String, creator: () -> AbilityStage): Unit {
        let optCreator = CREATORS.get(moduleName)
        match (optCreator) {
            case None =>
                CREATORS.add(moduleName, creator)
                ABILITY_LOG.info("Register AbilityStage creator successfully in " + moduleName)
            case Some(creatorFunc) => ABILITY_LOG.error(
                "Repeated registration for AbilityStage in " + moduleName + ", please check.")
        }
    }

    // protected function: available only for this package.
    static func create(moduleName: String): Option<AbilityStage> {
        let optCreator = CREATORS.get(moduleName)
        match (optCreator) {
            case None =>
                ABILITY_LOG.error("No such create functions for AbilityStageCreator: " + moduleName)
                Option<AbilityStage>.None
            case Some(creator) => creator()
        }
    }

    /**
     * Defines the context of AbilityStage.
     * The context is obtained in the callback invoked when initialization is performed during ability startup.
     *
     * @returns { AbilityStageContext } Returns the context of AbilityStageContext.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public mut prop context: AbilityStageContext {
        get() {
            match (abilityStageContext) {
                case None => throw BusinessException(ERROR_CODE_INNER, "Invalid context")
                case Some(value) => return value
            }
        }
        set(value) {
            abilityStageContext = value
        }
    }

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    func abilityStageInit(remote: AbilityStageHandle): Unit {
        if (remote == 0) {
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }

        // Init abilityContext
        let nativeAbilityStageContextId = unsafe { FFIAbilityGetAbilityStageContext(remote) }
        if (nativeAbilityStageContextId == ERR_INVALID_INSTANCE_CODE) {
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
        var value = AbilityStageContext(nativeAbilityStageContextId)
        abilityStageContext = Option<AbilityStageContext>.Some(value)
    }

    /**
     * Called when the application is created.
     * 
     * This API returns the result synchronously and does not support asynchronous callbacks.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public open func onCreate(): Unit {}
}

@C
func abilityStageCjFuncsRegister(result: CPointer<CJAbilityStageFuncs>): Unit {
    let funcs = CJAbilityStageFuncs(
        loadAbilityStage,
        releaseAbilityStage,
        abilityStageOnCreate,
        abilityStageOnAcceptWant,
        abilityStageOnConfigurationUpdated,
        abilityStageOnMemoryLevel,
        abilityStageInit,
        abilityStageOnConfigurationUpdated2,
        abilityStageOnDestroy,
        abilityStageOnNewProcessRequest
    )
    unsafe { result.write(funcs) }
}

let REGISTER_ABILITY_STAGE = unsafe { RegisterCJAbilityStageFuncs(abilityStageCjFuncsRegister) }
