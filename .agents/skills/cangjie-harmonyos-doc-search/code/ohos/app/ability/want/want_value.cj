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

package ohos.app.ability.want

import std.collection.HashMap
import ohos.encoding.json.{JsonValue, JsonKind, JsonObject, JsonInt, JsonArray, JsonFloat, JsonString, JsonBool}
import ohos.labels.APILevel
import ohos.business_exception.BusinessException

const ERROR_CODE_INNER: Int32 = 16000050

/**
 * Want value type.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityBase"
]
public enum WantValueType {
    /**
     * Int64 value type.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    Int64Value(Int64)
    |
    /**
     * Float64 value type.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    Float64Value(Float64)
    |
    /**
     * String value type.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    StringValue(String)
    |
    /**
     * Bool value type.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    BoolValue(Bool)
    |
    /**
     * Array value type.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    ArrayValue(Array<WantValueType>)
    |
    /**
     * HashMap value type.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    HashMapValue(HashMap<String, WantValueType>)
    | ...

    protected func toJsonValue(): JsonValue {
        match (this) {
            case Int64Value(n) => JsonInt(n)
            case Float64Value(n) => JsonFloat(n)
            case StringValue(n) => JsonString(n)
            case BoolValue(n) => JsonBool(n)
            case ArrayValue(n) => arrayToJsonArray(n)
            case HashMapValue(n) => mapToJsonObject(n)
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }

    protected static func fromJsonValue(jsValue: JsonValue): WantValueType {
        return match (jsValue.kind()) {
            case JsonKind.JsInt => Int64Value(jsValue.asInt().getValue())
            case JsonKind.JsFloat => Float64Value(jsValue.asFloat().getValue())
            case JsonKind.JsString => StringValue(jsValue.asString().getValue())
            case JsonKind.JsBool => BoolValue(jsValue.asBool().getValue())
            case JsonKind.JsArray => ArrayValue(arrayFromJsonArray(jsValue.asArray()))
            case JsonKind.JsObject => HashMapValue(mapFromJsonObject(jsValue.asObject()))
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

func arrayToJsonArray(array: Array<WantValueType>): JsonArray {
    let jsonArray = Array<JsonValue>(array.size) {
        i => array[i].toJsonValue()
    }
    return JsonArray(jsonArray)
}

func arrayFromJsonArray(jsArray: JsonArray): Array<WantValueType> {
    return Array<WantValueType>(jsArray.size()) {
        i => WantValueType.fromJsonValue(jsArray[i])
    }
}

protected func mapToJsonObject(map: HashMap<String, WantValueType>): JsonObject {
    let paramMap = HashMap<String, JsonValue>()
    for ((k, v) in map) {
        paramMap.add(k, v.toJsonValue())
    }
    return JsonObject(paramMap)
}

protected func mapFromJsonObject(jsObj: JsonObject): HashMap<String, WantValueType> {
    let paramMap = HashMap<String, WantValueType>()
    for ((k, v) in jsObj.getFields()) {
        paramMap.add(k, WantValueType.fromJsonValue(v))
    }
    return paramMap
}
