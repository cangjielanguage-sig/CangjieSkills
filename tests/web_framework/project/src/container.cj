package web

import std.collection.*

// Service lifetime for IoC container
public enum ServiceLifetime {
    Singleton | Transient
}

// IoC dependency injection container
public class ServiceContainer {
    private let _factories = HashMap<String, () -> Object>()
    private let _singletons = HashMap<String, Object>()
    private let _lifetimes = HashMap<String, ServiceLifetime>()

    public init() {}

    // Register a service factory with the given lifetime
    public func register(name: String, factory: () -> Object, lifetime!: ServiceLifetime = Transient): Unit {
        _factories[name] = factory
        _lifetimes[name] = lifetime
        // Clear cached singleton if re-registering
        if (!_singletons.get(name).isNone()) {
            _singletons.remove(name)
        }
    }

    // Resolve a service by name; throws WebException if not registered
    public func resolve(name: String): Object {
        if (_factories.get(name).isNone()) {
            throw WebException("Service not found: ${name}")
        }
        let factory = _factories.get(name).getOrThrow()
        if (isSingleton(name)) {
            if (let Some(instance) <- _singletons.get(name)) {
                return instance
            }
            let instance = factory()
            _singletons[name] = instance
            return instance
        }
        return factory()
    }

    // Safely resolve a service; returns None if not registered
    public func resolveOrNone(name: String): ?Object {
        if (!contains(name)) {
            return None
        }
        return resolve(name)
    }

    // Check if a service is registered
    public func contains(name: String): Bool {
        return !_factories.get(name).isNone()
    }

    func isSingleton(name: String): Bool {
        let lifetime = _lifetimes.get(name).getOrThrow()
        match (lifetime) {
            case Singleton => true
            case Transient => false
        }
    }
}
