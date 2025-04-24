"""
factory_decorator.py

Este módulo define un decorador genérico `@factory` que puede ser utilizado para funciones 
que actúan como fábricas de objetos. El decorador permite:

- Ejecutar lógica adicional antes y después de la creación del objeto.
- Validar que el objeto devuelto sea de un tipo esperado (opcional).
- Conservar los metadatos de la función original mediante `functools.wraps`.

Ejemplo de uso:

    @factory(expected_type=Hamburguesa)
    def crear_hamburguesa_cheddar():
        return Hamburguesa("cheddar", 150)

    burger = crear_hamburguesa_cheddar()

Parámetros:
    expected_type (type): Tipo esperado del objeto devuelto. Si se proporciona, el decorador
    validará que el objeto devuelto sea instancia de esa clase.

Dependencias:
    - functools (wraps)

"""


from functools import wraps
def factory(expected_type=None):
    """
    Decorador factory genérico que envuelve funciones de creación de objetos.

    :param expected_type: Clase esperada que debe devolver la función decorada (opcional).
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"🔧 Ejecutando factory: {func.__name__}")
            instance = func(*args, **kwargs)
            if expected_type and not isinstance(instance, expected_type):
                raise TypeError(
                    f"⚠️ Error: {func.__name__} no devolvió una instancia de {expected_type.__name__}"
                )
            print(f"✅ Objeto creado: {instance}")
            return instance

        return wrapper

    return decorator
