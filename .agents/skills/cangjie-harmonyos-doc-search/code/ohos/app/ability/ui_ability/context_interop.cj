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

package ohos.app.ability.ui_ability

import ohos.ark_interop.{JSContext, JSValue, napi_env, napi_value}
import ohos.ark_interop_helper.{arktsValuetoNapiValue, napiValueToArkTsValue}

import ohos.labels.APILevel

foreign {
    func FfiConvertBaseContext2Napi(env: napi_env, id: Int64): napi_value

    func FfiCreateBaseContextFromNapi(env: napi_env, object: napi_value): Int64

    func FfiConvertUIAbilityContext2Napi(env: napi_env, id: Int64): napi_value

    func FfiCreateUIAbilityContextFromNapi(env: napi_env, object: napi_value): Int64

    func FfiConvertAbilityStageContext2Napi(env: napi_env, id: Int64): napi_value

    func FfiCreateAbilityStageContextFromNapi(env: napi_env, object: napi_value): Int64

    func FfiConvertApplicationContext2Napi(env: napi_env, id: Int64): napi_value

    func FfiCreateApplicationContextFromNapi(env: napi_env, object: napi_value): Int64
}

/**
 * extend Context for cangjie object to arkts object
 */
extend Context <: SystemObjectInteropTypeToJS {
    /**
     * Convert Cangjie object to ArkTs object.
     *
     * @param { JSContext } context - The JSRuntime context.
     * @returns { JSValue } Returns the JSValue converted from the Cangjie object.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public func toJSValue(context: JSContext): JSValue {
        let napiValue = unsafe {
            match (this) {
                case _: UIAbilityContext => FfiConvertUIAbilityContext2Napi(context.getNapiEnv(), getID())
                case _: AbilityStageContext => FfiConvertAbilityStageContext2Napi(context.getNapiEnv(), getID())
                case _: ApplicationContext => FfiConvertApplicationContext2Napi(context.getNapiEnv(), getID())
                case _: Context => FfiConvertBaseContext2Napi(context.getNapiEnv(), getID())
            }
        }
        return JSValue(context, napiValueToArkTsValue(napiValue))
    }
}

/**
 * Create Cangjie object from ArkTs object.
 *
 * @param { JSContext } context - The JSRuntime context.
 * @param { JSValue } input - The JSValue to be converted.
 * @returns { UIAbilityContext } Returns the UIAbilityContext converted from the JSValue.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public func createUIAbilityContextFromJSValue(context: JSContext, input: JSValue): UIAbilityContext {
    let env = context.getNapiEnv()
    let napiValue = arktsValuetoNapiValue(env, input)
    let remoteId = unsafe { FfiCreateUIAbilityContextFromNapi(env, napiValue) }
    return UIAbilityContext(remoteId)
}

/**
 * Create Cangjie object from ArkTs object.
 *
 * @param { JSContext } context - The JSRuntime context.
 * @param { JSValue } input - The JSValue to be converted.
 * @returns { AbilityStageContext } Returns the AbilityStageContext converted from the JSValue.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public func createAbilityStageContextFromJSValue(context: JSContext, input: JSValue): AbilityStageContext {
    let env = context.getNapiEnv()
    let napiValue = arktsValuetoNapiValue(env, input)
    let remoteId = unsafe { FfiCreateAbilityStageContextFromNapi(env, napiValue) }
    return AbilityStageContext(remoteId)
}

/**
 * Create Cangjie object from ArkTs object.
 *
 * @param { JSContext } context - The JSRuntime context.
 * @param { JSValue } input - The JSValue to be converted.
 * @returns { ApplicationContext } Returns the ApplicationContext converted from the JSValue.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public func createApplicationContextFromJSValue(context: JSContext, input: JSValue): ApplicationContext {
    let env = context.getNapiEnv()
    let napiValue = arktsValuetoNapiValue(env, input)
    let remoteId = unsafe { FfiCreateApplicationContextFromNapi(env, napiValue) }
    return ApplicationContext(remoteId)
}

/**
 * Create Cangjie object from ArkTs object.
 *
 * @param { JSContext } context - The JSRuntime context.
 * @param { JSValue } input - The JSValue to be converted.
 * @returns { Context } Returns the Context converted from the JSValue.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public func createContextFromJSValue(context: JSContext, input: JSValue): Context {
    let env = context.getNapiEnv()
    let napiValue = arktsValuetoNapiValue(env, input)
    let remoteId = unsafe { FfiCreateBaseContextFromNapi(env, napiValue) }
    return Context(remoteId)
}
