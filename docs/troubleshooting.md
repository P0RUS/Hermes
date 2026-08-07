## Jupyter doesn't recognize changes in a module

Symptom:

ImportError or old behavior after editing a file inside `hermes/`.

Solution:

```python
import importlib
import hermes.models

importlib.reload(hermes.models)