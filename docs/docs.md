<h1 id="pygalle">pygalle</h1>


---
This file is part of pygalle.core.base.klass
Copyright (c) 2018 SAS 9 Février.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---

<h1 id="pygalle.core">pygalle.core</h1>


---
This file is part of pygalle.core.base.klass
Copyright (c) 2018 SAS 9 Février.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---

<h1 id="pygalle.core.base">pygalle.core.base</h1>


This file is part of pygalle.core.base.klass
Copyright (c) 2018 SAS 9 Février.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---

<h1 id="pygalle.core.base.klass">pygalle.core.base.klass</h1>


A plugin class used by the Pygalle framework.

---
This file is part of pygalle.core.base.klass
Copyright (c) 2018 SAS 9 Février.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---

<h2 id="pygalle.core.base.klass.PygalleBaseClass">PygalleBaseClass</h2>

```python
PygalleBaseClass(self, **kwargs) -> 'PygalleBaseClass'
```
The plugin class for Pigalle framework, strictly used by the derived modules. For example:

   `̀̀python

   class CustomClass(PygalleBaseClass):
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)

       def hello(self, name):
           return 'hello %s' % name

   ̀̀̀

<h3 id="pygalle.core.base.klass.PygalleBaseClass.init_properties">init_properties</h3>

```python
PygalleBaseClass.init_properties(self) -> 'PygalleBaseClass'
```
Initialize the Pigalle properties.

__Returns:__

           PygalleBaseClass: The current instance.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.get_pigalle">get_pigalle</h3>

```python
PygalleBaseClass.get_pigalle(self, key:str) -> dict
```
Return value of a Pigalle property.

__Arguments__

- __key(str)__: The key of looked up Pigalle property.

__Returns:__

           object: The value of the Pigalle property.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.internals">internals</h3>

```python
PygalleBaseClass.internals(self) -> dict
```
Return Pigalle containing internals properties of the Pigalle instance.

       :return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.public">public</h3>

```python
PygalleBaseClass.public(self) -> dict
```
Return an object containing public properties of the Pigalle instance.

       :return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.set_internal">set_internal</h3>

```python
PygalleBaseClass.set_internal(self, key, value) -> 'PygalleBaseClass'
```
Define an internal property.

       :param key:
       :param value:
       :return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.get_internal">get_internal</h3>

```python
PygalleBaseClass.get_internal(self, key) -> Any
```


:param key:
:return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.set">set</h3>

```python
PygalleBaseClass.set(self, key:str, value:Any) -> 'PygalleBaseClass'
```
Define a public property.

       :param key:
       :param value:
       :return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.get">get</h3>

```python
PygalleBaseClass.get(self, key:str) -> Any
```
Return a public property corresponding to the provided key.

       :param key:
       :return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.get_uid">get_uid</h3>

```python
PygalleBaseClass.get_uid(self) -> str
```
Return the identifier of class instance.

       :return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.uid">uid</h3>

```python
PygalleBaseClass.uid(self) -> str
```
Return the identifier of class instance.

       :return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.set_uid">set_uid</h3>

```python
PygalleBaseClass.set_uid(self) -> 'PygalleBaseClass'
```


:return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.generate_uid">generate_uid</h3>

```python
PygalleBaseClass.generate_uid() -> str
```
Static helper method to generate an identifier.

       :return:

<h3 id="pygalle.core.base.klass.PygalleBaseClass.set_class_name">set_class_name</h3>

```python
PygalleBaseClass.set_class_name(self) -> 'PygalleBaseClass'
```
Store the class name of the current instance of
       :class:`PygalleBaseClass` into internal property.

__Returns:__

           PygalleBaseClass: An instance of :class:`PygalleBaseClass`

<h3 id="pygalle.core.base.klass.PygalleBaseClass.get_class_name">get_class_name</h3>

```python
PygalleBaseClass.get_class_name(self) -> str
```
__Returns __

<h3 id="pygalle.core.base.klass.PygalleBaseClass.set_category">set_category</h3>

```python
PygalleBaseClass.set_category(self, category:str=None) -> 'PygalleBaseClass'
```
Define the category of the class.

__Arguments__

- __category__: The name of category.

__Returns:__

           PygalleBaseClass: An instance of :class:`PygalleBaseClass`

<h3 id="pygalle.core.base.klass.PygalleBaseClass.get_category">get_category</h3>

```python
PygalleBaseClass.get_category(self) -> str
```
__Returns the class category__


__Returns:__

           str: The class category.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.category">category</h3>

```python
PygalleBaseClass.category(self) -> str
```
__Returns the class category.__


       __Alias to :method:`get_category`__

__Returns:__

           str: The class category.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.to_dict">to_dict</h3>

```python
PygalleBaseClass.to_dict(self) -> dict
```
__Returns a `dict` representation of current instance.__


__Returns:__

          dict: The `dict` representation of the current instance.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.to_object">to_object</h3>

```python
PygalleBaseClass.to_object(self) -> dict
```
__Returns a `dict` representation of current instance.__


      __Alias of :method:`to_object`.__

__Returns:__

          dict: The `dict` representation of the current instance.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.to_json">to_json</h3>

```python
PygalleBaseClass.to_json(self) -> str
```
__Returns a representation as JSON of the current instance.__


__Returns:__

           str: A JSON string.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.instance_of">instance_of</h3>

```python
PygalleBaseClass.instance_of(self, kls:Any) -> bool
```
Return true if the current object is an instance of passed type.

__Arguments__

- __kls__: The class.

__Returns:__

           bool:
             * Return true if the current object is an instance of passed type.
             * False else.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.is_pigalle_instance">is_pigalle_instance</h3>

```python
PygalleBaseClass.is_pigalle_instance(obj:Any) -> bool
```
Return true if the passed object as argument is an instance
       of class being to the Pigalle framework.

__Arguments__

- __obj__: The object to check.

__Returns:__

           bool:
               * True if object is Pigalle.
               * False else.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.is_pigalle_class">is_pigalle_class</h3>

```python
PygalleBaseClass.is_pigalle_class(kls:ClassVar) -> bool
```
Return true if the passed object as argument is a class being to the Pigalle framework.

__Arguments__

- __kls__: The class to check.

__Returns:__

           bool:
               * True if class is Pigalle.
               * False else.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.is_pigalle">is_pigalle</h3>

```python
PygalleBaseClass.is_pigalle(obj:Any) -> bool
```
Return true if the passed object as argument is a class or an
       instance of class being to the Pigalle framework.

__Arguments__

- __obj__: The class or object to test.

__Returns:__

           bool:
               * True if class or object is Pigalle.
               * False else.


<h3 id="pygalle.core.base.klass.PygalleBaseClass.is_parent_class_of">is_parent_class_of</h3>

```python
PygalleBaseClass.is_parent_class_of(obj:Any) -> bool
```
Check if the provided object is a children of the current class.

__Arguments__

- __obj__: The object to check.

__Returns:__

           bool:
               * True if the current class is a parent of provided object.
               * False else.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.has_method">has_method</h3>

```python
PygalleBaseClass.has_method(self, key:str) -> bool
```
Return if a method exists for the current instance.

__Arguments__

- __key__: The method name.

__Returns:__

           bool:
               * True if the current instance has the provided method.
               * False else.


<h3 id="pygalle.core.base.klass.PygalleBaseClass.factory">factory</h3>

```python
PygalleBaseClass.factory(**kwargs) -> 'PygalleBaseClass'
```
A static factory method to create a new instance of {PigalleBaseClass}.
           If method is called from a derived class, create a new instance of this class.

__Arguments__

- __*args__:
- __**kwargs__:

__Returns:__

           PygalleBaseClass: An instance of class or derived class.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.get_class">get_class</h3>

```python
PygalleBaseClass.get_class(obj:Any) -> Any
```
A static helper to get the class of the passed object.

__Arguments__

- __o__: An object.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.class_name">class_name</h3>

```python
PygalleBaseClass.class_name(obj:Any) -> str
```
A static helper to get the class name of the passed object.

__Arguments__

- __o__: An object.

__Returns:__

           str: The class name of provided object.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.is_class">is_class</h3>

```python
PygalleBaseClass.is_class(obj) -> bool
```
Static helper method to check if the passed object is a class.

__Arguments__

- __o__: An object to test if is a class.

__Returns:__

           bool:
               * True if the passed object is a class.
               * False else.

<h3 id="pygalle.core.base.klass.PygalleBaseClass.i_am_pigalle">i_am_pigalle</h3>

```python
PygalleBaseClass.i_am_pigalle() -> bool
```
Simple function to check if the class is a Pigalle class.

__Returns:__

           bool: Always true.


